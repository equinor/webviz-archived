const { PlotlyFilters } = require('./plotly_filters')

function make_filter_checkboxes(containerId, labels, filters) {
    const boxes = {}
    filters.forEach((key, ki) => labels[key].forEach((label, li) => {
        if (!boxes[key]) boxes[key] = {}
        boxes[key][label] = document.querySelector(
            `#box${ki}-${li}${containerId}`,
        )
    }))
    return boxes
}

const global = window || {}

global.make_filtered_plotly = function (
    containerId,
    data,
    layout,
    config,
    labels,
    slider_filters,
    check_box_filters,
) {
    const boxes = make_filter_checkboxes(
        containerId,
        labels,
        check_box_filters,
    )
    const filtered = new PlotlyFilters(
        containerId,
        data,
        layout,
        config,
    )
    Object.entries(slider_filters).forEach(([a, b]) => filtered.add_slider_category(a, b))
    Object.entries(labels).forEach(([a, b]) => {
        if (check_box_filters.includes(a)) {
            filtered.add_checkbox_category(a, b)
        }
    })
    Object.values(boxes).forEach(y => (
        Object.values(y).forEach(x => (
            x.addEventListener('click', filtered.handle_checkbox_click.bind(filtered))
        ))
    ))
    filtered.update_plot()
}
