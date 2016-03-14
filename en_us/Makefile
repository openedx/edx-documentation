
.PHONY: all

Q_FLAG =

ifeq ($(quiet), true)
Q_FLAG = quiet=true
endif


all: clean html

clean:
	@cd $(CURDIR)/course_authors && make clean $(Q_FLAG)
	@cd $(CURDIR)/data && make clean $(Q_FLAG)
	@cd $(CURDIR)/developers && make clean $(Q_FLAG)
	@cd $(CURDIR)/edx_style_guide && make clean $(Q_FLAG)
	@cd $(CURDIR)/install_operations && make clean $(Q_FLAG)
	@cd $(CURDIR)/olx && make clean $(Q_FLAG)
	@cd $(CURDIR)/open_edx_course_authors && make clean $(Q_FLAG)
	@cd $(CURDIR)/open_edx_release_notes && make clean $(Q_FLAG)
	@cd $(CURDIR)/open_edx_students && make clean $(Q_FLAG)
	@cd $(CURDIR)/release_notes && make clean $(Q_FLAG)
	@cd $(CURDIR)/students && make clean $(Q_FLAG)
	@cd $(CURDIR)/xblock-tutorial && make clean $(Q_FLAG)
	@cd $(CURDIR)/release_notes_2014 && make clean $(Q_FLAG)
	$(MAKE html)


html:
	@cd $(CURDIR)/course_authors && make clean $(Q_FLAG)
	@cd $(CURDIR)/data && make clean $(Q_FLAG)
	@cd $(CURDIR)/developers && make clean $(Q_FLAG)
	@cd $(CURDIR)/edx_style_guide && make clean $(Q_FLAG)
	@cd $(CURDIR)/install_operations && make clean $(Q_FLAG)
	@cd $(CURDIR)/olx && make clean $(Q_FLAG)
	@cd $(CURDIR)/open_edx_course_authors && make clean $(Q_FLAG)
	@cd $(CURDIR)/open_edx_release_notes && make clean $(Q_FLAG)
	@cd $(CURDIR)/open_edx_students && make clean $(Q_FLAG)
	@cd $(CURDIR)/release_notes && make clean $(Q_FLAG)
	@cd $(CURDIR)/release_notes_2014 && make clean $(Q_FLAG)
	@cd $(CURDIR)/students && make clean $(Q_FLAG)
	@cd $(CURDIR)/xblock-tutorial && make clean $(Q_FLAG)
	@echo Building and Running an edX Course
	@cd $(CURDIR)/course_authors && make html $(Q_FLAG)
	@echo Researchers Guide
	@cd $(CURDIR)/data && make html $(Q_FLAG)
	@echo Developers Guide
	@cd $(CURDIR)/developers && make html $(Q_FLAG)
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
	@echo edX Release notes
	@cd $(CURDIR)/release_notes && make html $(Q_FLAG)
	@echo edX 2014 Release notes
	@cd $(CURDIR)/release_notes_2014 && make html $(Q_FLAG)
	@echo edX Students
	@cd $(CURDIR)/students && make html $(Q_FLAG)
	@echo XBlock Tutorial
	@cd $(CURDIR)/xblock-tutorial && make html $(Q_FLAG)
