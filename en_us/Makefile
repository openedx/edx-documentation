
.PHONY: all

Q_FLAG =

ifeq ($(quiet), true)
Q_FLAG = quiet=true
endif

# Directories beneath us with Makefiles
SUBMAKES   = $(dir $(shell find . -mindepth 2 -maxdepth 2 -type f -name Makefile))

all: clean html

clean:
	@for dir in $(SUBMAKES); do \
		echo ==== $$dir; \
		make -C $$dir clean; \
	done

html:
	@echo Building and Running an edX Course
	@cd $(CURDIR)/course_authors && make html $(Q_FLAG)
	@echo Researchers Guide
	@cd $(CURDIR)/data && make html $(Q_FLAG)
	@echo Developers Guide
	@cd $(CURDIR)/developers && make html $(Q_FLAG)
	@echo Discovery API Guide
	@cd $(CURDIR)/discovery_api && make html $(Q_FLAG)
	@echo EdX Style Guide
	@cd $(CURDIR)/edx_style_guide && make html $(Q_FLAG)
	@echo Open edX Installation and Configuration Guide
	@cd $(CURDIR)/install_operations && make html $(Q_FLAG)
	@echo edX Open Learning XML Guide
	@cd $(CURDIR)/olx && make html $(Q_FLAG)
	@echo Building and Running an Open edX Course
	@cd $(CURDIR)/open_edx_course_authors && make html $(Q_FLAG)
	@echo Open edX Release Notes
	@cd $(CURDIR)/open_edx_release_notes && make html $(Q_FLAG)
	@echo edX Open edX Students
	@cd $(CURDIR)/open_edx_students && make html $(Q_FLAG)
	@echo edX Students
	@cd $(CURDIR)/students && make html $(Q_FLAG)
	@echo XBlock Tutorial
	@cd $(CURDIR)/xblock-tutorial && make html $(Q_FLAG)
