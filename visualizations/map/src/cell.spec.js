import jsc from 'jsverify'
import {
    arbitraryCell,
    arbitraryNonEmptyCell,
    arbitraryPoint,
} from './arbitraries'


describe('Cell', () => {
    jsc.property(
        'has consistent i setter/getter',
        arbitraryCell,
        jsc.nat,
        (cell, n) => {
            cell.i = n
            return cell.i === n
        },
    )

    jsc.property(
        'has consistent j setter/getter',
        arbitraryCell,
        jsc.nat,
        (cell, n) => {
            cell.j = n
            return cell.j === n
        },
    )

    jsc.property(
        'non-empty cells have non-zero jacobian determinant',
        arbitraryNonEmptyCell,
        arbitraryPoint,
        (cell, point) => Math.abs(cell.jacobian(point).determinant()) !== 0,
    )

    jsc.property(
        'Positive flux, modulo jacobian determinant, means positive velocity',
        jsc.suchthat(
            arbitraryNonEmptyCell,
            jsc.bool,
            c => c.flux.values().every(x => x >= 0),
        ),
        arbitraryPoint,
        (cell, point) => {
            const det = cell.jacobian(point).determinant()
            return cell.normalVelocity(point)
                .values()
                .every(x => x * det >= 0)
        },
    )
})
