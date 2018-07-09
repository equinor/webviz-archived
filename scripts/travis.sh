set -e

declare -a projects=('.' 'themes/default/')

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
