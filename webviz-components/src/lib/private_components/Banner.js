import React from 'react';
import styled, {css} from 'styled-components';
import PropTypes from 'prop-types';

const backgroundImage = url => css`
    background-image: url(${url});
`;

const backgroundColor = color => css`
    background-color: ${color};
`;

const Wrapper = styled.div`
    ${({url}) => url && backgroundImage(url)};
    ${({color}) => color && backgroundColor(color)};
    height: 92px;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
`;

const StyledParagraph = styled.p`
    color: #ffffff;
    font-size: 48px;
    font-family: system-ui;
    font-weight: 700;
`;

const Banner = ({url, color, title}) => (
    <Wrapper url={url} color={color} role="banner">
        <StyledParagraph>{title}</StyledParagraph>
    </Wrapper>
);

Banner.propTypes = {
    url: PropTypes.string,
    color: PropTypes.string,
    title: PropTypes.string,
};

export default Banner;
