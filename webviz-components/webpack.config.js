const path = require('path');
const packagejson = require('./package.json');

const dashLibraryName = packagejson.name.replace(/-/g, '_');

module.exports = {
    entry: {main: './src/lib/index.js'},
    output: {
        path: path.resolve(__dirname, dashLibraryName),
        filename: 'bundle.js',
        library: dashLibraryName,
        libraryTarget: 'window',
    },
    externals: {
        react: 'React',
        'react-dom': 'ReactDOM',
        'plotly.js': 'Plotly',
    },
    module: {
        rules: [
            {
                test: /\.(otf|ttf|eot|svg|woff(2)?)(\?[a-z0-9=&.]+)?$/,
                loader: 'url-loader',
                // loader: 'url-loader?name=./Scripts/dist/[name].[ext]',
                options: {
                    name: './Scripts/dist/[name].[ext]',
                    outputPath: 'fonts/',
                },
            },
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'],
                    },
                },
            },
            {
                test: /\.css$/,
                use: [
                    'style-loader',
                    {loader: 'css-loader', options: {importLoaders: 1}},
                    {
                        loader: 'postcss-loader',
                        options: {
                            config: {
                                path: __dirname + '/.config',
                            },
                        },
                    },
                ],
            },
            {
                test: /\.(png|jpg|gif)$/i,
                use: [
                    {
                        loader: 'url-loader?name=./Scripts/dist/[name].[ext]',
                    },
                ],
            },
        ],
    },
    devServer: {
        historyApiFallback: true,
    },
};
