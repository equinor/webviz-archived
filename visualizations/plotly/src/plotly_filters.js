var Plotly = require('plotly.js');

function contains(obj, prop) {
    return Object.prototype.hasOwnProperty.call(obj, prop)
}
/**
 * The PlotlyFilters class updates a plotly graph by filtering the
 * data based on what is selected with checkboxes and sliders.
 *
 * Each data trace is tagged with a set of labels, only data traces
 * where all labels are selected are shown.
 *
 */
export default class PlotlyFilters {
    /**
     * @param {string} containerDiv the id of the container where
     *    the graph is drawn.
     * @param {object[]} labeledData The list of traces for the
     *    plotly graph. Each trace has an attribute labels where
     *    labels for each category is looked up. Only traces where
     *    all labels are selected are shown.
     * @param {object} layout The layout to be given to plotly.
     * @param {object} config The config to be given to plotly.
     */
    constructor(containerDiv, labeledData, layout, config) {
        this.containerDiv = containerDiv
        this._sliderPosition = {}
        this._sliderLabels = {}
        this._dropdownPosition = {}
        this._dropdownLabels = {}
        this._checkboxLabels = {}
        this.data = labeledData
        this.layout = layout
        if (!this.layout) this.layout = {}
        if (!this.layout.sliders) this.layout.sliders = []
        if (!this.layout.updatemenus) this.layout.updatemenus = []
        this.origMenu = this.layout.updatemenus
        this.config = config
    }

    /**
     * @returns true if the label under the given category is
     * selected by a checkbox.
     */
    isSelectedCheckbox(category, label) {
        return contains(this._checkboxLabels, category)
               && this._checkboxLabels[category].includes(label)
    }

    /**
     * selects a label under the given checkbox category.
     */
    selectCheckbox(category, label) {
        if (this.isSelectedCheckbox(category, label)) return
        if (!contains(this._checkboxLabels, category)) {
            this._checkboxLabels[category] = []
        }
        this._checkboxLabels[category].push(label)
    }

    /**
     * unselects a label under the given checkbox category.
     */
    unselectCheckbox(category, label) {
        if (!this.isSelectedCheckbox(category, label)) return
        this._checkboxLabels[category] = this._checkboxLabels[category].filter(l => l !== label)
    }

    /**
     * @returns true if the label under the given category is
     * selected by a slider.
     */
    isSelectedSlider(category, label) {
        if (!contains(this._sliderPosition, category)
           || !contains(this._sliderLabels, category)) {
            return false
        }
        const position = this._sliderPosition[category]
        return this._sliderLabels[category][position] === label
    }

    /**
     * @returns true if the label under the given category is
     * selected by a dropdown menu.
     */
    isSelectedDropdown(category, label) {
        if (!contains(this._dropdownPosition, category)
           || !contains(this._dropdownLabels, category)) {
            return false
        }
        const position = this._dropdownPosition[category]
        return this._dropdownLabels[category][position] === label
    }

    /**
     * @returns true if the label under the given category is
     * selected.
     */
    isSelected(category, label) {
        return this.isSelectedCheckbox(category, label)
               || this.isSelectedSlider(category, label)
               || this.isSelectedDropdown(category, label)
    }

    /**
     * Adds a checkbox category with the given labels. Initially,
     * all labels are selected.
     */
    addCheckboxCategory(name, labels) {
        this._checkboxLabels[name] = labels
    }

    /**
     * Adds a slider category with the given labels. Initially,
     * the first label is selected.
     */
    addSliderCategory(name, labels) {
        this._sliderPosition[name] = 0
        labels.sort(this.compareLabels)
        this._sliderLabels[name] = labels
    }

    /**
     * Adds a dropdown category with the given labels. Initially,
     * the first label is selected.
     */
    addDropdownCategory(name, labels) {
        this._dropdownPosition[name] = 0
        labels.sort(this.compareLabels)
        this._dropdownLabels[name] = labels
    }

    /**
     * handles an onclick event for a checkbox. Assumes that
     * the label being clicked is in the value attribute of
     * the target and that the category is in the name attribute
     * of the target.
     */
    handleCheckboxClick(e) {
        const { target } = e
        const label = target.getAttribute('value')
        const category = target.getAttribute('name')
        if (target.checked) {
            this.selectCheckbox(category, label)
        } else {
            this.unselectCheckbox(category, label)
        }
        this.updatePlot()
    }

    /**
     * Handles a 'plotly_sliderchange' event. Sets the selected
     * label.
     */
    handleSliderChanged(e) {
        this._sliderPosition[e.slider.name] = e.slider.active
        this.updatePlot()
    }

    /**
     * Handles a 'plotly_buttonclicked' event. Sets the selected
     * label.
     */
    handleButtonClicked(e) {
        this._dropdownPosition[e.menu.name] = e.active
        this.updatePlot()
    }

    /**
     * @returns the list of datatraces where all labels are selected.
     */
    filteredData() {
        const self = this
        return this.data.filter(
            point => Object.entries(point.labels).every(
                ([category, label]) => self.isSelected(category, label),
            ),
        )
    }

    /**
     * Redraws the plot.
     */
    updatePlot() {
        const origSliders = this.layout.sliders
        this.layout.sliders = this.layout.sliders.concat(
            this.sliderLayout(),
        )
        this.layout.updatemenus = this.origMenu.concat([])
        this.layout.updatemenus = this.layout.updatemenus.concat(
            this.dropdownLayout(),
        )
        Plotly.newPlot(
            this.containerDiv,
            this.filteredData(),
            this.layout,
            this.config,
        )
        this.layout.sliders = origSliders
        const thePlot = document.getElementById(this.containerDiv)
        thePlot.on(
            'plotly_sliderchange',
            this.handleSliderChanged.bind(this),
        )
        thePlot.on(
            'plotly_buttonclicked',
            this.handleButtonClicked.bind(this),
        )
    }

    /**
     * @returns The list of dropdown buttons as given in the layout parameter of
     *      plotly.newPlot.
     */
    dropdownLayout() {
        return Object.entries(this._dropdownLabels).map(([key, labels], idx) => ({
            type: 'dropdown',
            name: key,
            y: -idx * 0.10 + 1,
            active: this._dropdownPosition[key],
            buttons: labels.map(label => ({
                label,
                method: 'skip',
                name: label,
            })),
        }))
    }

    /**
     * @returns The list of sliders as given in the layout parameter of
     *      plotly.newPlot.
     */
    sliderLayout() {
        return Object.entries(this._sliderLabels).map(([key, labels], idx) => ({
            name: key,
            y: -idx * 0.75,
            pad: { t: 40 },
            currentvalue: { prefix: `${key}: ` },
            active: this._sliderPosition[key],
            steps: labels.map(label => ({
                label,
                method: 'skip',
                name: label,
                value: label,
            })),
        }))
    }

    /**
     * Compares two labels, used to sort labels for the slider.
     */
    compareLabels(a, b) {
        if (typeof a === 'string') {
            const adate = Date.parse(a)
            const bdate = Date.parse(b)
            if (adate && bdate) {
                return adate - bdate
            }
            return a.localeCompare(b)
        }
        return a - b
    }
}
