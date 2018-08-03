function plotly_checkbox_filter(
    containerDiv,
    boxes,
    filtered_data,
    layout,
    config
) {
        let keys = Object.keys(boxes);
        function updatePlot() {
            let enabled = {};
            keys.forEach(key => {
                if(!enabled[key]) enabled[key] = []
                Object.entries(boxes[key]).forEach(([label, box]) => {
                    if(box.checked){
                        enabled[key].push(label);
                    }
                })
            })
            let data = filtered_data.filter(point =>
                keys.every(key =>
                    enabled[key].find(e => e == point.labels[key])));
            Plotly.newPlot(
                containerDiv,
                data,
                layout,
                config);
        }
        Object.values(boxes).forEach(y =>
            Object.values(y).forEach(x =>
                x.addEventListener('click',updatePlot)
            )
        );
        updatePlot();
}
