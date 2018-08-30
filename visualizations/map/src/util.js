/**
 * Utility class for handling transform attribute in an svg element
 */
export default class SVGTransform {
    constructor(transform) {
        this.transform = this.parseTransform(transform)
    }

    addTransform(type, params) {
        this.transform[type] = params.map((item) => `${item}`)
    }

    /**
     * Outputs the convenience transforms object back into string (which is put inside the SVG transform attribute)
     */
    toString() {
        const transforms = Object.entries(this.transform)

        const transformString = transforms.reduce((accumulator, currentValue) => {
            const values = currentValue[1].join(',')

            return `${accumulator} ${currentValue[0]}(${values})`
        }, '')

        return transformString
    }
}
