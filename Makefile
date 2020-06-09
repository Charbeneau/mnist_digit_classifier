.PHONY: python-package help
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([0-9a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

args = `arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:-${1}}`

%:
    @:

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

docker-clean-unused: ## docker system prune --all --force --volumes
	docker system prune --all --force --volumes

docker-clean-all:  ## docker container stop $$(docker container ls --all --quiet) && docker system prune --all --force --volumes
	docker container stop $$(docker container ls --all --quiet) && docker system prune --all --force --volumes

build_model: ## Build the model container.
	docker build --file model/Dockerfile --tag model model/

fit_model: ## Run fit.py in the model container, and save the model to /model/mnist_model.
	docker run model python /workspace/fit.py && docker cp $$(docker ps -alq):/workspace/mnist_model ./server/mnist_model

build_server: ## Build the server container.
	docker build --file server/Dockerfile --tag server server/

run_server:  ## Run the server.
	docker run --publish 5000:5000 server

run: build_model fit_model build_server run_server ## Build the model container, and fit the model; build the server container, and run the server.
