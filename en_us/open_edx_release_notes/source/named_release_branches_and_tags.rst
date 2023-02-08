########################################
Open edX Named Release Branches and Tags
########################################

The Open edX community can share knowledge and improvements more easily when most people use the same stable, consistent version of the Open edX codebase. To that end, edX creates "Open edX named releases", which are distinct from the daily deployments to edx.org and have a longer release cycle (on the order of six months between each release). These releases will be tested both by edX and by the Open edX community.

Open edX releases are named alphabetically with botanical tree names.


Latest Open edX Release
-----------------------

The latest supported release line is Olive_, based on code from 2022-10-11.

The next release will be Palm__.

__ https://openedx.atlassian.net/wiki/spaces/COMM/pages/3552938822/Palm


All Open edX Releases
---------------------

.. contents::
   :local:
   :depth: 1

Note that the latest release is the only supported release. We currently do not have the ability to support more than one release at a time.

For documentation on the latest release, please visit the :doc:`openreleasenotes:index`.

Every release line (Ginkgo, Hawthorn, etc) has a branch that accumulates changes destined for that release (``open-release/ginkgo.master``, ``open-release/hawthorn.master``, etc). Periodically, we tag that branch (``open-release/hawthorn.1``, ``open-release/hawthorn.2``, etc). After a few releases, we might still add important fixes to the branch, but not make a new tagged release. At that point, someone installing that line will want to install from the branch, not the tags.

If an installation of a tag fails, try the corresponding release line master branch, it may have a fix.

Olive
~~~~~

* **Code cut date:** 2022-10-11
* **Status:** supported
* :doc:`Release Notes <openreleasenotes:olive>`

.. list-table::
   :header-rows: 1

   * - Release Name
     - Release Date
     - Git Tag

   * - Olive.1
     - 2022-12-12
     - open-release/olive.1

Nutmeg
~~~~~~

* **Code cut date:** 2022-04-12
* **Status:** unsupported
* :doc:`Release Notes <openreleasenotes:nutmeg>`

.. list-table::
   :header-rows: 1

   * - Release Name
     - Release Date
     - Git Tag

   * - Nutmeg.1
     - 2022-06-09
     - open-release/nutmeg.1

   * - Nutmeg.2
     - 2022-08-08
     - open-release/nutmeg.2

   * - Nutmeg.3
     - 2022-10-11
     - open-release/nutmeg.3

Maple
~~~~~

* **Code cut date:** 2021-10-15
* **Status:** unsupported
* :doc:`Release Notes <openreleasenotes:maple>`

.. list-table::
   :header-rows: 1

   * - Release Name
     - Release Date
     - Git Tag

   * - Maple.1
     - 2021-12-20
     - open-release/maple.1

Lilac
~~~~~

* **Code cut date:** 2021-04-09
* **Status:** unsupported
* :doc:`Release Notes <openreleasenotes:lilac>`

.. list-table::
   :header-rows: 1

   * - Release Name
     - Release Date
     - Git Tag

   * - Lilac.2
     - 2021-08-09
     - open-release/lilac.2

   * - Lilac.1
     - 2021-06-09
     - open-release/lilac.1

Koa
~~~

* **Code cut date:** 2020-11-12
* **Status:** unsupported
* :doc:`Release Notes <openreleasenotes:koa>`

.. list-table::
   :header-rows: 1

   * - Release Name
     - Release Date
     - Git Tag

   * - Koa.3
     - 2021-04-07
     - open-release/koa.3

   * - Koa.2a
     - 2021-02-10
     - open-release/koa.2a

   * - Koa.2
     - 2021-02-09
     - open-release/koa.2

   * - Koa.1
     - 2020-12-09
     - open-release/koa.1

Juniper
~~~~~~~

* **Code cut date:** 2020-05-27
* **Status:** unsupported
* :doc:`Release Notes <openreleasenotes:juniper>`

.. list-table::
   :header-rows: 1

   * - Release Name
     - Release Date
     - Git Tag

   * - Juniper.3
     - 2020-08-25
     - open-release/juniper.3

   * - Juniper.2
     - 2020-07-13
     - open-release/juniper.2

   * - Juniper.1
     - 2020-06-09
     - open-release/juniper.1

Ironwood
~~~~~~~~

* **Code cut date:** 2019-01-17
* **Status:** unsupported
* :doc:`Release Notes <openreleasenotes:ironwood>`

.. list-table::
   :header-rows: 1

   * - Release Name
     - Release Date
     - Git Tag

   * - Ironwood fixes
     - 2019-06-26+
     - open-release/ironwood.master

   * - Ironwood.2
     - 2019-06-05
     - open-release/ironwood.2

   * - Ironwood.1
     - 2019-03-21
     - open-release/ironwood.1

Hawthorn
~~~~~~~~

* **Code cut date:** 2018-07-03
* **Status:** unsupported
* **Note:** Devstack is now based on Docker.
* :doc:`Release Notes <openreleasenotes:hawthorn>`

.. list-table::
   :header-rows: 1

   * - Release Name
     - Release Date
     - Git Tag

   * - Hawthorn.2
     - 2018-09-26
     - open-release/hawthorn.2

   * - Hawthorn.1
     - 2018-08-07
     - open-release/hawthorn.1

Ginkgo
~~~~~~

A note about Vagrant box files:

* Ginko and earlier had Vagrant box files. Hawthorn and beyond do not.
* Not every release needed new box files.
* Box files the same as the previous release are marked with an asterisk \*.
* Hashes are SHA1 hashes of the box file, not git commit hashes.


* **Code cut date:** 2017-07-06
* **Status:** unsupported
* **Latest:** open-release/ginkgo.master
* :doc:`Release Notes <openreleasenotes:ginkgo>`

.. list-table::
   :header-rows: 1

   * - Release Name
     - Release Date
     - Git Tag
     - Vagrant Box Files

   * - Ginkgo.2
     - 2017-12-18
     - open-release/ginkgo.2
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/ginkgo-devstack-2017-07-14.box?torrent>`__
          * ginkgo-devstack-2017-07-14 *
          * a7e3fce6d0155cde28e9f3253103f3f66ba3ea54
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/ginkgo-fullstack-2017-12-14.box?torrent>`__
          * ginkgo-fullstack-2017-12-14
          * c05fcd63df5fae452f0c8cb84720317449215472

   * - Ginkgo.1
     - 2017-08-14
     - open-release/ginkgo.1
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/ginkgo-devstack-2017-07-14.box?torrent>`__
          * ginkgo-devstack-2017-07-14
          * a7e3fce6d0155cde28e9f3253103f3f66ba3ea54
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/ginkgo-fullstack-2017-08-14.box?torrent>`__
          * ginkgo-fullstack-2017-08-14
          * 990d5fdb5bbc7683c158dd99d5732064932c9cdd

Ficus
~~~~~

* **Code cut date:** 2017-01-10
* **Status:** unsupported
* **Latest:** open-release/ficus.master
* :doc:`Release Notes <openreleasenotes:ficus>`

.. list-table::
   :header-rows: 1

   * - Release Name
     - Release Date
     - Git Tag
     - Vagrant Box Files

   * - Ficus.4
     - 2017-08-10
     - open-release/ficus.4
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/ficus-devstack-2017-02-07.box?torrent>`__
          * ficus-devstack-2017-02-07 *
          * a7fb2200ccdb9f847bee7acd97f5e4e1434776b3
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/ficus-fullstack-2017-08-10.box?torrent>`__
          * ficus-fullstack-2017-08-10
          * c9f59b27b39339d12fcf008f7c5721c2970a57bd

   * - Ficus.3
     - 2017-04-21
     - open-release/ficus.3
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/ficus-devstack-2017-02-07.box?torrent>`__
          * ficus-devstack-2017-02-07 *
          * a7fb2200ccdb9f847bee7acd97f5e4e1434776b3
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/ficus-fullstack-2017-04-20.box?torrent>`__
          * ficus-fullstack-2017-04-20
          * 64eb0a247d99454bccf0eed7ec49b076cbb9cd69 

   * - Ficus.2
     - 2017-03-29
     - open-release/ficus.2
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/ficus-devstack-2017-02-07.box?torrent>`__
          * ficus-devstack-2017-02-07 *
          * a7fb2200ccdb9f847bee7acd97f5e4e1434776b3
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/ficus-fullstack-2017-03-28.box?torrent>`__
          * ficus-fullstack-2017-03-28
          * fc6aa0d3b686c83e38e8c7fa1b1f172fcf7f71c1 

   * - Ficus.1
     - 2017-02-23
     - open-release/ficus.1
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/ficus-devstack-2017-02-07.box?torrent>`__
          * ficus-devstack-2017-02-07
          * a7fb2200ccdb9f847bee7acd97f5e4e1434776b3
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/ficus-fullstack-2017-02-15.box?torrent>`__
          * ficus-fullstack-2017-02-15
          * cd6310ffc1e6b374d2c3d59aab5191500f9d5d6f 

Eucalyptus
~~~~~~~~~~

* **Code cut date:** 2016-07-13
* **Status:** unsupported
* **Latest:** open-release/eucalyptus.master
* :doc:`Release Notes <openreleasenotes:eucalyptus>`

.. list-table::
   :header-rows: 1

   * - Release Name
     - Release Date
     - Git Tag
     - Vagrant Box Files

   * - Eucalyptus.3
     - 2017-01-10
     - open-release/eucalyptus.3
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/eucalyptus-devstack-2016-09-01.box?torrent>`__
          * eucalyptus-devstack-2016-09-01 *
          * a26c8fdbb431279863654161d0145732ee36ed66
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/eucalyptus-devstack-2016-09-01.box?torrent>`__
          * eucalyptus-fullstack-2017-01-10
          * 64fd2a6efd656a7170127cccdf4458699ea04978 

   * - Eucalyptus.2
     - 2016-09-02
     - open-release/eucalyptus.2
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/eucalyptus-devstack-2016-09-01.box?torrent>`__
          * eucalyptus-devstack-2016-09-01
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/eucalyptus-fullstack-2016-09-01.box?torrent>`__
          * eucalyptus-fullstack-2016-09-01

   * - Eucalyptus.1
     - 2016-08-26
     - open-release/eucalyptus.1
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/eucalyptus-devstack-2016-08-19.box?torrent>`__
          * eucalyptus-devstack-2016-08-19
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/eucalyptus-fullstack-2016-08-25.box?torrent>`__
          * eucalyptus-fullstack-2016-08-25

Dogwood
~~~~~~~

* **Code cut date:** 2015-12-15
* **Status:** unsupported
* **Latest:** named-release/dogwood.rc
* :doc:`Release Notes <openreleasenotes:dogwood>`

.. list-table::
   :header-rows: 1

   * - Release Name
     - Release Date
     - Git Tag
     - Vagrant Box Files

   * - Dogwood.3
     - 2016-04-25
     - named-release/dogwood.3
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/dogwood-devstack-2016-03-09.box?torrent>`__
          * dogwood-devstack-2016-03-09 *
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/20151221-dogwood-fullstack-rc2.box?torrent>`__
          * dogwood-fullstack-rc2 *

   * - Dogwood.2
     - 2016-04-14
     - named-release/dogwood.2
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/dogwood-devstack-2016-03-09.box?torrent>`__
          * dogwood-devstack-2016-03-09 *
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/20151221-dogwood-fullstack-rc2.box?torrent>`__
          * dogwood-fullstack-rc2 *

   * - Dogwood.1
     - 2016-03-09
     - named-release/dogwood.1
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/dogwood-devstack-2016-03-09.box?torrent>`__
          * dogwood-devstack-2016-03-09
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/20151221-dogwood-fullstack-rc2.box?torrent>`__
          * dogwood-fullstack-rc2 *

   * - Dogwood
     - 2016-02-11
     - named-release/dogwood
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/20151221-dogwood-devstack-rc2.box?torrent>`__
          * dogwood-devstack-rc2
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/20151221-dogwood-fullstack-rc2.box?torrent>`__
          * dogwood-fullstack-rc2

Cypress
~~~~~~~

* **Code cut date:** 2015-07-07
* **Status:** unsupported
* **Latest:** named-release/cypress.rc
* :doc:`Release Notes <openreleasenotes:cypress>`

.. list-table::
   :header-rows: 1

   * - Release Name
     - Release Date
     - Git Tag
     - Vagrant Box Files

   * - Cypress
     - 2015-08-13
     - named-release/cypress
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/cypress-devstack.box?torrent>`__
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/cypress-fullstack.box?torrent>`__

Birch
~~~~~

* **Code cut date:** 2015-01-29
* **Status:** unsupported
* **Latest:** named-release/birch.rc
* :doc:`Release Notes <openreleasenotes:birch>`

.. list-table::
   :header-rows: 1

   * - Release Name
     - Release Date
     - Git Tag
     - Vagrant Box Files

   * - Birch.2
     - 2015-08-05
     - named-release/birch.2
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/birch-2-devstack.box?torrent>`__
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/birch-2-devstack.box?torrent>`__

   * - Birch.1
     - 2015-07-27
     - named-release/birch.1
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/birch-1-devstack.box?torrent>`__
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/birch-1-fullstack.box?torrent>`__

   * - Birch
     - 2015-02-24
     - named-release/birch
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/20150224-birch-devstack.box?torrent>`__
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/20150224-birch-fullstack.box?torrent>`__

Aspen
~~~~~

* **Code cut date:** 2014-09-05
* **Status:** unsupported
* Release notes: Not available

.. list-table::
   :header-rows: 1

   * - Release Name
     - Release Date
     - Git Tag
     - Vagrant Box Files

   * - Aspen
     - 2014-10-28
     - named-release/aspen
     - * `devstack <https://s3.amazonaws.com/edx-static/vagrant-images/20141028-aspen-devstack-1.box?torrent>`__
       * `fullstack <https://s3.amazonaws.com/edx-static/vagrant-images/20141028-aspen-fullstack-1.box?torrent>`__


Future Releases
---------------

Upcoming releases have wiki pages for engineers to collect information that will be needed for their release on the
`Open edX Release Planning`_ page.

.. _Open edX Release Planning: https://openedx.atlassian.net/wiki/spaces/COMM/pages/13205845/Open+edX+Release+Planning

Security Updates
----------------

If security vulnerabilities or other serious problems (such as data loss) are discovered in the most recent Open edX
release, edX will release a new version of that release that includes the fix. We will not make patches of any releases
before the most recent one. We are still working on the details of how often to update Open edX releases. We will
publicly announce the security issue, and encourage the Open edX community to update their installations to close the
vulnerability. If you have found a security vulnerability in the Open edX codebase, please report it by sending an
email to security@openedx.org. Please do not post the vulnerability to the public.

Feedback
--------

If you find a problem in the release candidate, please report them to the Build-Test-Release Working Group.  You can
do so by `creating a new issue`_.

.. _creating a new issue: https://github.com/openedx/build-test-release-wg/issues/new/choose
