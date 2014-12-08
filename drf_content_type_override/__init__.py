from rest_framework.negotiation import DefaultContentNegotiation
from rest_framework.utils.mediatypes import media_type_matches


class URLOverrideContentNegotiation(DefaultContentNegotiation):
    def select_parser(self, request, parsers):
        content_type = request.content_type
        if not content_type or content_type == 'text/plain':
            content_type = request.QUERY_PARAMS.get('content_type',
                                                    content_type)
        for parser in parsers:
            if media_type_matches(parser.media_type, content_type):

                # Create a parser that proxies to the matching one but with the
                # overridden content type.
                class ParserWrapper(object):
                    media_type = content_type

                    def parse(self, stream, media_type=None, parser_context=None):
                        return parser.parse(stream, content_type, parser_context)

                return ParserWrapper()
        return None
