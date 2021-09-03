.. _Discovery API Introduction:

############
Introduction
############

Discovery is a service that provides access to consolidated course and program metadata.
It does this primarily through a REST API that supports ``courses``, ``course runs``, ``programs``,
``catalogs``, and ``search``.

It also provides ``skills``, ``jobs`` and ``job postings`` data for all the published ``courses``.
the ``skills`` are extracted by text processing provided in course's full description. We
also collect and save the data about ``jobs`` that are related to ``skills`` in our system
using third party tools and services. ``JobPostings`` contains the number of job postings with
posting companies and median salary information.
