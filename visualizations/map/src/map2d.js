import * as d3 from 'd3'
import Map from './map'
import Compass from './compass'
import DistanceScale from './distance-scale'
import ColorScale from './color-scale'
import InfoBox from './infobox'
import VerticalSlider from './vertical-slider'
import Component from './component'

export default class Map2D extends Component {
    constructor(config, height) {
        super()
        this.elementSelector = config.elementSelector
        this.plotOptions = config.plotOptions
        this.coords = config.coords
        this.values = config.values

        this.MARGIN = {
            TOP: 50,
            RIGHT: 200,
            BOTTOM: 20,
            LEFT: 40,
        }

        this._calculateDimensions(height)
    }

    _calculateDimensions(height) {
        this.width = d3.select(this.elementSelector).node().offsetWidth
        this.height = height

        const xRange = this.plotOptions.xMax - this.plotOptions.xMin
        const yRange = this.plotOptions.yMax - this.plotOptions.yMin

        if (xRange / this.width > yRange / this.height) {
            this.kInit = this.width / this.plotOptions.precisionCoord
            if (yRange > xRange) {
                this.kInit *= yRange / xRange
            }
            this.scaleToRealCoord = xRange / this.plotOptions.precisionCoord
            this.origMeter2Px = this.width / xRange / this.kInit
        } else {
            this.kInit = this.height / this.plotOptions.precisionCoord
            if (xRange > yRange) {
                this.kInit *= xRange / yRange
            }
            this.scaleToRealCoord = yRange / this.plotOptions.precisionCoord
            this.origMeter2Px = this.height / yRange / this.kInit
        }

        this.mapTransform = {
            x: 0,
            y: 0,
            k: this.kInit,
            angle: 0,
        }
    }

    _isHorizontal() {
        const xRange = this.plotOptions.xMax - this.plotOptions.xMin
        const yRange = this.plotOptions.yMax - this.plotOptions.yMin

        return xRange / this.width > yRange / this.height
    }

    init() {
        this.initColorScale()
        this.initContainer()
        this.initContainerBorder()

        this.initMap()
        this.initZoom()

        this.initCompass()
        this.initLayerSlider()
        this.initDistanceScale()
        this.initInfoBox()
        this.initDepthScale()

        this.initResize()
    }

    initColorScale() {
        let colorScale
        switch (this.plotOptions.colorMap) {
            case 'viridis':
                colorScale = d3.interpolateViridis
                break
            case 'inferno':
                colorScale = d3.interpolateInferno
                break
            case 'warm':
                colorScale = d3.interpolateWarm
                break
            case 'cool':
                colorScale = d3.interpolateCool
                break
            case 'rainbow':
                colorScale = d3.interpolateRainbow
                break
            default:
                colorScale = d3.interpolateViridis
                break
        }

        this.colorScale = colorScale
    }

    initContainer() {
        this.containerMap = d3.select(this.elementSelector)
            .attr('class', 'map_2d')
            .append('svg')
            .attr('id', 'svg_map')
            .attr('width', this.width)
            .attr('height', this.height)

        this.containerControls = d3.select(this.elementSelector)
            .append('svg')
            .attr('id', 'svg_controls')
            .style('z-index', 10)
            .style('pointer-events', 'none')
            .attr('width', this.width)
            .attr('height', this.height)
    }

    initContainerBorder() {
        this.containerControls.append('rect')
            .attr('width', '100%')
            .attr('height', '100%')
            .attr('fill', 'none')
            .attr('stroke', '#aaaaaa')
            .attr('stroke-width', '2')
    }

    initMap() {
        this.map = new Map({
            parentElement: this.containerMap,
            coords: this.coords,
            values: this.values,
            colorScale: this.colorScale,
        })

        this.map.setTransform(this.mapTransform)

        this.map.render()

        this.map.on('mousemove', (info) => {
            this.infoBox.setX(`x = ${this._calculateXCoord(info.x)}`)
            this.infoBox.setY(`y = ${this._calculateYCoord(info.y)}`)
            this.infoBox.setValue(
                `${this._calculateValue(info.value)} ${this.plotOptions.valUnit}`,
            )
        })

        this.map.on('mouseleave', () => {
            this.infoBox.setX('')
            this.infoBox.setY('')
            this.infoBox.setValue('')
        })
    }

    _calculateXCoord(x) {
        return parseFloat(((this.scaleToRealCoord * x + this.plotOptions.xMin))
            .toPrecision(4))
    }

    _calculateYCoord(y) {
        return parseFloat(((this.plotOptions.yMax - this.scaleToRealCoord * y))
            .toPrecision(4))
    }

    _calculateValue(value) {
        return parseFloat((((this.plotOptions.maxVal - this.plotOptions.minVal)
            * (value / this.plotOptions.precisionValues) + this.plotOptions.minVal))
            .toPrecision(3))
    }

    initZoom() {
        const zoomListener = d3.zoom()
            .scaleExtent([0.1, 20])
            .on('zoom', this.handleZoom.bind(this))

        zoomListener(this.containerMap)
    }

    handleZoom() {
        const { transform } = d3.event

        this.mapTransform.x = transform.x
        this.mapTransform.y = transform.y
        this.mapTransform.k = transform.k * this.kInit

        this.scale.setK(this.mapTransform.k)
        this.map.setTransform(this.mapTransform)
        this.emit('zoom', this.mapTransform)
    }

    initCompass() {
        this.compass = new Compass({
            parentElement: this.containerControls,
            initialPosition: {
                x: this.width - 200,
                y: 0,
            },
        })

        this.compass.render()

        this.compass.initDragEvents()
        this.compass.on('dragged', (angle) => {
            this.mapTransform.angle = angle
            this.map.setTransform(this.mapTransform)
            this.emit('rotate', this.mapTransform)
        })
    }

    initLayerSlider() {
        if (this.plotOptions.layerNames.length > 1) {
            this.layerSlider = new VerticalSlider({
                parentElement: this.containerControls,
                initialPosition: {
                    x: this.width - 20,
                    y: this.MARGIN.TOP + 160,
                },
                values: this.plotOptions.layerNames,
                height: this.height - this.MARGIN.TOP - this.MARGIN.BOTTOM - 160,
            })

            this.layerSlider.render()

            this.layerSlider.on('change', (value) => {
                this.map.setLayer(value)
            })
        }
    }

    initDistanceScale() {
        this.scale = new DistanceScale({
            parentElement: this.containerControls,
            initialK: this.kInit,
            origMeter2Px: this.origMeter2Px,
            initialPosition: {
                x: 45,
                y: 45,
            },
        })

        this.scale.render()
    }

    initInfoBox() {
        this.infoBox = new InfoBox({
            parentElement: this.containerControls,
            initialPosition: {
                x: 0,
                y: this.height - 70,
            },
        })

        this.infoBox.render()
    }

    initDepthScale() {
        this.depthScale = new ColorScale({
            parentElement: this.containerControls,
            scale: this.colorScale,
            initialPosition: {
                x: 45,
                y: 60,
            },
            labelMin: `${this._calculateMinVal()} ${this.plotOptions.valUnit}`,
            labelMax: `${this._calculateMaxVal()} ${this.plotOptions.valUnit}`,
        })

        this.depthScale.render()
    }

    _calculateMinVal() {
        return parseFloat(this.plotOptions.minVal.toPrecision(3))
    }

    _calculateMaxVal() {
        return parseFloat(this.plotOptions.maxVal.toPrecision(3))
    }

    initResize() {
        const resize = () => {
            this.width = d3.select(this.elementSelector).node()
                .offsetWidth

            this.containerMap.attr('width', this.width)
            this.containerControls.attr('width', this.width)

            this.compass.setPosition({
                x: this.width - 200,
                y: 0,
            })

            this.layerSlider.setPosition({
                x: this.width - 20,
                y: this.MARGIN.TOP + 160,
            })
        }

        window.addEventListener('resize', resize)
    }
}
