function plotly_checkbox_filter(
    containerDiv,
    boxes,
    sliders,
    filtered_data,
    layout,
    config
) {
        function compare(a,b) {
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
        let slider_values = {};
        Object.entries(sliders).forEach(([slider, labels]) => {
          slider_values[slider] = 0;
        });
        Object.values(sliders).forEach(labels => labels.sort(compare));
        function updatePlot() {
            let keys = Object.keys(boxes);
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
                Object.entries(slider_values).every(([slider, value]) =>
                  point.labels[slider] == sliders[slider][value])
                &&
                keys.every(key =>
                    enabled[key].find(e => e == point.labels[key])));
            data.forEach(point =>
                {point.name = keys
                        .filter(k => enabled[k] && enabled[k].length > 1)
                        .map(key => point.labels[key])
                        .join('-');
                }
            )
            let slider_layout = Object.entries(sliders).map(([key, labels], idx) =>
              ({
                name: key,
                y: -idx*0.75,
                pad: {t: 40},
                currentvalue: {'prefix': key+': '},
                active: slider_values[key],
                steps: labels.map(label => ({
                  'label': label,
                  method: 'skip',
                  name: label,
                  value: label
                }))
              })
            );
            if(!layout) layout = {};
            if(!layout.sliders) layout.sliders = [];
            orig_sliders = layout.sliders;
            layout.sliders = layout.sliders.concat(slider_layout);
            Plotly.newPlot(
                containerDiv,
                data,
                layout,
                config);
            layout.sliders = orig_sliders;
            const myPlot = document.getElementById(containerDiv);
            myPlot.on('plotly_sliderchange', e => {
              slider_values[e.slider.name] = e.slider.active;
              updatePlot();
            });
        }

        Object.values(boxes).forEach(y =>
            Object.values(y).forEach(x =>
                x.addEventListener('click',updatePlot)
            )
        );
        updatePlot();
}
