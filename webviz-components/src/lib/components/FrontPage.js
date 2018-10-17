import React from 'react';
import PropTypes from 'prop-types';
import Page from './Page';

const FrontPage = ({children}) => (
    <Page id="frontpage" title="Frontpage">
        {children}
    </Page>
);

FrontPage.propTypes = {
    children: PropTypes.node,
};

export default FrontPage;
