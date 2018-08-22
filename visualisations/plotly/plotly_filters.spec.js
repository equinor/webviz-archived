const {expect} = require('chai');
const {PlotlyFilters} = require('./plotly_checkboxes');

describe('PlotlyFilters', function() {
    let filters = undefined
    beforeEach(function() {
        filters = new PlotlyFilters('div', [], {}, {})
    });
    it('select/unselect are idenpotent', function() {
        filters.select_checkbox('name', 'label');
        expect(filters.is_selected('name', 'label')).to.equal(true);
        filters.unselect_checkbox('name', 'label');
        expect(filters.is_selected('name', 'label')).to.equal(false);
    });
    it('add_checkbox_category selects all', function() {
        filters.add_checkbox_category('name', ['label1', 'label2']);
        expect(filters.is_selected('name', 'label1')).to.equal(true);
        expect(filters.is_selected('name', 'label2')).to.equal(true);
    });
    it('add_slider_category selects first', function() {
        filters.add_slider_category('name', ['label1', 'label2']);
        expect(filters.is_selected('name', 'label1')).to.equal(true);
        expect(filters.is_selected('name', 'label2')).to.equal(false);
    });
});
