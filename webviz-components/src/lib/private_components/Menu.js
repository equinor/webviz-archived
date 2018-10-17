import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {Route, Link} from 'react-router-dom';
import styled, {css} from 'styled-components';
import MenuButton from './MenuButton';

const OuterWrapper = styled.div`
    background: ${({theme}) => theme.menuBackground};
    @media (min-width: 1201px) {
        min-height: fill-available;
    }
`;

const displayNone = css`
    display: none;
`;

const Wrapper = styled.div`
    background: ${({theme}) => theme.menuBackground};
    min-width: 250px;
    display: flex;
    flex-direction: column;
`;

const SubLinksWrapper = styled.div`
    display: flex;
    flex-direction: column;
    @media (max-width: 1200px) {
        ${({menuOpen}) => !menuOpen && displayNone};
    }
    @media (min-width: 1201px) {
        height: 100%;
    }
`;

const MainLinkWrapper = styled.div`
    display: flex;
    align-items: center;
`;

const LinkHome = styled(Link)`
    text-decoration: none;
    font-size: 30px;
    font-familiy: system-ui;
    @media (max-width: 1200px) {
        text-align: center;
        margin-left: -50px;
    }
`;

const LogoWrapper = styled.div`
    margin: 12px 20px 20px 18px;
    @media (max-width: 1200px) {
        height: 50px;
        margin: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
    }
    margin: 12px 20px 20px 18px;
    height: 60px;
    display: flex;
    align-items: center;
`;

const yellowBackground = css`
    background: #f59f00;
`;

const SubPageLink = styled(Link)`
    ${({selected}) => selected && yellowBackground};
    text-decoration: none;
    text-transform: uppercase;
    color: #ffffff;
    padding: 20px;
    font-size: 15px;
    font-family: system-ui;
    font-weight: 700;
    border-bottom: 1px solid white;
`;

const ButtonWrapper = styled.div`
    @media (min-width: 1201px) {
        display: none;
    }
`;

const StyledLogo = styled.img`
    @media (max-width: 1200px) {
        height: 42px;
    }
    height: 50px;
    content: url(${({theme}) => theme.logo});
`;

class Menu extends Component {
    constructor(props) {
        super(props);
        this.state = {
            menuOpen: false,
        };
    }

    render() {
        const {subPages} = this.props;
        const {menuOpen} = this.state;
        return (
            <OuterWrapper>
                <Wrapper>
                    <MainLinkWrapper>
                        <ButtonWrapper>
                            <MenuButton
                                onClick={() => {
                                    this.setState({menuOpen: !menuOpen});
                                }}
                            />
                        </ButtonWrapper>
                        <Route
                            exact
                            path="/"
                            children={() => (
                                <LogoWrapper>
                                    <LinkHome to="/">
                                        <StyledLogo />
                                    </LinkHome>
                                </LogoWrapper>
                            )}
                        />
                    </MainLinkWrapper>
                    {subPages && subPages.length ? (
                        <SubLinksWrapper menuOpen={menuOpen}>
                            {subPages.map(({title, id}) => (
                                <Route
                                    key={`subpage-${id}`}
                                    path={`/${id}`}
                                    children={({match}) => (
                                        <SubPageLink
                                            selected={match}
                                            to={`/${id}`}
                                        >
                                            {title}
                                        </SubPageLink>
                                    )}
                                />
                            ))}
                        </SubLinksWrapper>
                    ) : null}
                </Wrapper>
            </OuterWrapper>
        );
    }
}

Menu.propTypes = {
    subPages: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.string.isRequired,
            title: PropTypes.string.isRequired,
        })
    ),
};

export default Menu;
