SECRET_KEY = 'SEKRIT'

INSTALLED_APPS = ('rest_framework',)

REST_FRAMEWORK = {
    'DEFAULT_CONTENT_NEGOTIATION_CLASS':
    'drf_url_content_type_override.URLOverrideContentNegotiation',
}
