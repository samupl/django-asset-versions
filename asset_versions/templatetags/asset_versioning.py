import importlib

from django import template
from django.conf import settings


register = template.Library()


BACKEND = getattr(
    settings,
    'ASSET_VERSION_BACKEND',
    'asset_versions.backends.version_git.Git'
)
BACKEND_MODULE_STR, BACKEND_CLASS_STR = BACKEND.rsplit('.', 1)
BACKEND_MODULE = importlib.import_module(BACKEND_MODULE_STR)
BACKEND_CLASS = getattr(BACKEND_MODULE, BACKEND_CLASS_STR)


@register.simple_tag
def version():
    """
    Returns a version string from an asset backend defined in the settings
    (long version).

    :return: Version string (long)
    :rtype: str
    """

    cls = BACKEND_CLASS()
    return cls.version_long()


@register.simple_tag
def version_short():
    """
    Returns a version string from an asset backend defined in the settings
    (short version, if backend supports any).

    :return: Version string (short)
    :rtype: str
    """

    cls = BACKEND_CLASS()
    return cls.version_short()
