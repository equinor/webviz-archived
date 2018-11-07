import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

const StyledButton = styled.button`
    :hover {
        color: var(--menuLinkHoverColor);
    }
    color: var(--menuLinkColor);
    height: 50px;
    width: 50px;
    border: none;
    background: transparent;
    outline: none;
    cursor: pointer;
`;

const MenuButton = ({onClick = () => {}}) => (
    <StyledButton onClick={onClick}>
        <svg
            width="22px"
            height="18px"
            strokeLinejoin="round"
            strokeLinecap="round"
            strokeWidth="4"
            stroke="currentColor"
            fill="None"
        >
            <path d="M2,2 L20,2 M2,9 L20,9 M2,16 L20,16" />
        </svg>
    </StyledButton>
);

MenuButton.propTypes = {
    onClick: PropTypes.func,
};

export default MenuButton;
