import React, {Component} from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';
import FlowMap from '../private_components/map-resources/flow_map';
import Map2D from '../private_components/map-resources/map2d';

const Wrapper = styled.div`
    heigth: ${({height}) => height}px;
    margin-bottom: ${({height}) => height}px;
`;

const StyledCanvas = styled.canvas`
    pointer-events: none;
    position: absolute;
    z-index: 1;
`;

const getIndexies = layers => {
    const index = {};
    layers.forEach(kLayer => {
        kLayer.forEach(({k, i, j, ...layer}) => {
            if (!index[k]) {
                index[k] = {};
            }
            if (!index[k][i]) {
                index[k][i] = {};
            }
            if (!index[k][i][j]) {
                index[k][i][j] = {};
                index[k][i][j]['FLOWI+'] = layer['FLOWI+'];
                index[k][i][j]['FLOWJ+'] = layer['FLOWJ+'];
            }
        });
    });
    return index;
};

const addNegativeFlow = ({layers, indexies}) =>
    layers.map(kLayer =>
        kLayer.map(({i, j, k, ...layer}) => {
            let FLOWInegative = 0;
            let FLOWJnegative = 0;
            if (
                indexies[k][i - 1] &&
                indexies[k][i - 1][j] &&
                indexies[k][i - 1][j]['FLOWI+'] !== undefined
            ) {
                FLOWInegative = indexies[k][i - 1][j]['FLOWI+'];
            }
            if (
                indexies[k][i][j - 1] &&
                indexies[k][i][j - 1]['FLOWJ+'] !== undefined
            ) {
                FLOWJnegative = indexies[k][i][j - 1]['FLOWJ+'];
            }
            return {
                ...layer,
                k,
                i,
                j,
                'FLOWI-': FLOWInegative,
                'FLOWJ-': FLOWJnegative,
            };
        })
    );

const makeFlowLayers = data => {
    const {i, j, k, x0, y0, x1, y1, x2, y2, x3, y3, value} = data;
    const FLOWIplus = data['FLOWI+'];
    const FLOWJplus = data['FLOWJ+'];
    const keys = Object.keys(data.i);
    const layers = [];

    keys.forEach(key => {
        const kValue = k[key];
        if (!layers[kValue]) {
            layers[kValue] = [];
        }
        layers[kValue].push({
            i: i[key],
            j: j[key],
            k: k[key],
            points: [
                [x0[key], y0[key]],
                [x1[key], y1[key]],
                [x2[key], y2[key]],
                [x3[key], y3[key]],
            ],
            value: value[key],
            'FLOWI+': FLOWIplus[key],
            'FLOWJ+': FLOWJplus[key],
        });
    });
    const indexies = getIndexies(layers);
    return addNegativeFlow({layers, indexies});
};

const initFlowMap = ({canvasSelector, elementSelector, data, height}) => {
    const layers = makeFlowLayers(data);
    const layerNames = undefined;
    const map = new FlowMap({
        canvasSelector,
        elementSelector,
        layers: layers,
        layerNames,
        height,
    });
    map.init();
};

const make2DLayers = ({i, j, k, x0, y0, x1, y1, x2, y2, x3, y3, value}) => {
    const layers = [];
    Object.keys(i).map(key => {
        const kValue = k[key];
        if (!layers[kValue]) {
            layers[kValue] = [];
        }
        layers[kValue].push({
            i: i[key],
            j: j[key],
            k: k[key],
            points: [
                [x0[key], y0[key]],
                [x1[key], y1[key]],
                [x2[key], y2[key]],
                [x3[key], y3[key]],
            ],
            value: value[key],
        });
    });
    return layers;
};

const init2DMap = ({elementSelector, data, height}) => {
    const layers = make2DLayers(data);
    const layerNames = undefined;
    const map = new Map2D({
        elementSelector,
        layers: layers,
        layerNames,
        height,
    });
    map.init();
};

const parseData = data => (typeof data === 'string' ? JSON.parse(data) : data);

const shouldRenderFlowMap = data => Boolean(data['FLOWI+']);

class Map extends Component {
    constructor(props) {
        super(props);
        this.canvas = null;
        this.canvasId = `canvas-${props.id}`;
        this.elementId = `container-${props.id}`;
    }

    componentDidMount() {
        if (this.canvas) {
            const {data, height} = this.props;
            const parsedData = parseData(data);
            const isFlowMap = shouldRenderFlowMap(parsedData);
            const canvasSelector = `#${this.canvasId}`;
            const elementSelector = `#${this.elementId}`;
            if (isFlowMap) {
                initFlowMap({
                    canvasSelector,
                    elementSelector,
                    data: parsedData,
                    height,
                });
            } else {
                init2DMap({
                    elementSelector,
                    data: parsedData,
                    height,
                });
            }
        }
    }

    render() {
        return (
            <Wrapper height={this.props.height}>
                <div id={this.elementId}>
                    <StyledCanvas
                        id={this.canvasId}
                        innerRef={ref => {
                            this.canvas = ref;
                        }}
                    />
                </div>
            </Wrapper>
        );
    }
}

Map.defaultProps = {
    height: 800,
};

Map.propTypes = {
    id: PropTypes.string.isRequired,
    data: PropTypes.string,
    height: PropTypes.number,
    layerNames: PropTypes.arrayOf(PropTypes.string),
};

export default Map;
