const fs = require('fs')

function basename(path) {
    return path.split(/[\\/]/).pop()
}

function copyFile(src, dest) {
    fs.writeFileSync(`${dest}/${basename(src)}`, fs.readFileSync(src))
}

const moveToJs = [
    'node_modules/plotly.js-dist/plotly.js',
]

moveToJs.forEach(file => {
    copyFile(file, 'webviz_plotly/resources/js')
})
