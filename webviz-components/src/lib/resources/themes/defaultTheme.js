import defaultLogo from '../images/logo.svg';
let defaultTheme = {};
import 'frontend-assets-internal/bull.css';

try {
    require('frontend-assets-internal/font.css');
    const logo = require('frontend-assets-internal/logo.png');

    defaultTheme = {
        menuLinkFont: 'Equinor',
        menuLogo: logo,
        menuLogoHeight: 75,
        menuBackground: '#ffffff',
        menuLinkBackgroundHover: '#E2E5E7',
        menuLinkBackgroundSelected: '#EB0036',
        menuLinkColor: '#66737e',
        menuLinkColorSelected: '#ffffff',
        menuLinkFontStyle: 'normal',
        menuLinkFontWeight: 500,
        menuLinkHoverColor: '#243746',
    };
} catch (e) {
    defaultTheme = {
        menuLinkFont: 'system-ui',
        menuLogo: defaultLogo,
        menuLogoHeight: 50,
        menuBackground: '#adb5bd',
        menuLinkBackgroundHover: '#adb5bd',
        menuLinkBackgroundSelected: '#F59F00',
        menuLinkColor: '#ffffff',
        menuLinkColorSelected: '#ffffff',
        menuLinkFontStyle: 'normal',
        menuLinkFontWeight: 700,
        menuLinkHoverColor: '#ffffff',
        menuLinkUppercase: true,
    };
}

export default defaultTheme;
