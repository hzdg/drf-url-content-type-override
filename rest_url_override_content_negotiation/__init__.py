from rest_framework.negotiation import DefaultContentNegotiation
from rest_framework.utils.mediatypes import media_type_matches


class URLOverrideContentNegotiation(DefaultContentNegotiation):
    def select_parser(self, request, parsers):
        content_type = request.QUERY_PARAMS.get('content_type', request.content_type)
        for parser in parsers:
            if media_type_matches(parser.media_type, content_type):
                return parser
        return None
