.. _Safe Templates:

###############################################
Preventing Cross Site Scripting Vulnerabilities
###############################################

Cross Site Scripting (XSS) vulnerabilities allow user-supplied data to be
incorrectly executed as code in a web browser. It can be difficult to write
templates that are safe from XSS security vulnerabilities. This section
presents best practices for handling proper escaping in the Open edX platform
to avoid these vulnerabilities.

.. note:: If you become aware of security issues, do not report them in
   public. Instead, please email security@edx.org.

.. contents::
   :depth: 1
   :local:


Philosophy and General Rules
****************************

The philosophy behind the recommendations in this section is to make things as
simple as possible for developers. Protecting against XSS vulnerabilities
typically requires properly escaping user-provided data before it is placed on
the page. Rather than trying to determine if data is user-provided and could
be compromised, we will play it safe and escape data whether it is user-provided
or not. Unfortunately, because there are many different rules for escaping, you
still must choose the proper type of escaping.

Here are some general rules.

#. **Escape always.** Assume that all data is untrusted and escape it
   appropriately. Do not try to determine whether data could or could not be
   manipulated by a user.

#. **Escape late.** Delay escaping as long as possible, until you can see the
   actual context and understand the proper escaping that is required for
   the context. Browsers interpret different contexts such as HTML, URLs,
   CSS, and Javascript/JSON with different rules, so there are different
   escaping requirements based on where the data is being used in a page.

#. **Escape appropriately.** Know what kind of data you have (HTML, plain text,
   JSON, etc.) and where it is going (HTML, JavaScript, etc.). Choose the
   proper escaping function based on these details.

#. **Validation is not sufficient.** Validating inputs does not replace the
   need to properly escape. In some cases, this may reduce the likelihood of
   potential problems, but proper escaping is always necessary.

#. **Do not store escaped data.** Again, because you do not know ahead of time
   all the places that the data will be used, you must wait until you have
   the proper context to decide on the proper escaping.


Types of Context and Escaping
*****************************

.. contents::
   :depth: 1
   :local:

Overview of Contexts
====================

The following diagram provides a high-level overview of the relationship
between the different templates, different contexts of DOM creation and
manipulation, and different types of escaping. As a general rule, proper
escaping is related to the context in which the data is being written, and
might not match the context that will eventually be reading the data.

.. image:: ../images/safe-templates.png
    :width: 666px
    :height: 289px
    :align: center
    :alt: A diagram detailing how data flows from Django applications and Django
     models through Mako templates and Django templates into an HTML page. Data can
     then flow from the HTML page into JavaScript, and back down into the DOM
     through jQuery or Underscore.js templates.

In the Open edX platform, data flows from the application to the initial HTML page
mainly through the use of Mako templates.

.. Make sure the numbers in the list below are in sync with the numbered arrows in
.. the safe-templates.png diagram above, if either the diagram or the list is modified.

Descriptions of each numbered arrow in the diagram follow.

#. This step represents the use of Mako templates to write general HTML tags
   (that is, tags other than ``<script>`` tags) to create the HTML page. Any
   data written to the page inside one of these HTML tags or HTML attributes
   must be HTML-escaped to be treated as plain text.

#. This step represents the use of Mako templates to write JavaScript inside
   a ``<script>`` tag in the HTML page. Data written to this context must all
   be JavaScript-escaped to keep it from mistakenly being treated as HTML.
   Note that this data should not be HTML-escaped, which must happen in a
   later step if it is written back to the DOM by JavaScript.

#. This step represents the loading and executing of JavaScript from the HTML
   page by the JavaScript engine. This step should be safe, if data was
   properly JavaScript-escaped earlier.

#. In this step, JavaScript might load additional data from HTML tags and
   attributes using the DOM. Sometimes data is passed in this way via data
   attributes. This data is typically read using jQuery functions, but it can
   be read using other JavaScript functions. The data can be in the form of
   plain text strings or JSON. If it is in the form of strings, this data
   should mostly be plain text. Be careful with the escaping in this case.
   Although the data is used in JavaScript, it is transmitted as HTML, and so
   must be HTML-escaped.

#. In this step, JavaScript is being used to edit the DOM, often by creating
   HTML tags or setting HTML attributes. Often this is done using jQuery
   functions. Since HTML tags and attributes are being written here, any plain
   text must be properly HTML-escaped.

#. This step represents a subset of DOM manipulation using JavaScript,
   specifically through use of Underscore.js templates. Although these
   templates have a specific syntax for escaping, because HTML tags and
   attributes are being written any plain text must be properly HTML-escaped.


HTML Context and Escaping
=========================

The outtermost context of an HTML file is HTML. In an HTML context inside an
HTML file, data is kept safe by HTML-escaping.

How HTML-Escaping Makes HTML Safe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. highlight:: mako

Let's review a simple example of an XSS attack and how proper escaping might
prevent such an attack. Imagine that we find the following expression in a
Mako template.

.. code-block:: mako

    <div>${course_name}</div>

Imagine further that someone uses Studio to set the course name as shown in
this example, including the HTML ``<script>`` tag.

.. code-block:: mako

    <script>alert('XSS attack!');</script>

The following resulting unsafe page source is sent to the browser.

.. code-block:: mako

    <div><script>alert('XSS attack!');</script></div>

The browser would execute the JavaScript code in the ``<script>alert('XSS
attack!');</script>`` tag. The user has injected code into the page that would
display a pop-up alert, which we would not want to allow. Because this attack
could contain arbitrary JavaScript that would be executed by the browser with
the same trust as any JavaScript that is sent from the application, it has the
potential to do something much more malicious than simply displaying a pop-up.
An example might be to steal and email the user's cookies.

In Mako, you can introduce HTML-escaping for all expressions on a page using
the page directive with the ``h`` filter. Here is an example of an expression
that is properly HTML-escaped.

.. code-block:: mako

    <%page expression_filter="h"/>
    ...
    <div>${course_name}</div>

The resulting safe page source is as follows.

.. code-block:: mako

    <div>&lt;script&gt;alert(&#39;XSS!&#39;);&lt;/script&gt;</div>

This time, the browser will not interpret the ``<script>`` tag as a JavaScript
context, and instead simply displays the original string in the page.


JavaScript Context and Escaping
===============================

The outtermost context of a JavaScript file is JavaScript. An HTML file also
contains a JavaScript context inside any `<script>` tag. Inside a JavaScript
context, data is kept safe by JavaScript-escaping.

How JavaScript-Escaping Makes HTML Safe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is an example of an expression used in a valid JavaScript context created
using a ``<script>`` tag inside a Mako template.

.. code-block:: mako

    <script type="text/javascript">
       var courseName = "${course_name}";
       ...
    </script>

For this example, imagine that someone uses Studio to set the course name as
shown here.

.. code-block:: mako

    ";alert('XSS attack!');"

The resulting unsafe page source, sent to the browser with no escaping, would look
like this.

.. code-block:: mako

    <script type="text/javascript">
       var courseName = "";alert('XSS attack!');"";
       ...
    </script>

You can see how the attacker closed out the string and again tricked the browser
into executing the malicious JavaScript in the context of JavaScript. There
are several reasons why you do not want to use the default HTML-escaping here.

#. JavaScript-escaping will also escape all characters that are special
   characters in HTML, such as ``<``. However, JavaScript-escaping will
   escape ``<`` to ``\u003C``, rather than to ``&lt;``. This will still keep
   the browser from finding an HTML tag where it does not belong.

#. The resulting string might not ultimately be used in an HTML context, so
   HTML entities might not be the proper escaping.

The way to properly JavaScript-escape code in Mako is shown in the following
example.

.. code-block:: mako

    <%! from openedx.core.djangolib.js_utils import js_escaped_string %>
    ...
    <script type="text/javascript">
       var courseName = "${course_name | n, js_escaped_string}";
       ...
    </script>

The code above would produce the following safe page source.

.. code-block:: mako

    <script type="text/javascript">
       var courseName = "\u0022\u003Balert(\u0027XSS attack!\u0027)\u003B\u0022\u0022\u003B";
       ...
    </script>

.. _CSS Context:

CSS Context and Escaping
========================

The browser will treat any code inside a ``<style>`` tag or ``style`` attribute
in an HTML page as a CSS context, or something that requires CSS parsing. CSS
parsing has its own rules, and requires CSS-escaping.

In a CSS context, user supplied data has some additional constraints required
for keeping it safe:

* User supplied data can only appear as the value of a style property. In other
  words, never allow a user to supply the entire contents of the style tag or
  style property, or anything outside of the limited scope of an individual
  property value.

* User supplied URLs must use a whitelisted or acceptable protocol (e.g. http).
  This is to avoid users being able to supply a URL that uses the "javascript"
  protocol as an example.

* User supplied style property values must not contain ``expression(...)`` due
  to an IE feature that would enable arbitrary JavaScript to run.

There are no existing helper functions for this in the platform. If you need to
use user supplied data in a CSS context you must work with edX to help expand
the suite of available helpers.

For more information, see
`OWASP: CSS and XSS <https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet#RULE_.234_-_CSS_Escape_And_Strictly_Validate_Before_Inserting_Untrusted_Data_into_HTML_Style_Property_Values>`_.

.. _URL Context:

URL Context and Escaping
========================

URLs require multiple types of escaping. This typically involves both
URL-escaping, in addition to either HTML-escaping or JavaScript-escaping.

There are many special characters that are meaningful in a URL. For example,
both `&` and `=` are used to designate parts of the query string. If data is
being provided as a query parameter, and it may contain special characters, it
must be fully URL-escaped. This is especially true with user provided data which
could contain any character. Using the JavaScript URL-escaping functions as an
example, you would use the ``encodeURIComponent`` function on the data which
will URL-escape all special characters.  Here is an example.

.. code-block:: javascript

    var url = "http://test.com/?data=" + encodeURIComponent(userData)

URL-escaping is susceptible to double-escaping, meaning you must URL-escape its
parts exactly once. It is best to perform the URL-escaping at the time the URL
is being assembled.

Additionally, you will typically HTML-escape or JavaScript-escape a URL
following the same rules for any other data added to the page, since a properly
URL-escaped URL may still contain characters that are meaningful in an HTML
context, like ``&`` and ``'``.

For example, when adding a URL to the ``href`` attribute of an anchor tag
(``<a>``), it should already be properly URL-escaped, and would need to be
HTML-escaped at the time it is added to the HTML.

.. note:: If the entire URL is user provided, additional validation is required.

When an entire URL is user provided, and not just some query parameters, you
must also validate the URL to ensure it uses a whitelisted or acceptable
protocol (e.g. https). This is to avoid users being able to supply a URL that
uses the "javascript" protocol as an example.

For more information, see `oWASP: URL Escape <https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet#RULE_.235_-_URL_Escape_Before_Inserting_Untrusted_Data_into_HTML_URL_Parameter_Values>`_.


Editing Template Files
**********************

When you edit template files (including Mako templates, Underscore templates,
or JavaScript), use the appropriate conventions.

The topics that follow address these points for each type of file.

#. What has to be at the top of the file (if anything) to make it safe?

#. How is code properly escaped? The answer is different depending on the
   templating language and the context.

#. How do you properly handle internationalization and escaping together? For
   more information, see :ref:`i18n`.

.. note:: Remember to take into account the type of file in addition to the
   programming language involved. For example, JavaScript embedded in an HTML
   Mako template is treated differently than JavaScript in a pure .js file.

To find the proper guidelines to follow, first start with the appropriate file
type below.

.. contents::
   :depth: 2
   :local:

.. _Safe Django Template Files:

Django Template Files
=====================

.. highlight:: django

Django templates are considered "safe by default", meaning that expressions
are HTML-escaped by default. HTML-escaping is not always the right choice for
escaping, for example, with embedded JavaScript.


.. _Safe Mako Template Calls:

Mako Template() Calls in Python Files
=====================================

.. highlight:: mako

If a Mako template is loaded from Python outside of the general template loading
scheme, the following default filters should be provided to make the template
safe by default (i.e. use HTML-escaping by default).

.. code-block:: mako

    template = Template(" ... ",
        default_filters=['decode.utf8', 'h'],
    )


.. _Safe Mako Template Files:

Mako Template Files
===================

This topic covers the best practices for protecting Mako template files from XSS
vulnerabilities.

If you need to convert a legacy Mako template to be safe by default, it is
recommended that you do the following:

* First read through the following subtopics and become familiar with the
  current best practices.

* Next, follow the step-by-step instructions detailed in
  :ref:`Making Mako Templates Safe By Default`, which will often refer back to
  this topic.

.. _HTML-Escape Mako by Default:

HTML-Escape by Default in Mako
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. highlight:: mako

For Mako templates, all expressions will use HTML-escaping by default. This is
accomplished by adding the following directive to the very top of each
template. ::

    <%page expression_filter="h"/>

Using this default HTML-escaping, the following combination will represent an
HTML-escaped expression. ::

    <%page expression_filter="h"/>
    ...
    ${data}

the first filter. This can be seen in some of the examples below.

If you need to disable the default filters, you must use the ``n`` filter as
For more information, see `Mako: Expression Filtering <http://docs.makotemplates.org/en/latest/filtering.html>`_.

Determining the Context in Mako
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most of the Mako template files are in an HTML context. That is why
HTML-escaping is a good default option.

A JavaScript context can either appear explicitly through the use of a
``<script>`` tag, or implicitly through the use of ``<%static:require_module>``,
which itself sets up the ``<script>`` context.

When converting a Python object to JSON, there are two very similar filters
named ``dump_html_escaped_json`` and ``dump_js_escaped_json``. It is important
to first know the context you are in to properly choose the ``html`` or ``js``
version.

Additionally, make sure you follow the best practices for :ref:`URL Context`
when working with URLs, and :ref:`CSS Context` when in the context of a
``<style>`` tag or style attribute.

.. _HTML Context in Mako:

HTML Context in Mako
~~~~~~~~~~~~~~~~~~~~

Most Mako expressions in an HTML context will already be properly HTML-escaped.
See :ref:`HTML-Escape Mako by Default`.

When you need to dump JSON in the context of HTML (for example, into a data
attribute), you must use ``dump_html_escaped_json``. This same filter can be
used for numbers and booleans in addition to dicts and lists. If you have a
string, continue to use the default ``h`` filter. You must import and use
``dump_html_escaped_json`` as seen in the following example.

.. code-block:: mako

    <%page expression_filter="h"/>
    <%! from openedx.core.djangolib.js_utils import dump_html_escaped_json %>
    ...
    <div
        data-course-name='${course.name}'
        data-course-options='${course.options | n, dump_html_escaped_json}'
        data-course-max-students='${course.max_students | n, dump_html_escaped_json}'
        data-course-is-great='${course.is_great | n, dump_html_escaped_json}'
    ></div>

For translations that contain no HTML tags, the default HTML-escaping is
enough. You must only import and use ``ugettext`` as shown in the following
simple example.

.. code-block:: mako

    <%page expression_filter="h"/>
    <%!
    from django.utils.translation import ugettext as _
    %>
    ...
    ${_("Course Outline")}

For more complicated examples of translations that mix plain text and HTML, use
the the ``HTML()``, ``Text()``, and ``format()`` functions. Use the ``HTML()``
function when you have a replacement string that contains HTML tags. For the
``HTML()`` function to work, you must first use the ``Text()`` function to wrap
the plain text translated string. Both the ``HTML()`` and ``Text()`` functions
must be closed before any calls to ``format()``.  You will not use the ``Text``
function where you don't need the ``HTML()`` function.  See the following
example for how to import and use these functions.

.. code-block:: mako

    <%page expression_filter="h"/>
    <%!
    from django.utils.translation import ugettext as _

    from openedx.core.djangolib.markup import Text, HTML
    %>
    ...
    ${Text(_("Click over to {link_start}the home page{link_end}.")).format(
        link_start=HTML('<a href="/home">'),
        link_end=HTML('</a>'),
    )}


For more details about translating strings and ensuring proper escaping, see
:ref:`i18n`.

There are times where a block of HTML is retrieved using a function in a Mako
expression. For example, review the following Mako expression.

.. code-block:: mako

    <%page expression_filter="h"/>
    from openedx.core.djangolib.markup import HTML
    ...
    ${HTML(get_course_date_summary(course, user))}

In this example, you use the ``HTML()`` function to declare the results of the
function as HTML and turn off the default HTML-escaping. Using the ``HTML()``
function by itself can be very dangerous, unless you make sure that the
function returning the HTML has itself properly escaped any plain text.


.. _JavaScript Context in Mako:

JavaScript Context in Mako
~~~~~~~~~~~~~~~~~~~~~~~~~~

As a general guideline, JavaScript in Mako templates should be kept to an
absolute minimum for a number of reasons.

* It is very hard to mix syntax appropriately, which can lead to bugs, some of
  which might lead to security issues.

* The JavaScript code cannot easily be tested.

* The JavaScript code does not get included for code coverage.

The only JavaScript code in Mako that is appropriate is the minimal RequireJS
code and Factory setup code that is used to pass data from the server side to
client side code. This topic will show this example.

In coding this glue between server side and client side code, special Mako
filters are required for working with Mako expressions when in a JavaScript
context.

When you need to dump JSON in the context of JavaScript, you must use either the
``js_escaped_string`` or ``dump_js_escaped_json`` filters. These are the
JavaScript-escaping equivalents of ``h`` and ``dump_html_escaped_json``
respectively.

With ``js_escaped_string`` you must supply the enclosing quotes. When ``None``
is supplied to ``js_escaped_string``, it results in an empty string for
convenience.

The JavaScript context can either appear explicitly through the use of a
``<script>`` tag, or implicitly through the use of ``<%static:require_module>``,
which itself sets up the ``<script>`` context.

Here is an example of how to import and use ``js_escaped_string`` and
``dump_js_escaped_json`` in the context of JavaScript in a Mako template.

.. code-block:: mako

    <%namespace name='static' file='static_content.html'/>
    <%!
    from openedx.core.djangolib.js_utils import (
        dump_js_escaped_json, js_escaped_string
    )
    %>
    ...
    <%static:require_module module_name="js/course_factory" class_name="CourseFactory">
        CourseFactory({
            course_name: '${course.name | n, js_escaped_string}',
            course_options: ${course.options | n, dump_js_escaped_json},
            course_max_students: ${course.max_students | n, dump_js_escaped_json},
            course_is_great: ${course.is_great | n, dump_js_escaped_json},
        });
    </%static:require_module>

If you have a string that already contains JSON, rather than a Python object,
see :ref:`Strings with JSON` for how to resolve this situation.

In general, the JavaScript code inside a Mako template file should be succinct,
simply providing a bridge to a JavaScript file. For best practices for
any JavaScript code outside of the Mako expressions, see
:ref:`Safe JavaScript Files`.


URL Context in Mako
~~~~~~~~~~~~~~~~~~~

To properly URL-escape in Python, you can use `urllib
<https://docs.python.org/2/library/urllib.html#utility-functions>`_.

For more details about URLs, see :ref:`URL Context`.


Mako Defs
~~~~~~~~~

In a Mako ``%def`` we encounter one of the rare cases where we need to turn off
default HTML-escaping using ``| n, unicode``. In the example below, this is
done because the expression assumes that the required JavaScript-escaping was
already performed by the caller.

Be extremely careful when using ``| n, unicode``, and make sure the originating
code is properly escaped. Note that the ``n`` filter turns off all default
filters, including the default ``unicode`` filter, so it is added back
explicitly. Here is an example.

.. code-block:: mako

    <%page expression_filter="h"/>
    ...
    <%def name="require_module(module_name, class_name)">
        <script type="text/javascript">
            ...
            ${caller.body() | n, unicode}
            ...
        </script>
    </%def>

For more information, see `Mako: Defs and Blocks
<http://docs.makotemplates.org/en/latest/defs.html>`_.


.. _Safe JavaScript Files:

JavaScript Files
================

.. highlight:: javascript

JavaScript files are often used to perform DOM manipulation, and must properly
HTML-escape text before inserting it into the DOM.

The UI Toolkit has introduced various ``StringUtils`` and ``HtmlUtils`` that are
handy for handling escaping in JavaScript.  You can declare ``StringUtils`` and
``HtmlUtils`` as dependencies using RequireJS ``define`` as seen in the following
example.

.. code-block:: javascript

    define(['backbone',
            'underscore',
            'gettext',
            'edx-ui-toolkit/js/utils/string-utils',
            'edx-ui-toolkit/js/utils/html-utils'],
        function (Backbone, _, gettext, StringUtils, HtmlUtils) {
            ...

The following ``HtmlUtils`` functions all make use of ``HtmlUtils.HtmlSnippet``.
An HTML snippet is used to communicate to other functions that the string it
represents contains HTML that has been safely escaped as necessary.

The ``HtmlUtils.ensureHtml()`` function will ensure you have properly escaped
HTML by HTML-escaping any plain text string, or simply returning any HTML
snippet provided to it.

If you must do string interpolation and translation, and your string does not
contain any HTML, then use the plain text ``StringUtils.interpolate()``
function as follows. This function will not escape, and follows the best
practice of delaying escaping as late as possible. Since the result is a plain
text string, it would properly be treated as unescaped text by any of the
``HtmlUtils`` functions.

.. code-block:: javascript

    StringUtils.interpolate(
        gettext('You are enrolling in {courseName}'),
        {
            courseName: 'Rock & Roll 101'
        }
    );

If you are performing string interpolation and translation with a mix of plain
text and HTML, then you must perform HTML-escaping early and the result can be
represented by an HTML snippet.  Use the ``HtmlUtils.HTML()`` function to wrap
any string that is already HTML and must not be HTML-escaped. The function
``HtmlUtils.interpolateHtml()`` will perform the interpolations and will
HTML-escape any plain text and not HTML-escape anything wrapped with
``HtmlUtils.HTML()``. See the following example.

.. code-block:: javascript

    HtmlUtils.interpolateHtml(
        gettext('You are enrolling in {spanStart}{courseName}{spanEnd}'),
        {
            courseName: 'Rock & Roll 101',
            spanStart: HtmlUtils.HTML('<span class="course-title">'),
            spanEnd: HtmlUtils.HTML('</span>')
        }
    );

You can also use ``HtmlUtils.joinHtml()`` to join together a mix of HTML
snippets and plain text strings into a larger HTML snippet where each part will
be properly HTML-escaped as necessary.  See the following example.

.. code-block:: javascript

    HtmlUtils.joinHtml(
        HtmlUtils.HTML('<p>'),
        gettext('This is the best course.'),
        HtmlUtils.HTML('</p>')
    )

Often, much of the preparation of HTML in JavaScript can be written using an
Underscore.js template. The function ``HtmlUtils.template()`` provides
some enhancements for escaping.  First, it makes ``HtmlUtils`` available inside
the template automatically. Also, it returns an HTML snippet so that other
``HtmlUtils`` functions know not to HTML-escape its results. It is assumed that
any HTML-escaping required will take place inside the Underscore.js template.
Follow the best practices detailed in :ref:`Safe Underscorejs Template Files`.

The final step of DOM manipulation in JavaScript often happens using JQuery.
There are some JQuery functions like ``$.text()``, ``$.attr()`` and ``$.val()``
that expect plain text strings and take care of HTML-escaping its input for you.

There are other JQuery functions like ``$.html()``, ``$.append()`` and
``$.prepend()`` that expect HTML and adds it into the DOM. However, these
functions don't know whether or not they are being provided properly escaped
HTML as represented by an HTML snippet. In place of these functions, you will
use ``HtmlUtils.setHtml()``, ``HtmlUtils.append()`` and ``HtmlUtils.prepend()``
respectively. These ``HtmlUtils`` JQuery wrappers respect HTML snippets, and can
be used as seen in the following example.

.. code-block:: javascript

    HtmlUtils.setHtml(
        this.$el.html,
        HtmlUtils.joinHtml(
            HtmlUtils.HTML('<p>'),
            gettext('This is the best course.'),
            HtmlUtils.HTML('</p>')
        )
    );

In the case of Backbone.js models, although attributes can be retrieved using
the ``get()`` or ``escape()`` functions, you should avoid using the
``escape()`` function, which will HTML-escape the retrieved value. It is
preferable to use the ``get()`` function and delay escaping until the time of
rendering, which is often handled using an Underscore.js template.

To properly URL-escape, you can use the `JavaScript functions
<http://www.w3schools.com/jsref/jsref_obj_global.asp>`_ ``encodeURI`` and
``encodeURIComponent``.  For example, to properly URL-escape user provided data
before it is used as a query parameter, you could do the following.

.. code-block:: javascript

    var url = "http://test.com/?data=" + encodeURIComponent(userData)

For more details about URLs, see :ref:`URL Context`.


.. _Safe CoffeeScript Files:

CoffeeScript Files
==================

.. highlight:: coffeescript

For CoffeeScript files, follow the same guidelines as provided for
:ref:`JavaScript files <Safe JavaScript Files>`, but using the CoffeeScript
syntax.


.. _Safe Underscorejs Template Files:

Underscore.js Template Files
============================

.. highlight:: javascript

The best way to HTML-escape expressions in an Underscore.js template is to use
the ``<%-`` tag, which will perform the HTML-escaping.

There are some exceptions where you must use a combination of ``<%=``, which
does not escape, and one of the UI Toolkit ``HtmlUtils`` functions. One example
is when using the ``HtmlUtils.interpolateHtml()`` function to translate strings
that are mixed plain text and HTML. You can easily gain access to the
``HtmlUtils`` object inside a template by creating rendering the Underscore.js
template using the ``HtmlUtils.template()`` function.

If you need to pass an HTML snippet to a template, which has already been
HTML-escaped, you should name the variable with an ``Html`` suffix, and use
``HtmlUtils.ensureHtml()`` to ensure it was in fact properly HTML-escaped. See
the following example.

.. code-block:: javascript

    <%= HtmlUtils.ensureHtml(nameHtml) %>

For more details on using the ``HtmlUtils`` utility functions, see
:ref:`Safe JavaScript Files`.


.. _Making Mako Templates Safe By Default:

Making Legacy Mako Templates Safe by Default
********************************************

.. highlight:: mako

This topic provides a step-by-step set of instructions for making our Mako
templates safe by default. For all best practices for writing a new Mako
template, see :ref:`Safe Mako Template Files`.

By default, our Mako templates perform no escaping for expressions.
We refer to this as not being "safe by default". Our intention is get to the
state where our Mako templates *are* "safe by default", by ensuring that Mako
template expressions perform HTML-escaping by default.

.. note:: It is important to understand that HTML-escaping might not be the
   right thing to do in all cases, but it is a good starting place. Additional
   escaping filters are available to help with other scenarios.

Due to valid exceptions to the general rule of HTML-escaping, it is not
possible to configure escaping for all Mako templates in the entire platform
without introducing errors.

The current process is for developers to make changes to each Mako template to
ensure that all expressions use HTML-escaping by default. For details, see
:ref:`Set HTML Escaping Filter as Default`.

The following topics describe the steps you need to take to make your Mako
templates safe by default. Although we have attempted to cover as many
scenarios as possible, we are sure to have missed some cases. If you are
unsure about what to do, reach out and ask for help. For contact information,
see the `Getting Help <https://open.edx.org/getting-help>`_ page on the Open
edX portal .

.. note:: If you come across an old template that is no longer in use and can
   be cleaned out of the platform, help to remove the template rather than
   following these steps.

.. contents::
   :depth: 1
   :local:


.. _Set HTML Escaping Filter as Default:

Set HTML-Escaping Filter as Default
===================================

Add the following line to the very top of your template.

.. code-block:: mako

    <%page expression_filter="h"/>

If this line has already been added, the process of making the template safe
by default might have been already completed.


Search for JavaScript Contexts
==============================

Search for any JavaScript contexts in the Mako template. These might appear
either explicitly through the use of a ``<script>`` tag, or implicitly through
the use of ``<%static:require_module>``.

Check that all Mako expressions (``${}``) in these JavaScript contexts are
using either ``| n, dump_js_escaped_json`` or ``| n, js_escaped_string``, as
detailed in :ref:`JavaScript Context in Mako`.  For strings, use
``js_escaped_string`` with quotes around the expression, rather than
``dump_js_escaped_json``.

If the template was using the ``escapejs`` function, replace it with ``| n,
js_escaped_string``, which will also make sure that the string is unicode and
will replace ``None`` with an empty string.

Take note of any expression that was mistakenly using ``| h`` in a JavaScript
context. Although you likely just fixed a bug, you will want to pay extra
attention to the downstream JavaScript that is rendering this data and double-
check that it is being properly escaped. It might not be, because it would
have caused a double-escaping issue as it was.


Replace Calls to ``json.dumps``
===============================

Mako templates should not include calls to ``json.dumps``. Instead, you must
use the ``dump_js_escaped_json`` or ``dump_html_escaped_json`` filters as
detailed in :ref:`Safe Mako Template Files`. You must understand whether the
template is writing HTML or JavaScript in order to choose the correct filter.

Additionally, if you find a case where your string already contains JSON, it
is likely that ``json.dumps`` was called prematurely in Python before passing
the data to Mako. In this case, you should refactor to pass the data in its
original form, and then once again use one of the provided filters in the Mako
template.

Finally, if there is no way around having to work with a string that is already
JSON, the only way to ensure that any potential user-provided data is safe is
to use ``json.loads`` and then use one of the provided filters.


Remove All ``h`` Filters
========================

Review the page for any Mako expressions that have an ``h`` filter and remove
this redundant HTML-escaping.

Before::

    ${data | h}

After::

    ${data}


Fix Translations That Contain HTML Tags
=======================================

Search the page for calls to ``_()`` that have replacement strings that
contain actual HTML tags (such as ``<strong>``). For these cases, you must use
both the ``HTML()`` and ``Text()`` functions as documented in :ref:`i18n`.


Remove Calls to ``display_name_with_default_escaped``
======================================================

The XBlock function ``display_name_with_default_escaped`` has been deprecated
and should not be used. Instead, you must use the call
``display_name_with_default`` and follow the best practices for proper
escaping based on the context.

It might be that ``display_name_with_default_escaped`` was called from Python
while setting up the context for your Mako template. You still must fix this
to be ``display_name_with_default`` and make sure it is properly escaped in
the Mako template.

Take note of any places where this value was used in a JavaScript context. You
must make sure that this data is properly escaped downstream when it is
finally added to the page (for example, in an Underscore.js template).


Fix Custom Escaping
===================

One example of custom escaping is when the code includes ``&amp;`` directly in a
string. These should be removed.

Before::

    ${_("Files &amp; Uploads")}

After::

    ${_("Files & Uploads")}

Another example of custom escaping is if you have a string that was already
escaped through a call such as ``replace('<', '&lt;')``.

Again, the preferred solution is to not escape the string at all until you are
in the template, and then to escape only using the best practices previously
detailed.

If a string absolutely must be HTML-escaped before getting to the template, you
should use some combination of ``Text()`` and ``HTML()`` provided for use with
translations. Also, you should name any such variable with the suffix ``_html``
to make it clear that it contains HTML that was already escaped. For more
information, see :ref:`i18n`.


Fix Downstream JavaScript and Underscore.js Templates
=====================================================

Because Mako templates only generate the initial page source, you should
ensure that any downstream JavaScript files or Underscore.js templates also
follow the best practices.

When you have found the proper downstream JavaScript and Underscore.js template
files, you can follow the best practices as detailed in :ref:`Safe JavaScript
Files` and :ref:`Safe Underscorejs Template Files`.

For information about internationalized strings found in JavaScript, see
:ref:`i18n`.

Navigating JavaScript and Underscore.js Templates
=================================================

TODO: Move this to Confluence and link from here.

It can be difficult to trace through all of the JavaScript dependencies in some
of our legacy code.

One tip that is useful for our legacy code is knowing that ``-tpl`` is often
appended to the name of an Underscore.js template name inside the JavaScript
code. For example, you might see the following line of JavaScript.

.. code-block:: javascript

    _.template($("#show-textbook-tpl").text());

The above code would indicate you will find the template code in a file named
``show-textbook.underscore``.

Newer code uses RequireJS to manage the JavaScript dependencies.  You may see
code like the following.

.. code-block:: javascript

    require(['js/models/course'], function(Course) {

This would indicate that you'll find a JavaScript file in
``js/models/course.js``.


Run Safe Template Linter
========================

Follow instructions for the :ref:`Safe Template Linter`. Search for any rule
violations in the files you are working on. Since accuracy and completeness is
not guaranteed, this should just be used to check your work.


Advanced Topics
***************

The following advanced topics provides details that may be useful for those
interested in a deeper understanding or an understanding of more rare
situations.

.. contents::
   :depth: 1
   :local:


Why both ``js_escaped_string`` or ``dump_js_escaped_json``?
===========================================================

In Mako templates, why don't we just use ``dump_js_escaped_json`` to escape
strings as well, rather than using ``js_escaped_string``?

* The ``js_escaped_string`` function provides the additional benefit of
  returning an empty string in the case of None.
* The ``js_escaped_string`` and wrapping quotes makes the expected type more
  declarative.


Mako Filter Ordering and the ``n`` filter
=========================================

Mako executes any default filter before any filter that is added inside an
expression. Additionally, one of the default filters is the ``unicode`` filter.
This filter is used to decode to utf8, but only if the Python object is not
already unicode.

Let's take the following example Mako expression.

.. code-block:: mako

    ${data | h}

When Mako compiles this to Python, it gets translated to the following Python
code.

.. code-block:: python

    __M_writer(filters.html_escape(filters.decode.utf8(data)))

From the Python line above, you can see that the default ``unicode`` filter is
applied before the the ``h`` filter which was supplied inside the expression.

The ``n`` filter can be used to turn off all default filters, including the
``unicode`` filter. Here is an example Mako expression.

.. code-block:: mako

    ${data | n}

In this case, when Mako compiles this to Python we get the following Python.

.. code-block:: python

    __M_writer(data)

For more information, see `Mako: Expression Filtering <http://docs.makotemplates.org/en/latest/filtering.html>`_.


Mako Blocks
===========

A Mako ``%block`` can sometimes create tricky situations where the context is
not clear. In these cases, it would be best to provide the context (e.g. HTML or
JavaScript) in the name of the block.

Take the following Mako ``%block`` definition as an example.

.. code-block:: mako

    <%page expression_filter="h"/>
    ...
    <%block name="html_title">${display_name}</%block>

Based on the above ``%block`` definition, only the name of the block tells us
that it is HTML-escaped, and only usable in an HTML context. You could not use
this same ``%block`` in a JavaScript context.

Here is this same ``%block`` above, as it is actually used to display the title.

.. code-block:: mako

    <title>
        <%block name="html_title"></%block>
    </title>

For more information, see `Mako: Defs and Blocks
<http://docs.makotemplates.org/en/latest/defs.html>`_.


.. _Strings with JSON:

Strings Containing JSON in Mako
===============================

In a Mako template, it is better to work with Python objects, rather than
strings containing JSON.

If you find yourself with a string that contains JSON inside a Mako template,
try to remove the call to ``json.dumps`` that created the JSON string in the
Python file feeding the Mako template.

In the rare case that you can't avoid having a string that contains JSON, and it
might contain user provided data, you must ensure it is safe by parsing it and
then dumping it again. Here is an example.

.. code-block:: mako

    <script>
        var options = ${json.loads(options_json_string) | n, dump_js_escaped_json};
    </script>


.. _Safe Template Linter:

Safe Template Linter
********************

The safe template linter is a tool to help ensure best practices are being
followed.

The linter should be used in addition to following all documented best
practices. It does not yet cover all rules. Additionally, for rules it
does cover, it may output false positives. This is especially true with the
Underscore.js template expressions.

For help running the linter, use the following command.

.. code-block:: bash

    edxapp@precise64:~/edx-platform$ ./scripts/safe_template_linter.py --help


.. _Safe Templates Additional Resources:

Additional Resources
********************

To learn more about XSS in general, see the following references.

* `OWASP: Cross-site Scripting (XSS) <https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)>`_
* `OWASP: XSS (Cross Site Scripting) Prevention Cheat Sheet <https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet>`_
* `OWASP: DOM based XSS Prevention Cheat Sheet <https://www.owasp.org/index.php/DOM_based_XSS_Prevention_Cheat_Sheet>`_
* `OWASP: XSS Filter Evasion Cheat Sheet <https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet>`_
