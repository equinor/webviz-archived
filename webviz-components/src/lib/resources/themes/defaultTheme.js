import defaultLogo from '../images/logo.svg';
import './theme.css';

let defaultTheme = {};

try {
    require('frontend-assets-internal/theme.css');
    const logo = require('frontend-assets-internal/logo.png');
    defaultTheme = {menuLogo: logo};
} catch (e) {
    defaultTheme = {menuLogo: defaultLogo};
}

export default defaultTheme;
