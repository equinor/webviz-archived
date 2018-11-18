const path = require("path");
const webpack = require("webpack");

module.exports =  {
  entry: ["./src/index.js"],
  output: {
    path: path.resolve(__dirname, "./build/"),
    filename : "webviz_plotly.js",
    library: "webviz_plotly"
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        loader: 'ify-loader'
      }
    ]
  },
  resolve: {
    modules: [
        path.resolve(__dirname, "src/"),
        path.resolve(__dirname, "node_modules")
    ]
  }
};

      
