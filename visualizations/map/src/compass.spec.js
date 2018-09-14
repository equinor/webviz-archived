/* eslint-env node, mocha */
import chai from 'chai'
import sinonChai from 'sinon-chai'
import sinon from 'sinon'
import jsdom from 'jsdom-global'
import * as d3 from 'd3'
import Compass from './compass'
import SVGTransform from './util'

const { expect } = chai
chai.use(sinonChai)

describe('Compass component', () => {
    beforeEach(() => {
        jsdom(
            `<body>
            </body>
        `,
        )
    })

    const createValidCompass = () => {
        const svg = d3.select('body').append('svg')

        const compass = new Compass({
            parentElement: svg,
        })

        return compass
    }

    describe('init', () => {
        it('should init the default events', () => {
            const compass = new Compass({
                parentElement: {},
            })

            sinon.spy(compass, 'initEvents')

            compass.init()
        })
    })

    describe('initDragEvents', () => {
        it('should initialize the drag events', () => {
            const compass = createValidCompass()

            compass.render()
            const spy = sinon.spy(compass.element, 'call')

            compass.initDragEvents()

            expect(spy).to.be.called
        })
    })

    describe('constructor', () => {
        it('should validate the input', () => {
            const spy = sinon.spy(Compass.prototype, 'validate')

            createValidCompass()

            expect(spy).to.be.called
        })

        it('should throw an error if svg element is not provided', () => {
            const invalidCompassConstruction = () => new Compass()

            expect(invalidCompassConstruction).to.throw('Parent element not provided')
        })

        it('should not throw an error if svg element is provided', () => {
            expect(createValidCompass).not.to.throw('Parent element not provided')
        })

        it('should set position.x to 0 if no initialPosition is provided', () => {
            const compass = createValidCompass()

            expect(compass.position.x).to.be.equal(0)
        })

        it('should set position.y to 0 if no initialPosition is provided', () => {
            const compass = createValidCompass()

            expect(compass.position.y).to.be.equal(0)
        })

        it('should set position.x to initialPosition.x if initialPosition is provided', () => {
            const initialPosition = {
                x: 50,
                y: 50,
            }
            const compass = new Compass({
                parentElement: d3.select('body').append('svg'),
                initialPosition,
            })

            expect(compass.position.x).to.be.equal(initialPosition.x)
        })

        it('should set position.y to initialPosition.y if initialPosition is provided', () => {
            const initialPosition = {
                x: 50,
                y: 60,
            }

            const compass = new Compass({
                parentElement: d3.select('body').append('svg'),
                initialPosition,
            })

            expect(compass.position.y).to.be.equal(initialPosition.y)
        })

        it('should set rotation to 0 if no initialRotation is provided', () => {
            const compass = createValidCompass()

            expect(compass.initialRotation).to.be.equal(0)
        })

        it('should set rotation to initialRotation if initialRotation is provided', () => {
            const initialRotation = 30

            const compass = new Compass({
                parentElement: d3.select('body').append('svg'),
                initialRotation,
            })

            expect(compass.initialRotation).to.be.equal(initialRotation)
        })
    })

    describe('render', () => {
        it('should create the compass element inside the parent element', () => {
            const compass = createValidCompass()
            const spy = sinon.spy(compass, 'renderContainer')

            compass.render()

            expect(spy).to.be.called

            const selectionArray = d3.selectAll('#g_compass')

            expect(selectionArray.empty()).to.be.false
        })

        it('should set the position of the compass elemenent', () => {
            const initialPosition = {
                x: 50,
                y: 60,
            }
            const compass = new Compass({
                parentElement: d3.select('body').append('svg'),
                initialPosition,
            })

            compass.render()

            const compassElement = d3.select('#g_compass')
            const { transform } = new SVGTransform(compassElement.attr('transform'))

            expect(transform.translate).to.be.ok
            expect(transform.translate[0]).to.be.equal(`${initialPosition.x}`)
            expect(transform.translate[1]).to.be.equal(`${initialPosition.y}`)
        })

        it('should set the rotation of the compass elemenent', () => {
            const initialRotation = 0
            const compass = new Compass({
                parentElement: d3.select('body').append('svg'),
                initialRotation,
            })

            compass.render()

            const compassElement = d3.select('#g_compass')
            const { transform } = new SVGTransform(compassElement.attr('transform'))

            expect(transform.rotate).to.be.ok
            expect(transform.rotate[0]).to.be.equal(`${initialRotation}`)
            expect(transform.rotate[1]).to.be.equal(`${100}`)
            expect(transform.rotate[2]).to.be.equal(`${100}`)
        })


        it('should render the compass shape', () => {
            const compass = createValidCompass()
            const spy = sinon.spy(compass, 'renderShape')

            compass.render()

            expect(spy).to.be.called
        })

        it('should render the direction letters', () => {
            const compass = createValidCompass()
            const spy = sinon.spy(compass, 'renderLetters')

            compass.render()

            expect(spy).to.be.called
        })
    })
})
