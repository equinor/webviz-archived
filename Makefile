projects = \
	core/\
	themes/default/\
	visualizations/plotly\
	visualizations/line_chart\
	visualizations/bar_chart\
	visualizations/pie_chart\
	visualizations/tornado_plot\
	visualizations/fan_chart\
	visualizations/scatter_plot_matrix\


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
        make build -C $$project || exit 1;\
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
