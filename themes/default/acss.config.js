const oc = require('open-color')

const flatten = (name, arr) => arr.reduce((prev, curr, index) => ({
    ...prev,
    [`${name}-${index}`]: curr,
}), {})

const buildColorList = colors => Object.keys(colors).reduce((list, color) => ({
    ...list,
    ...(Array.isArray(oc[color]) ? flatten(color, oc[color]) : { [color]: oc[color] }),
}), {})


const colorPalette = buildColorList(oc)

/*
 * Building all the colors is useful for designing in the browser, but leads to bloated css.
 * Make sure to comment out these lines in production
 */

const colorClassnames = Object.keys(colorPalette).reduce((prev, curr) => [
    ...prev,
    ...[
        `C(${curr})`,
        `Bgc(${curr})`,
        `Bdc(${curr})`,
        `Fill(${curr})`,
    ],
], [])

/*
 * Common breakpoints. The design is made with mobile first in mind.
 * Each breakpoint overrides the previous one - with xs overriding the default value
 */

const breakPoints = {
    xs: '@media (min-width: 576px)',
    sm: '@media (min-width: 768px)',
    md: '@media (min-width: 992px)',
    lg: '@media (min-width: 1200px)',
    xl: '@media (min-width: 1600px)',
}

const deFonts = [
    'system-ui',
    '-apple-system',
    'BlinkMacSystemFont',
    '"Segoe UI"',
    'Roboto',
    'Oxygen-Sans',
    'Ubuntu',
    'Cantarell',
    '"Helvetica Neue"',
    'sans-serif',
].join(',')


/*
 * Custom fonts as specified in fonts.css
 */

const fonts = {
    de: deFonts,
    di: '"League Gothic"',
}

/*
 * Responsive font-size classes
 */

const rwd = {
    'Fz(default)': {
        default: '18px',
        md: '20px',
    },
    'Fz(h1)': {
        default: '32px',
        sm: '40px',
        md: '48px',
    },
    'Fz(h2)': {
        default: '28px',
        sm: '32px',
        md: '40px',
    },
    'Fz(h3)': {
        default: '20px',
        sm: '25px',
        md: '25px',
    },
    'Fz(h4)': {
        default: '16px',
        sm: '18px',
        md: '20px',
    },
}

/*
 * These classes are always generated even though they might not be used on a given page
 */

const classNames = [
    'Ff(de)',
    'Ff(di)',
    'D(n)',
    ...colorClassnames,
]


/*
 * These classes are just hard or impossible to do with acss
 */

const misc = {
    bannerTextShadow: '0.025em 0.025em 0 black',
}

module.exports = {
    breakPoints,
    custom: {
        ...colorPalette,
        ...fonts,
        ...misc,
        ...rwd,
    },
    classNames,
}
