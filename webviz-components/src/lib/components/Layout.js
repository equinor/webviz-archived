import React from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import styled, {ThemeProvider} from 'styled-components';
import PropTypes from 'prop-types';
import Menu from '../private_components/Menu';
import Banner from '../private_components/Banner';
import defaultTheme from '../resources/themes/defaultTheme';
import 'normalize.css';

const PageWrapper = styled.div`
    display: flex;
    flex-direction: column;
    width: 100%;
`;

const Wrapper = styled.div`
    display: flex;
    height: 100%;
    @media (max-width: 1200px) {
        flex-direction: column;
    }
`;

const Layout = ({theme = defaultTheme, children = [], banner}) => {
    const [frontPage, ...subPages] = Array.isArray(children)
        ? children
        : [children];
    const subPageProps = subPages.map(
        ({props}) => (props && props.children && props.children.props) || props
    );
    return (
        <BrowserRouter>
            <ThemeProvider theme={theme}>
                <Wrapper id="layout">
                    <Menu subPages={subPageProps} />
                    <Switch>
                        <Route
                            exact
                            path="/"
                            component={() => (
                                <PageWrapper>
                                    {banner && <Banner {...banner} />}
                                    {frontPage}
                                </PageWrapper>
                            )}
                        />
                        <Route
                            path="/:id"
                            component={({match}) => {
                                const page = subPages.find(
                                    ({props}) => props.id === match.params.id
                                );
                                return <PageWrapper>{page}</PageWrapper>;
                            }}
                        />
                    </Switch>
                </Wrapper>
            </ThemeProvider>
        </BrowserRouter>
    );
};

Layout.propTypes = {
    theme: PropTypes.object,
    children: PropTypes.node,
    banner: PropTypes.shape({
        url: PropTypes.string,
        color: PropTypes.string,
        title: PropTypes.string,
    }),
};

export default Layout;
