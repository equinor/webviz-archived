const fs = require('fs')

function basename(path) {
    return path.split(/[\\/]/).pop()
}

function copyFile(src, dest) {
    fs.writeFileSync(`${dest}/${basename(src)}`, fs.readFileSync(src))
}

const moveToJs = [
    'node_modules/d3-selection/dist/d3-selection.min.js',
    'image_viewer.js',
]
const moveToCss = [
    'node_modules/bootstrap-css-only/css/bootstrap.min.css',
]
moveToJs.forEach(file => {
    copyFile(file, 'webviz_image_viewer/resources/js')
})

moveToCss.forEach(file => {
	copyFile(file, 'webviz_image_viewer/resources/css')
})