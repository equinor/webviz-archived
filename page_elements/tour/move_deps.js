const fs = require('fs')

function basename(path) {
    return path.split(/[\\/]/).pop()
}

function copyFile(src, dest) {
    fs.writeFileSync(`${dest}/${basename(src)}`, fs.readFileSync(src))
}

const moveToJs = [
    'node_modules/hopscotch/dist/js/hopscotch.js',
]

const moveToCss = [
    'node_modules/hopscotch/dist/css/hopscotch.css',
]

const moveToImg = [
    'node_modules/hopscotch/dist/img/sprite-green.png',
    'node_modules/hopscotch/dist/img/sprite-orange.png',
]

moveToJs.forEach(file => {
    copyFile(file, 'webviz_tour/resources/js')
})

moveToCss.forEach(file => {
    copyFile(file, 'webviz_tour/resources/css')
})

moveToImg.forEach(file => {
    copyFile(file, 'webviz_tour/resources/img')
})
