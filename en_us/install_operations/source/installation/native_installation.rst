.. _Lilac/Koa Native Open edX platform Installation:

###################################################################
Lilac/Koa Native Open edX platform Installation
###################################################################

This page describes how to install the Open edX Koa release on a single Ubuntu 20.04 64-bit server from scratch.
For Juniper and earlier, see `Legacy Open edX Native Installation`_ .

.. warning:: Installing and running an Open edX instance is not simple.  We **strongly recommend** that you use a `service provider <https://open.edx.org/get-started/>`_ to run the software for you.  They have free trials that make it easy to get started: https://open.edx.org/get-started/

    Only proceed with these installation steps if you are comfortable with installing and diagnosing complex Linux systems.

*******************
Server Requirements
*******************
The following server requirements will be fine for supporting hundreds of registered students on a single server.

*Note: This will run MySQL, Memcache, Mongo, nginx, and all of the Open edX services (LMS, Studio, Forums, ORA, etc) on a single server. In production configurations we recommend that these services run on different servers and that a load balancer be used for redundancy. Setting up production configurations is beyond the scope of this wiki page.*

* **Ubuntu 20.04 amd64** (oraclejdk required). It may seem like other versions of Ubuntu will be fine, but they are not.
* **Minimum 8GB of memory**
* **At least one 2.00GHz CPU or EC2 compute unit**
* **Minimum 25GB of free disk, 50GB recommended for production servers**

For hosting in Amazon we recommend an t2.large with at least a 50Gb EBS volume, see https://aws.amazon.com/ec2/pricing. Community Ubuntu AMIs have 8GB on the root directory, make sure to expand it before installing.

*************************
Installation instructions
*************************

.. warning::
    * These instructions will potentially **destroy the server** they are run on, you should only do them on a freshly installed virtual machine. But if you still want to have a try to re-install the Open edX stack on the same server, please see `Re install Open edX in Ubuntu 12.04`_ for some issues you may face and how to fix them.
    * **By default ssh will only allow key based authentication**. Please setup key based SSH logins or modify the configuration repo to allow for password based SSH logins before running Ansible.

.. note::
    * If you are running your services behind a proxy, please see `EdX Proxy Instructions`_

===============
Prep the server
===============
Launch your Ubuntu 20.04 64-bit server and log in to it as a user that has full sudo privileges.

Update your Ubuntu package sources:

.. code-block:: shell

    $ sudo apt-get update -y
    $ sudo apt-get upgrade -y
    $ sudo reboot

==============
Installation
==============
You will run a few scripts to accomplish the installation. Please read the contents of the scripts before running this to ensure you are aware of everything they will do: they are quite extensive. The scripts require that the running user can run commands as root via sudo.

#. **Set** the OPENEDX_RELEASE variable. You choose the version of software by setting the OPENEDX_RELEASE variable before running the commands. See the `Open edX Named Releases page`_ for the tags you can use.

    .. code-block:: shell

        $ export OPENEDX_RELEASE=the-tag/you-want-to-install

#. **Create** a config.yml file.  This file specifies the hostname (and port, if needed) of the LMS and Studio.   Create a file in the current directory named **config.yml**, like this:

    .. code-block:: yaml

        # The host names of LMS and Studio. Don't include the "https://" part:
        EDXAPP_LMS_BASE: "online.myeducation.org"
        EDXAPP_CMS_BASE: "studio.online.myeducation.org"

    Your LMS host and Studio host must either be the same hostname (on different ports), or Studio must be a subdomain of the LMS.  If you need a different configuration, you may need to also set EDXAPP_SESSION_COOKIE_DOMAIN.

    **NOTE** : Open edX and edX are registered trademarks.  You **may not** use "openedx." or "edx." as subdomains when naming your site. For more details, see the `edX Trademark Policy`_.  Here are some examples of **unacceptable domain names**:

        * **DON'T:** openedx.yourdomain.org
        * **DON'T:** edx.yourdomain.org
        * **DON'T:** openedxyourdomain.org
        * **DON'T:** yourdomain-edx.com

#. **Bootstrap** the Ansible installation:

    .. code-block:: shell

        $ wget https://raw.githubusercontent.com/edx/configuration/$OPENEDX_RELEASE/util/install/ansible-bootstrap.sh -O - | sudo -E bash

    .. warning:: DO NOT activate a virtualenv at this point, even if the ansible-bootstrap script tells you to.

#. **Randomize** passwords. If this is to replace an older installation, copy your my-passwords.yml file from that installation.  If this is a new installation:

    .. code-block:: shell

        $ wget https://raw.githubusercontent.com/edx/configuration/$OPENEDX_RELEASE/util/install/generate-passwords.sh -O - | bash

    **IMPORTANT**: Be sure to save the generated my-passwords.yml in a safe place. If you ever need to access your services directly, you'll need these credentials. More details of password generation and other security measures are here: `How to Override Default Configuration Passwords and Verify Exposed Services`_.

#. **Install** the Open edX software.  This can take some time, perhaps an hour. (Note: for Ginkgo and earlier, this file was called sandbox.sh):

    .. code-block:: shell

        $ wget https://raw.githubusercontent.com/edx/configuration/$OPENEDX_RELEASE/util/install/native.sh -O - | bash

#. **Finish** configuring your server, for example to set the LMS_ROOT_URL setting, before everything will work properly. The `Managing Open edX Tips and Tricks`_ page may be useful.


************************************
Do not upgrade!
************************************
Some Open edX components are outdated. If you see a message suggesting that you update something manually, **don't do it** -- something is probably relying on the outdated software remaining at that older version. Specifically:

* Ubuntu may alert you that a newer version of Ubuntu available when you SSH in to your server, and may suggest that you run :code:`do-release-upgrade` to upgrade to that newer version. **Don't do it.**
* Pip may alert you that there is a newer version of pip available, and may suggest that you run :code:`pip install --upgrade pip` to install it. **Don't do it.**

If you arbitrarily upgrade parts of Open edX software, *things will break*. Instead, you should submit a pull request to change the line in the Open edX project where that specific version of the software is defined. All pull requests need to be reviewed before they can be merged, and part of the review process will consist of testing the full platform with the updated software, identifying any breakages, and fixing them as part of the pull request.

.. include:: ../../../links/links.rst
