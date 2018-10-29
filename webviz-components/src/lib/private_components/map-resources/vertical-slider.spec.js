import chai from 'chai'
import sinonChai from 'sinon-chai'
import sinon from 'sinon'
import jsdom from 'jsdom-global'
import * as d3 from 'd3'
import VerticalSlider from './vertical-slider'

const { expect } = chai
chai.use(sinonChai)

describe('Vertical slider', () => {
    beforeEach(() => {
        jsdom(
            `<body>
            </body>
        `,
        )
    })

    const createValidSlider = () => new VerticalSlider({
        parentElement: d3.select('body').append('svg'),
        values: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
        height: 470,
    })

    describe('constructor', () => {
        it('should validate the input', () => {
            const spy = sinon.spy(VerticalSlider.prototype, 'validate')

            const slider = createValidSlider()

            expect(spy).to.be.called
        })
    })

    describe('validate', () => {
        it('should throw an error if svg element is not provided', () => {
            const invalidSliderConstruction = () => new VerticalSlider()

            expect(invalidSliderConstruction).to.throw('Parent element not provided')
        })

        it('should throw an error if no values are provided', () => {
            const invalidSliderConstruction = () => new VerticalSlider({
                parentElement: d3.select('body').append('svg'),
            })

            expect(invalidSliderConstruction).to.throw('Values')
        })

        it('should throw an error if no height provided', () => {
            const invalidSliderConstruction = () => new VerticalSlider({
                parentElement: d3.select('body').append('svg'),
                values: ['0', '1', '2'],
            })

            expect(invalidSliderConstruction).to.throw('Height not provided')
        })
    })

    describe('render', () => {
        it('should render the container element', () => {
            const slider = createValidSlider()

            const spy = sinon.spy(slider, 'renderContainer')

            slider.render()

            expect(spy).to.be.called
        })

        it('should render the slider', () => {
            const slider = createValidSlider()

            const spy = sinon.spy(slider, 'renderSlider')

            slider.render()

            expect(spy).to.be.called
        })
    })

    describe('setPosition', () => {
        it('should set the internal position variable', () => {
            const slider = createValidSlider()

            slider.render()

            slider.setPosition({
                x: 100,
                y: 100,
            })

            expect(slider.position.x).to.equal(100)
            expect(slider.position.y).to.equal(100)
        })

        it('should set the transform attribute', () => {
            const slider = createValidSlider()

            slider.render()

            slider.setPosition({
                x: 50,
                y: 70,
            })

            const element = d3.select('body #g_slider')
            expect(element.attr('transform')).to.equal('translate(50,70)')
        })
    })

    // Private method - since there is no way to test dragging in unit test
    describe('_onDragSlider', () => {
        it('should emit changed event with the current value of the slider', () => {
            const slider = createValidSlider()

            slider.render()

            const spy = sinon.spy(slider, 'emit')

            slider._onDragSlider(1)

            expect(spy).to.be.calledWith('change')
        })

        it('should not emit the changed event when the drag is below the threshold', () => {
            const slider = createValidSlider()

            slider.render()

            const spy = sinon.spy(slider, 'emit')

            slider._onDragSlider(0.2)

            expect(spy).not.to.be.calledWith('change')
        })
    })
})
