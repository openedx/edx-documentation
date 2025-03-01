Apple Pay
#########

Apple Pay support is available when you use the CyberSource processor. Apple Pay
allows learners to check out quickly without having to manually fill out the
payment form. If you are not familiar with Apple Pay, take a moment to read the
following documents to understand the user flow and necessary configuration.

* `Apple Pay JS <https://developer.apple.com/documentation/applepayjs>`_
* `CyberSource Simple Order API <https://www.cybersource.com/developers/integration_methods/apple_pay/>`_

Apple Pay is available only to learners using Safari on the following platforms:

* iOS 10+ on devices with a Secure Element
* macOS 10.12+. The user must have an iPhone, Apple Watch, or a MacBook Pro with
  Touch ID that can authorize the payment.

An exhaustive list of devices that support Apple Pay is available on
`Wikipedia <https://en.wikipedia.org/wiki/Apple_Pay>`_.

.. note::

    The Apple Pay button is not displayed to users with incompatible hardware
    and software.

Settings
--------
Apple Pay is configured via the ``PAYMENT_PROCESSOR_CONFIG`` dictionary in settings. The following keys are required.

.. list-table::
    :header-rows: 1

    * - Name
      - Purpose
    * - apple_pay_merchant_identifier
      - Merchant identifier created at the `Apple Developer portal`_
    * - apple_pay_country_code
      - Two-letter `ISO 3166 country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ for your
        business/merchant account
    * - apple_pay_merchant_id_domain_association
      - Domain verification text obtained from the `Apple Developer portal`_
    * - apple_pay_merchant_id_certificate_path
      - Filesystem path to the merchant identity certificate (used to authenticate with Apple to start sessions). This
        file should be kept in a secure location that is only accessible by administrators and the application'
        service user.

.. _Apple Developer portal: https://developer.apple.com/account/ios/identifier/merchant
