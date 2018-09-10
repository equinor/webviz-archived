import PlotlyFilters from './plotly_filters'

function makeFilterCheckboxes(containerId, labels, filters) {
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

global.makeFilteredPlotly = function makeFilteredPlotly(
    containerId,
    data,
    layout,
    config,
    labels,
    sliderFilters,
    dropdownFilters,
    checkBoxFilters,
) {
    const boxes = makeFilterCheckboxes(
        containerId,
        labels,
        checkBoxFilters,
    )
    const filtered = new PlotlyFilters(
        containerId,
        data,
        layout,
        config,
    )
    Object.entries(sliderFilters).forEach(
        ([a, b]) => filtered.addSliderCategory(a, b),
    )
    Object.entries(dropdownFilters).forEach(
        ([a, b]) => filtered.addDropdownCategory(a, b),
    )
    Object.entries(labels).forEach(([a, b]) => {
        if (checkBoxFilters.includes(a)) {
            filtered.addCheckboxCategory(a, b)
        }
    })
    Object.values(boxes).forEach(y => (
        Object.values(y).forEach(x => (
            x.addEventListener('click', filtered.handleCheckboxClick.bind(filtered))
        ))
    ))
    filtered.updatePlot()
}
