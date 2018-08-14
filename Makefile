projects = \
	core/\
    themes/default/\
    visualisations/plotly\
    visualisations/line_chart\
    visualisations/bar_chart\
    visualisations/pie_chart\
    visualisations/tornado_plot\
	visualisations/fan_chart\


build:
	for project in $(projects); do\
	    make build -C $$project || exit 1;\
	done

lint:
	for project in $(projects); do\
	    make lint -C $$project || exit 1;\
	done

dev-install:
	for project in $(projects); do\
	    make dev-install -C $$project || exit 1;\
	done

test:
	for project in $(projects); do\
	    make test -C $$project || exit 1;\
	done

install:
	for project in $(projects); do\
	    make install -C $$project || exit 1;\
	done


doc:
	cd docs && make html && cd ..
