SECRET_KEY = 'SEKRIT'

INSTALLED_APPS = ('rest_framework',)

REST_FRAMEWORK = {
    'DEFAULT_CONTENT_NEGOTIATION_CLASS':
    'rest_url_override_content_negotiation.URLOverrideContentNegotiation',
}
