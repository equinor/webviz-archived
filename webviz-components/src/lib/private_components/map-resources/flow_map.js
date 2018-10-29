import * as d3 from 'd3';
import Map2D from './map2d';
import FlowAnimation from './flow_animation';
import {Cell} from './cell';
import Grid from './grid';
import Field from './field';
import ParticleGenerator from './particle_generator';

export default class FlowMap extends Map2D {
    constructor({canvasSelector, layers, ...rest}) {
        super(Object.assign(rest, {layers}));
        if (typeof canvasSelector === 'string') {
            this._canvas = d3
                .select(canvasSelector)
                .attr('width', this.width)
                .attr('height', this.height);

            this._canvasNode = this._canvas.node();
        }

        this._setLayer(0);
        this._flowAnimation = new FlowAnimation(
            this._canvasNode,
            0,
            1,
            this._particleGenerator,
            1500,
            this.kInit
        );
    }

    _setLayer(i) {
        const cells = [];
        const self = this;
        this.layers[i].forEach(cell => {
            cells.push(
                new Cell(
                    cell.points.map(([x, y]) => [x - self.xMin, self.yMax - y]),
                    cell.i,
                    cell.j,
                    cell['FLOWI-'],
                    cell['FLOWJ-'],
                    cell['FLOWI+'],
                    cell['FLOWJ+']
                )
            );
        });
        const grid = new Grid(cells);
        const field = new Field(grid);
        this._particleGenerator = new ParticleGenerator(field);
    }

    init() {
        super.init();

        const self = this;
        this.on('zoom', t => {
            self._flowAnimation.clear();
            self._flowAnimation.setTransform(
                t.x,
                t.y,
                t.k,
                this.kInit,
                t.angle,
                [(t.k * this.map.mapWidth) / 2, (t.k * this.map.mapHeight) / 2]
            );
        });
        this.on('rotate', t => {
            self._flowAnimation.clear();
            self._flowAnimation.setTransform(
                t.x,
                t.y,
                t.k,
                this.kInit,
                t.angle,
                [(t.k * this.map.mapWidth) / 2, (t.k * this.map.mapHeight) / 2]
            );
        });
        if (this.layerSlider) {
            this.layerSlider.on('change', value => {
                self._setLayer(value);
                self._flowAnimation.clear();
                self._flowAnimation.particleGenerator = self._particleGenerator;
            });
        }
        this._flowAnimation.setTransform(0, 0, this.kInit, this.kInit, 0, [
            0,
            0,
        ]);
        this._flowAnimation.start();
    }

    initResize() {
        super.initResize();

        const resizeCanvas = () => {
            this._canvas.attr('width', this.width);
            this._flowAnimation.clear();

            const t = this.map.mapTransform;
            this._flowAnimation.setTransform(
                t.x,
                t.y,
                t.k,
                this.kInit,
                t.angle,
                [(t.k * this.map.mapWidth) / 2, (t.k * this.map.mapHeight) / 2]
            );
        };

        window.addEventListener('resize', resizeCanvas);
    }
}
