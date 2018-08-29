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

.PHONY: build test
build:
	for project in $(projects); do\
	    make build -C $$project || (echo 'error building' $$project; exit 1)\
	done

lint:
	for project in $(projects); do\
	    make lint -C $$project || exit 1;\
	done

dev-install:
	make install ARGS=-e;\
	for project in $(projects); do\
	    make build -C $$project || exit 1;\
	done

test:
	for project in $(projects); do\
	    make test -C $$project || exit 1;\
	done

install:
ifdef ARGS
	for project in $(projects); do\
		make install ARGS=$(ARGS) -C $$project || exit 1;\
		make build -C $$project || exit 1;\
	done
else
	for project in $(projects); do\
		make install -C $$project || exit 1;\
	done
endif

doc:
	cd docs && make html && cd ..
