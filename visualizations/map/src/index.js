import FlowMap from './flow_map'
import Map2D from './map2d'

const global = window || {}

global.initMap = function initMap(
    elementSelector,
    canvasSelector,
    layers,
    layerNames,
    hasFlowLayer,
) {
    const height = 800
    let map

    if (hasFlowLayer) {
        map = new FlowMap({
            canvasSelector,
            elementSelector,
            layers,
            layerNames,
            height,
        })
    } else {
        map = new Map2D({
            elementSelector,
            layers,
            layerNames,
            height,
        })
    }

    map.init()
}
