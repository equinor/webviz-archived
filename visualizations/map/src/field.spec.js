import jsc from 'jsverify'
import { isEqual } from 'lodash'
import { outsideUnitSquare } from './cell'
import { arbitraryField, arbitraryPoint } from './arbitraries'

describe('Field', () => {
    jsc.property(
        'If inside unit square, does not change cell',
        arbitraryField,
        arbitraryPoint,
        (field, point) => {
            const { grid } = field
            const cell = grid.getCell(0, 0)
            if (cell === undefined) return true
            if (!outsideUnitSquare(...point)) {
                const [newCell, newPoint] = field.calculateNewCell(point, cell)
                return isEqual(newCell, cell)
                    && isEqual(newPoint, point)
            }
            return true
        },
    )
})
