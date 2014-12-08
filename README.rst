DRF URL Content Type Override
===================================================

DRF URL Content Type Override allows the content type of the request to be overriden with a url parameter.


Why would I need this?
=============================
Sometimes it makes sense to override the content type specified in the header. For example, some browser's XHR, such as IE9, are unable to support CORS. Pollyfills like, `jQuery-ajaxTransport-XDomainRequest`_ or httpplease's `oldiexdomain.js`_ plug-in get around this by using XDomainRequest, which supports CORS. The problem is XDomainRequest only sends a content type of text/plain in the header. This is problematic when POSTing form data. DRF URL Content Type Override let's you specify a content type which will override the header value.

.. _`jQuery-ajaxTransport-XDomainRequest`: https://github.com/MoonScript/jQuery-ajaxTransport-XDomainRequest
.. _`oldiexdomain.js`: https://github.com/matthewwithanm/httpplease.js/blob/master/plugins/oldiexdomain.js


Install
-------------

.. code-block:: shell

  pip install drf-url-content-type-override

Add 'DEFAULT_CONTENT_NEGOTIATION_CLASS'

.. code-block:: python

  REST_FRAMEWORK = {
    'DEFAULT_CONTENT_NEGOTIATION_CLASS': 'drf_url_content_type_override.URLOverrideContentNegotiation',
  }


Usage
-------------
Example: Javascript on a different domain from the API.

.. code-block:: javascript

  jquery.ajax({
    'url': 'http://apidomain.com/api/1/contact?_content_type=application/x-www-form-urlencoded',
    'type': 'POST',
    'data': {'name': 'Chris'}
  })


For more background see https://github.com/tomchristie/django-rest-framework/pull/1731
