set -e

declare -a projects=(\
    '.'\
    'themes/default/'\
    'visualisations/plotly'\
    'visualisations/line_chart'\
    'visualisations/bar_chart'\
    'visualisations/pie_chart'\
    'visualisations/tornado_plot'\
)

for project in "${projects[@]}"
do
    pushd $project
    make build
    make lint
    make dev-install
    make test
    make doc
    make install
    popd
done
