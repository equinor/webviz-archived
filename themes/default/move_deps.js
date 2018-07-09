const fs = require('fs')

function basename(path) {
    return path.split(/[\\/]/).pop()
}

function copyFile(src, dest) {
    fs.writeFileSync(`${dest}/${basename(src)}`, fs.readFileSync(src))
}

const moveToJs = [
    'node_modules/@fortawesome/fontawesome-free/js/fontawesome.js',
    'node_modules/@fortawesome/fontawesome-free/js/solid.js',
]

moveToJs.forEach(file => {
    copyFile(file, 'src/webviz_default_theme/resources/js')
})
