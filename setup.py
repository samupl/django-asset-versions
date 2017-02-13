import os
import re
from setuptools import setup, find_packages


def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as fd:
        return fd.read()


VERSION_FILE = 'asset_versions/_version.py'
version_text = read(VERSION_FILE)
VS_RE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VS_RE, version_text, re.M)
if mo:
    version = mo.group(1)
else:
    raise RuntimeError(
        "Unable to find version string in {}".format(VERSION_FILE)
    )


install_requires = [
    'Django >= 1.10.0',
    'GitPython >= 2.1.1',
]
test_requires = []


setup(
    name="django-asset-versions",
    version=version,
    author="Jakub Szafrański",
    author_email="s@samu.pl",
    description=(
        "Collection of templatetags allowing versioning of static assets"
    ),
    license="MIT",
    url="https://github.com/samupl/django-asset-versions",
    packages=[
        'asset_versions',
        'asset_versions.templatetags',
        'asset_versions.backends',
    ],
    long_description=read('README.md'),
    install_requires=install_requires,
    extras_require={
        ':python_version=="2.7"': [
            'functools32 >= 3.2.3'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
0
