.. _Open edX Platform Installation Options:

########################################
Open edX Platform Installation Options
########################################

This section describes Open edX installation options and the components that
each option includes. There are two development environment installation 
options, which install the Open edX software using Docker. If you prefer, you 
can install into an Ubuntu machine of your own using the Native installation.

.. contents::
 :local:
 :depth: 1

**********************************
Open edX Platform on Docker
**********************************

You can install the Open edX developer stack (**Devstack**) or the Open edX
analytics developer stack (**Analytics Devstack**).

* Devstack is a set of Docker containers designed for local
  development. For more information, see :ref:`Info Devstack`.

* Analytics Devstack is a modified version of the Devstack installation that
  allows you to run Open edX Analytics. For more information, see
  :ref:`Info Analytics Devstack`.

You can run Devstack or Analytics Devstack on Linux or macOS. See the
`Docker`_ downloads page for information about the operating systems and
architectures on which you can run Docker.

Devstack using `Docker for Windows`_ has not been tested and it is not
supported.

.. _Info Devstack:

=================
Open edX Devstack
=================

Devstack is a deployment of the Open edX platform within a set of Docker 
containers designed for local development. Running the Open edX platform 
locally allows you to discover and fix system configuration issues early in 
development.

Devstack simplifies certain production settings to make development more
convenient. For example, `nginx`_ and `gunicorn`_ are disabled in Devstack;
Devstack uses Django's ``runserver`` instead.

.. note::
  Because of the large number of dependencies needed to develop extensions to
  Open edX Insights, a separate development environment is available to support
  Analytics development. For more information, see :ref:`Installing and
  Starting Analytics Devstack`.

For more information about Docker, see the `Docker documentation`_.

.. _Info Analytics Devstack:

===========================
Open edX Analytics Devstack
===========================

Some users might want to develop Analytics features on their instance of the
Open edX platform. Because of the large number of dependencies needed to
develop extensions to Analytics, edX has created a separate developer stack,
known as Analytics Devstack. We strongly recommend that you install the
Analytics Devstack instead of adding Analytics extensions to an instance of
devstack.

Analytics Devstack is a modified version of the :ref:`Open edX developer
stack<Info Devstack>`. This development environment provides all of the
services and tools needed to modify the Open edX Analytics Pipeline, Data API,
and Insights projects.


*******************
Native Installation
*******************

The Native installation installs the Open edX software on your own Ubuntu 16.04
machine in a production-like configuration. Details are at the `Open edX
Native Installation`_ page on the edX wiki.


.. include:: ../../../links/links.rst
