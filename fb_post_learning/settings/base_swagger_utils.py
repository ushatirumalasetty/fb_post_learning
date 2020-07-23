import os


from fb_post_learning.settings.base import *

# swagger utils #

PRINT_REQUEST_RESPONSE_TO_CONSOLE = False

STORE_LATENCY_OBJECT = True

INSERT_LAST_ACCESS_REQUIRED = True

STORE_LAST_ACCESS_OBJECT = True

################ Installed Apps ###############

# Application definition
from django_swagger_utils.drf_server.utils.general.import_app_settings import import_app_settings

THIRD_PARTY_APPS = []
APPS = [
    "fb_post_clean_arch"
]

INSTALLED_APPS += THIRD_PARTY_APPS
INSTALLED_APPS += APPS

# this will import all settings from [APPS].conf.settings
for app_name in APPS:
    try:
        _dict = import_app_settings(app_name)
        locals().update({name: _dict["module_dict"][name] for name in _dict["to_import"]})
    except ImportError as err:
        print(err)


# *************************** Swagger Utils ***************************

from django_swagger_utils.drf_server.utils.decorator.getDecryptedData import getDecryptedData
from django_swagger_utils.drf_server.utils.decorator.getPrivateKeyFromClientKeyRelatedDetails import \
    getPrivateKeyFromClientKeyRelatedDetails

SWAGGER_UTILS = {
    "DEFAULTS": {
        "REQUEST_WRAPPING_REQUIRED": False,
        "REQUEST_ENCRYPTION_REQUIRED": False,
        "GET_CLIENT_KEY_DETAILS_FUNCTION": getPrivateKeyFromClientKeyRelatedDetails,
        "GET_DECRYPTED_DATA_FUNCTION": getDecryptedData,
        "RESPONSE_SERIALIZER_VALIDATION": True
    },
    "CUSTOM_EXCEPTIONS": {
        "CustomException": {
            "http_status_code": 404,
            "is_json" : True,
        }
    },
    "APPS": {

        "fb_post_clean_arch": {}

    },
    "HOST": os.environ.get('APIGATEWAY_ENDPOINT', '127.0.0.1:8080'),
}

API_KEY_AUTHENTICATION_CLASS = \
    "fb_post_learning.common.authentication.APIKeyAuthentication"

THIRD_PARTY_SWAGGER_APPS = [
]
INSTALLED_APPS += THIRD_PARTY_SWAGGER_APPS