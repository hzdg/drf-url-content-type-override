import pytest
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from mock import Mock


factory = APIRequestFactory()


def test_content_type_override_query():
    from rest_url_override_content_negotiation import \
        URLOverrideContentNegotiation
    negotiation = URLOverrideContentNegotiation()
    parsers = (JSONParser(), FormParser(), MultiPartParser())

    requestWithQueryParam = Request(
        factory.post('/?_content_type=application/x-www-form-urlencoded',
                     {'email': 'mmmmmm@test.com'},
                     content_type='text/plain'))
    parser = negotiation.select_parser(requestWithQueryParam, parsers)
    assert parser.media_type == 'application/x-www-form-urlencoded'

    requestWithoutQueryParam = Request(
        factory.post('/', {'email': 'mmmmmm@test.com'},
                     content_type='text/plain'))
    assert None is negotiation.select_parser(
        requestWithoutQueryParam, parsers)


def test_limited_overrides():
    """
    The content type shouldn't be overridden if the header is something other
    than 'text/plain', or missing entirely.

    """
    from rest_url_override_content_negotiation import \
        URLOverrideContentNegotiation
    negotiation = URLOverrideContentNegotiation()
    parsers = (JSONParser(), FormParser(), MultiPartParser())

    req = Request(
        factory.post('/?_content_type=application/x-www-form-urlencoded',
                     {'email': 'mmmmmm@test.com'},
                     content_type='text/somethingelse'))
    assert negotiation.select_parser(req, parsers) is None


def test_parser_media_type():
    class MockParser(object):
        media_type = 'text/fake'

    MockParser.parse = Mock()

    from rest_url_override_content_negotiation import \
        URLOverrideContentNegotiation
    negotiation = URLOverrideContentNegotiation()

    req = Request(
        factory.post('/?_content_type=text/fake', {'email': 'mmmmmm@test.com'},
                     content_type='text/plain'))
    parser = negotiation.select_parser(req, [MockParser()])
    parser.parse(None, 'text/plain', None)
    MockParser.parse.assert_called_with(None, 'text/fake', None)
