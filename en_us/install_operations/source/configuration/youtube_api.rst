.. _YouTube_API:

###############################
Setting Up the YouTube API Key
###############################

This section describes how to set the YouTube API key for your instance of
Open edX.

.. contents::
   :local:
   :depth: 1

*********
Overview
*********

If you intend for courses on your Open edX instance to include videos that are
hosted on YouTube, you must get a YouTube API key and set the key in the
Open edX Platform.

The Open edX Platform uses the `YouTube Data API v3`_, which requires that
the application uses an API key.

*************************
Get a YouTube API key
*************************

To get the YouTube API key, follow YouTube's `instructions for obtaining
authorization credentials`_. YouTube provides two different options for API
keys: server keys or browser keys. You should use a **browser key** for
Open edX.

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the edX Platform`.

******************************************
Install the YouTube API key in Open edX
******************************************

After you obtain a YouTube API key, you must install that key into your
Open edX installation. There are two different ways you can do this.

Option 1: Ansible (recommended)
===============================

`Ansible`_ is the automation system used for installing and updating Open edX.
If you set your YouTube API key in Ansible's configuration file, then Ansible
will make sure that the YouTube API key remains in place when you update Open
edX.

To set your YouTube API key in Ansible's configuration file, complete the following steps.

#. Find the `configuration`_ repository on your Open edX server. If you are
   running Devstack or Fullstack, the directory is
   ``/edx/app/edx_ansible/edx_ansible``.

#. In that repository, open the ``playbooks/roles/edxapp/defaults/main.yml``
   file in a text editor.

#. Find the line for the YouTube API key.

   ``EDXAPP_YOUTUBE_API_KEY: "PUT_YOUR_API_KEY_HERE"``

   Replace ``PUT_YOUR_API_KEY_HERE`` with your YouTube API key. Ensure
   that the YouTube API key is within by quotation marks.

#. Save and close the file.

#. Run Ansible so that it applies your YouTube API key to your Open edX
   installation. If you are running the Open edX Cypress release, run the
   following command.

   .. code-block:: bash

      /edx/bin/update edx-platform named-release/cypress


Option 2: JSON files
====================

Ansible outputs information to several JSON files used by Open edX. If you
prefer not to edit the Ansible configuration, you can edit these files
directly.

However, every time you update Open edX, your edits will be overwritten by
Ansible. As a result, we recommend setting your YouTube API key in Ansible's
configuration instead.

To set your YouTube API key by editing JSON files, complete the following
steps.

#. Find the `edx-platform`_ repository on your Open edX server. If you are
   running Devstack or Fullstack, the directory is ``/edx/app/edxapp/edx-
   platform``.

#. In the directory *above* your repository, there should be several JSON
   files, including ``lms.auth.json`` and ``cms.auth.json``. If you are running
   Devstack or Fullstack, the directory is ``/edx/app/edxapp``.

#. Open the ``lms.auth.json`` file in your text editor.

#. Find the line for the YouTube API key.
   ``"YOUTUBE_API_KEY": "PUT_YOUR_API_KEY_HERE",``

   Replace ``PUT_YOUR_API_KEY_HERE`` with your YouTube API key. Ensure
   that the YouTube API key is within by quotation marks.

#. Save and close the file.

#. Open the ``cms.auth.json`` file and make the same change. If that line does
   not exist in this file, create it.

#. Save and close the file.

.. include:: ../../../links/links.rst
