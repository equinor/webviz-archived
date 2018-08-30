import * as d3 from 'd3'
import Component from './component'

export default class VerticalSlider extends Component {
    constructor(config = {}) {
        super()
        this.validate(config)

        this.parentElement = config.parentElement
        this.values = config.values
        this.value = 0

        this.scale = d3.scaleLinear()
            .domain([0, this.values.length - 1])
            .range([0, config.height])
            .clamp(true)

        if (config.initialPosition) {
            this.position = {
                x: config.initialPosition.x,
                y: config.initialPosition.y,
            }
        } else {
            this.position = {
                x: 0,
                y: 0,
            }
        }
    }

    validate(config) {
        if (!config.parentElement) {
            throw new Error('Parent element not provided')
        }

        if (!config.values) {
            throw new Error('Values not provided')
        }

        if (!config.height) {
            throw new Error('Height not provided')
        }
    }

    setPosition({ x, y }) {
        this.position.x = x
        this.position.y = y

        this.element.attr('transform', `translate(${x},${y})`)
    }

    render() {
        this.renderContainer()
        this.renderSlider()
    }

    renderContainer() {
        this.element = this.parentElement.append('g')
            .attr('id', 'g_slider')
            .attr('transform', `translate(${this.position.x}, ${this.position.y})`)
    }

    renderSlider() {
        this._renderLine()
        this._renderHandle()
        this._renderLabel()
    }

    _renderLine() {
        this.slider = this.element.append('g')
            .attr('class', 'slider')

        this.slider.append('line')
            .attr('class', 'track')
            .attr('y1', this.scale.range()[0])
            .attr('y2', this.scale.range()[1])
            .select(function () {
                return this.parentNode.appendChild(this.cloneNode(true))
            })
            .attr('class', 'track-inset')
            .select(function () {
                return this.parentNode.appendChild(this.cloneNode(true))
            })
            .attr('class', 'track-overlay')
            .call(d3.drag()
                .on('start.interrupt', () => {
                    this.slider.interrupt()
                })
                .on('start drag', () => {
                    this._onDragSlider(this.scale.invert(d3.event.y))
                }))
    }

    _onDragSlider(h) {
        if (Math.round(h) !== this.value) {
            this.value = Math.round(h)

            this.handle.attr('cy', this.scale(this.value))

            this.text.attr('y', this.scale(this.value))
                .text(this.values[this.value])

            this.emit('change', this.value)
        }
    }

    _renderHandle() {
        this.handle = this.slider.insert('circle', '.track-overlay')
            .attr('class', 'handle')
            .attr('r', 9)
    }

    _renderLabel() {
        this.text = this.slider.append('text')
            .text(this.values[this.value])
            .attr('x', -12)
            .attr('y', 0)
            .style('font-size', 30)
            .attr('text-anchor', 'end')
            .attr('cursor', 'default')
            .attr('alignment-baseline', 'middle')
    }
}
