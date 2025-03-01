.. _Adding ECommerce to Open edX:

Adding ECommerce to Open edX
#############################

This section is intended for those are who are building Open edX ecommerce
solutions and customizing an Open edX installation to support their use.

.. contents::
   :local:
   :depth: 1

WooCommerce Plugin
*******************

There exists a WooCommerce plugin for the Open edX platform. See the following resources:

* `WooCommerce Quickstart <https://edunext-docs-openedx-woocommerce-plugin.readthedocs-hosted.com/en/latest/plugin_quickstart.html#add-the-plugin-settings>`_
* `WooCommerce plugin source <https://github.com/openedx/openedx-wordpress-ecommerce?tab=readme-ov-file#-open-edx-commerce-wordpress-plugin>`_

Open edX Webhook Receiver
*************************

The `Open edX Webhook Receiver <https://github.com/hastexo/webhook-receiver?tab=readme-ov-file#openedx-webhook-receiver>`
extension  is a small Django app that listens for incoming webhooks, and then
translates those into calls against the Open edX REST APIs.

As of Sumac it supports WooCommerce and Shopify endpoints.