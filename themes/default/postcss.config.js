const autoprefixer = require('autoprefixer')
const color = require('postcss-color-function')

const config = {
    plugins: [
        color(),
        autoprefixer({
            browsers: [
                'last 2 versions',
                'not ie < 12',
            ],
        }),
    ],
}

module.exports = config
