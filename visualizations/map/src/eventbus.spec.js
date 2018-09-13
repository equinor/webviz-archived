import chai from 'chai'
import sinonChai from 'sinon-chai'
import sinon from 'sinon'
import EventBus from './eventbus'

const { expect } = chai
chai.use(sinonChai)


describe('Event bus', () => {
    describe('on', () => {
        it('should throw an error if no event name is provided', () => {
            const bus = new EventBus()

            const noEventNameProvided = () => {
                bus.on()
            }

            expect(noEventNameProvided).to.throw('No event name provided')
        })

        it('should throw an error if no handler is provided', () => {
            const bus = new EventBus()

            const noHandlerProvided = () => {
                bus.on('event')
            }

            expect(noHandlerProvided).to.throw('No handler provided')
        })

        it('should add a handler in the array of handlers for a event', () => {
            const bus = new EventBus()
            const handler = () => {

            }

            bus.on('event', handler)

            expect(bus.events.event).to.contain(handler)
        })
    })

    describe('emit', () => {
        it('should throw an error if no event name is provided', () => {
            const bus = new EventBus()

            const noEventNameProvided = () => {
                bus.emit()
            }

            expect(noEventNameProvided).to.throw('No event name provided')
        })

        it('should call all the handlers from the array of handlers for an event', () => {
            const bus = new EventBus()
            const handler = sinon.spy()

            bus.on('event', handler)

            bus.emit('event')

            expect(handler).to.be.called
        })
    })

    describe('off', () => {
        it('should throw an error if no event name is provided', () => {
            const bus = new EventBus()

            const noEventNameProvided = () => {
                bus.off()
            }

            expect(noEventNameProvided).to.throw('No event name provided')
        })

        it('should throw an error if no handler is provided', () => {
            const bus = new EventBus()

            const noHandlerProvided = () => {
                bus.off('event')
            }

            expect(noHandlerProvided).to.throw('No handler provided')
        })

        it('should remove the handler from array of handlers for an event', () => {
            const bus = new EventBus()
            const handler = sinon.spy()

            bus.on('event', handler)

            bus.off('event', handler)

            expect(bus.events.event).to.not.contain(handler)
        })
    })
})
