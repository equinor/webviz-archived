import * as d3 from 'd3'
import Component from './component'

export default class Map extends Component {
    constructor(config = {}) {
        super()

        this.validate(config)

        this.layer = 0
        this.parentElement = config.parentElement
        this.coords = config.coords
        this.values = config.values
        this.valMin = config.valMin
        this.valMax = config.valMax
        this.colorScale = config.colorScale
        this.mapTransform = {
            x: 0,
            y: 0,
            k: 0,
            angle: 0,
        }
    }

    validate(config) {
        if (!config.parentElement) {
            throw new Error('Parent element not provided')
        }

        if (!config.coords) {
            throw new Error('Coords not provided')
        }

        if (!config.values) {
            throw new Error('Values not provided')
        }

        if (!config.colorScale) {
            throw new Error('Color scale not provided')
        }
    }

    render() {
        this.renderContainer()
        this.renderCells()
    }

    renderContainer() {
        this.element = this.parentElement.append('g')
            .attr('id', 'g_map_cells')
    }

    color(i) {
        return this.colorScale(
            (this.values[this.layer][i] - this.valMin)
            / (this.valMax - this.valMin),
        )
    }

    renderCells() {
        const self = this

        this.map = this.element.selectAll('polygon')
            .data(this.coords[this.layer])

        this.map.enter()
            .append('polygon')
            .merge(this.map)
            .attr('points', (d) => d.map(x => x.join(',')).map(x => x.join(' ')))
            .attr('fill', (d, i) => this.color(i))
            .on('mousemove', (d, i) => self.emit('mousemove', {
                x: d3.mouse(this)[0],
                y: d3.mouse(this)[1],
                value: self.values[self.layer][i],
            }))
            .on('mouseleave', () => self.emit('mouseleave'))

        this.map.exit()
            .remove()

        if (this.mapWidth === undefined) {
            this.mapWidth = this.element.node()
                .getBoundingClientRect()
                .width
        }

        if (this.mapHeight === undefined) {
            this.mapHeight = this.element.node()
                .getBoundingClientRect()
                .height
        }

        this.element.attr('transform', this.getMapTransform())
    }

    setTransform(transform) {
        this.mapTransform = transform

        if (this.element) {
            this.element.attr('transform', this.getMapTransform())
        }
    }

    getMapTransform() {
        return `translate(${this.mapTransform.x},${this.mapTransform.y})`
            + ` scale(${this.mapTransform.k})`
            + ` rotate(${this.mapTransform.angle}, ${this.mapWidth / 2},${this.mapHeight / 2})`
    }

    setLayer(layer) {
        this.layer = layer
        this.renderCells()
    }
}
