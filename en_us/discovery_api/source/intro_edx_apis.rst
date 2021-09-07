.. _Discovery API Introduction:

############
Introduction
############

Discovery is a service that provides access to consolidated course and program metadata.
It does this primarily through a REST API that supports ``courses``, ``course runs``, ``programs``,
``catalogs``, and ``search``.

It also provides ``skills``, ``jobs`` and ``job postings`` data for all the published ``courses``.
The ``skills`` are extracted using course's full description by third party tools and services. We
also collect and save the data about ``jobs`` that is relevant to the ``skills`` in our system.
``JobPostings`` contains the number of job postings with posting companies and median salary information.
