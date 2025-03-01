.. _Changing Payment Processors:

#############################
Changing Payment Processors
#############################


Payment processors sometimes experience temporary outages. When these outages
occur, you can use Waffle switches to disable the faulty payment processor or
processors, then re-enable them after the outage is over.

The names of these switches use prefixes that are the value of the
``PAYMENT_PROCESSOR_SWITCH_PREFIX`` setting. By default, this value is
``payment_processor_active_``. The following table lists valid switches and the
payment processors they control.

.. list-table::
   :widths: 15 45 10
   :header-rows: 1

   * - Payment Processor
     - Switch Name
     - Default Value
   * - PayPal
     - payment_processor_active_paypal
     - True
   * - CyberSource
     - payment_processor_active_cybersource
     - True

In the unlikely event that all payment processors are disabled, the LMS will
display an informative error message explaining why payment is not currently
possible.
