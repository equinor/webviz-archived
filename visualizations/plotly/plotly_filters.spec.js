const { expect } = require('chai')
const { PlotlyFilters } = require('./plotly_filters')

describe('PlotlyFilters', () => {
    let filters
    beforeEach(() => {
        filters = new PlotlyFilters('div', [], {}, {})
    })
    it('select/unselect are idenpotent', () => {
        filters.selectCheckbox('name', 'label')
        expect(filters.isSelected('name', 'label')).to.equal(true)
        filters.unselectCheckbox('name', 'label')
        expect(filters.isSelected('name', 'label')).to.equal(false)
    })
    it('addCheckboxCategory selects all', () => {
        filters.addCheckboxCategory('name', ['label1', 'label2'])
        expect(filters.isSelected('name', 'label1')).to.equal(true)
        expect(filters.isSelected('name', 'label2')).to.equal(true)
    })
    it('addSliderCategory selects first', () => {
        filters.addSliderCategory('name', ['label1', 'label2'])
        expect(filters.isSelected('name', 'label1')).to.equal(true)
        expect(filters.isSelected('name', 'label2')).to.equal(false)
    })
})
