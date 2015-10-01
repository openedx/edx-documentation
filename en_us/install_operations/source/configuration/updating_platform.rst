.. _Guidelines for Updating the edX Platform:

######################################################
Guidelines for Updating the edX Platform
######################################################

When you update the edX Platform, you should not change configuration files on
a running server. Doing so can result in unpredictable problems.

If you need to change settings on a running server, take the following steps.

#. Provision a new server that matches the running server.
#. Make configuration changes on the new server.
#. Start the new server.
#. Reroute traffic from the old server to the new server.
#. Decommission the old server.

.. include:: ../../../links/links.rst
