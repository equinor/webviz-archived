/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';
import PropTypes from 'prop-types';
import * as R from 'ramda';

import {Button, Layout} from '../lib';

class App extends Component {
    constructor() {
        super();
        this.state = {
            value: '',
        };
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        return (
            // <div>
            //     <Button setProps={this.setProps} {...this.state} />
            // </div>
            <div>
                {/* <Button eqStyle="primary" theme="default" id="primary-button">
                    Primary Button
                </Button> */}

                <Layout
                    frontPage={{
                        banner: {
                            url:
                                'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAACoCAMAAABt9SM9AAAAA1BMVEVBaeIsGYmXAAAAR0lEQVR4nO3BAQEAAACCIP+vbkhAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO8GxYgAAb0jQ/cAAAAASUVORK5CYII=',
                            color: 'red',
                            title: 'Banner baby',
                        },
                        content: <div>Front page content</div>,
                    }}
                    // subPages={[
                    //     {
                    //         id: 'page_1',
                    //         title: 'Page 1',
                    //         content: <div>Content for page 1</div>,
                    //     },
                    //     {
                    //         id: 'page_2',
                    //         title: 'Page 2',
                    //         content: <div>Content for page 2</div>,
                    //     },
                    //     {
                    //         id: 'page_3',
                    //         title: 'Page 3',
                    //         content: <div>Content for page 3</div>,
                    //     },
                    // ]}
                />
            </div>
        );
    }
}

export default App;
