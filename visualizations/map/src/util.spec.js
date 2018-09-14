import chai from 'chai'
import sinonChai from 'sinon-chai'
import sinon from 'sinon'
import SVGTransform from './util'

const { expect } = chai
chai.use(sinonChai)

describe('SVGTransform', () => {
    describe('constructor', () => {
        it('should parse the transform string', () => {
            const spy = sinon.spy(SVGTransform.prototype, 'parseTransform')

            const transform = new SVGTransform()

            expect(spy).to.be.called
        })
    })

    describe('addTransform', () => {
        it('should add a transform if it doesn\'t exist', () => {
            const transform = new SVGTransform()

            expect(transform.transform.translate).to.be.undefined

            transform.addTransform('translate', [0, 0])

            expect(transform.transform.translate).to.be.deep.equal(['0', '0'])
        })

        it('should correctly update an existing transform', () => {
            const transform = new SVGTransform('translate(0,0)')

            expect(transform.transform.translate).to.deep.equal(['0', '0'])

            transform.addTransform('translate', [100, 100])

            expect(transform.transform.translate).to.deep.equal(['100', '100'])
        })
    })
})
