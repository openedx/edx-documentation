# Do things in edx-documentation
.PHONY: release-note requirements upgrade

help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

release-note:
	./utilities/add-upcoming-release-notes-file.sh

requirements: ## install development environment requirements
	pip install -r requirements/dev.txt

upgrade: requirements ## update the pip requirements files to use the latest releases satisfying our constraints
	# Make sure to compile files after any other files they include!
	pip-compile --upgrade -o requirements/base.txt requirements/base.in
	pip-compile --upgrade -o requirements/dev.txt requirements/dev.in
	# Post process all of the files generated above to replace the instructions for recreating them
	sed 's/pip-compile .*/make upgrade/' requirements/base.txt > requirements/base.tmp
	mv requirements/base.tmp requirements/base.txt
	sed 's/pip-compile .*/make upgrade/' requirements/dev.txt > requirements/dev.tmp
	mv requirements/dev.tmp requirements/dev.txt
