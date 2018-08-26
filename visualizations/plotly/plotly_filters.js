/**
 * The PlotlyFilters class updates a plotly graph by filtering the
 * data based on what is selected with checkboxes and sliders.
 *
 * Each data trace is tagged with a set of labels, only data traces
 * where all labels are selected are shown.
 *
 */
class PlotlyFilters {
    /**
     * @param {string} containerDiv the id of the container where
     *    the graph is drawn.
     * @param {object[]} labeled_data The list of traces for the
     *    plotly graph. Each trace has an attribute labels where
     *    labels for each category is looked up. Only traces where
     *    all labels are selected are shown.
     * @param {object} layout The layout to be given to plotly.
     * @param {object} config The config to be given to plotly.
     */
    constructor(containerDiv, labeled_data, layout, config) {
        this.containerDiv = containerDiv;
        this._slider_position = {};
        this._slider_labels = {};
        this._dropdown_position = {};
        this._dropdown_labels = {};
        this._checkbox_labels = {};
        this.data = labeled_data;
        this.layout = layout;
        if(!this.layout) this.layout = {};
        if(!this.layout.sliders) this.layout.sliders = [];
        if(!this.layout.updatemenus) this.layout.updatemenus = [];
        this.orig_menu = this.layout.updatemenus;
        this.config = config;
    }

    /**
     * @returns true if the label under the given category is
     * selected by a checkbox.
     */
    is_selected_checkbox(category, label){
        return this._checkbox_labels.hasOwnProperty(category) &&
               this._checkbox_labels[category].includes(label);
    }

    /**
     * selects a label under the given checkbox category.
     */
    select_checkbox(category, label){
        if(this.is_selected_checkbox(category, label)) return;
        if(!this._checkbox_labels.hasOwnProperty(category))
            this._checkbox_labels[category] = [];
        this._checkbox_labels[category].push(label);
    }

    /**
     * unselects a label under the given checkbox category.
     */
    unselect_checkbox(category, label){
        if(!this.is_selected_checkbox(category, label)) return;
        this._checkbox_labels[category] =
            this._checkbox_labels[category].filter(l => l !== label);
    }

    /**
     * @returns true if the label under the given category is
     * selected by a slider.
     */
    is_selected_slider(category, label){
        if(!this._slider_position.hasOwnProperty(category) ||
           !this._slider_labels.hasOwnProperty(category)){
            return false;
        }
        const position = this._slider_position[category];
        return this._slider_labels[category][position] === label;
    }

    /**
     * @returns true if the label under the given category is
     * selected by a dropdown menu.
     */
    is_selected_dropdown(category, label){
        if(!this._dropdown_position.hasOwnProperty(category) ||
           !this._dropdown_labels.hasOwnProperty(category)){
            return false;
        }
        const position = this._dropdown_position[category];
        return this._dropdown_labels[category][position] === label;
    }

    /**
     * @returns true if the label under the given category is
     * selected.
     */
    is_selected(category, label){
        return this.is_selected_checkbox(category, label) ||
               this.is_selected_slider(category, label) ||
               this.is_selected_dropdown(category, label);
    }

    /**
     * Adds a checkbox category with the given labels. Initially,
     * all labels are selected.
     */
    add_checkbox_category(name, labels){
        this._checkbox_labels[name] = labels;
    }

    /**
     * Adds a slider category with the given labels. Initially,
     * the first label is selected.
     */
    add_slider_category(name, labels){
        this._slider_position[name] = 0;
        labels.sort(this.compare_labels);
        this._slider_labels[name] = labels;
    }

    /**
     * Adds a dropdown category with the given labels. Initially,
     * the first label is selected.
     */
    add_dropdown_category(name, labels){
        this._dropdown_position[name] = 0;
        labels.sort(this.compare_labels);
        this._dropdown_labels[name] = labels;
    }

    /**
     * handles an onclick event for a checkbox. Assumes that
     * the label being clicked is in the value attribute of
     * the target and that the category is in the name attribute
     * of the target.
     */
    handle_checkbox_click(e){
        const target = e.target;
        const label = target.getAttribute('value');
        const category = target.getAttribute('name');
        if(target.checked){
            this.select_checkbox(category, label);
        } else {
            this.unselect_checkbox(category, label);
        }
        this.update_plot();
    }

    /**
     * Handles a 'plotly_sliderchange' event. Sets the selected
     * label.
     */
    handle_slider_changed(e){
        this._slider_position[e.slider.name] = e.slider.active;
        this.update_plot();
    }

    /**
     * Handles a 'plotly_buttonclicked' event. Sets the selected
     * label.
     */
    handle_button_clicked(e){
        this._dropdown_position[e.menu.name] = e.active;
        this.update_plot();
    }

    /**
     * @returns the list of datatraces where all labels are selected.
     */
    filtered_data() {
        const self = this;
        return this.data.filter(point =>
                Object.entries(point.labels).every(([category, label]) =>
                    self.is_selected(category, label)
                ));
    }

    /**
     * Redraws the plot.
     */
    update_plot() {
        const orig_sliders = this.layout.sliders;
        this.layout.sliders = this.layout.sliders.concat(
            this.slider_layout()
        );
        this.layout.updatemenus = this.orig_menu.concat([]);
        this.layout.updatemenus = this.layout.updatemenus.concat(
            this.dropdown_layout()
        );
        Plotly.newPlot(
            this.containerDiv,
            this.filtered_data(),
            this.layout,
            this.config);
        this.layout.sliders = orig_sliders;
        const thePlot = document.getElementById(this.containerDiv);
        thePlot.on(
            'plotly_sliderchange',
            this.handle_slider_changed.bind(this)
        );
        thePlot.on(
            'plotly_buttonclicked',
            this.handle_button_clicked.bind(this)
        );
    }

    /**
     * @returns The list of dropdown buttons as given in the layout parameter of
     *      plotly.newPlot.
     */
    dropdown_layout() {
        return Object.entries(this._dropdown_labels).map(([key, labels], idx) =>
              ({
                type: 'dropdown',
                name: key,
                y: -idx*0.10 + 1,
                active: this._dropdown_position[key],
                buttons: labels.map(label => ({
                  'label': label,
                  method: 'skip',
                  name: label,
                }))
              })
            );
    }

    /**
     * @returns The list of sliders as given in the layout parameter of
     *      plotly.newPlot.
     */
    slider_layout() {
        return Object.entries(this._slider_labels).map(([key, labels], idx) =>
              ({
                name: key,
                y: -idx*0.75,
                pad: {t: 40},
                currentvalue: {'prefix': key+': '},
                active: this._slider_position[key],
                steps: labels.map(label => ({
                  'label': label,
                  method: 'skip',
                  name: label,
                  value: label
                }))
              })
            );
    }

    /**
     * Compares two labels, used to sort labels for the slider.
     */
    compare_labels(a, b){
        if(typeof a === "string"){
                let adate = undefined, bdate = undefined;
            if((adate = Date.parse(a)) && (bdate = Date.parse(b))){
                return adate - bdate;
            } else {
                return a.localeCompare(b);
            }
        }
        return a - b;
    }
}
module.exports = {PlotlyFilters}
