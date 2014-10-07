import pytest
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from rest_framework.parsers import JSONParser, FormParser, MultiPartParser


factory = APIRequestFactory()


def test_content_type_override_query():
    from rest_url_override_content_negotiation import \
        URLOverrideContentNegotiation
    negotiation = URLOverrideContentNegotiation()
    parsers = (JSONParser, FormParser, MultiPartParser)

    requestWithQueryParam = Request(
        factory.post('/?content_type=application/x-www-form-urlencoded',
                     {'email': 'mmmmmm@test.com'},
                     content_type='text/plain'))
    assert FormParser is negotiation.select_parser(
        requestWithQueryParam, parsers)

    requestWithoutQueryParam = Request(
        factory.post('/', {'email': 'mmmmmm@test.com'},
                     content_type='text/plain'))
    assert None is negotiation.select_parser(
        requestWithoutQueryParam, parsers)
