# django-asset-versions
A bunch of utilities to append a version string to static assets, without the requirement to clear cache after deployment

This package provides templatetags which allow to use a version string in any template from various sources - GIT, Mercurial, SVN, CHANGELOG, static file or even timeout-based.
  
## But, why?
Normally, static asset cache lifetime should be determined through Cache-Control headers. However, sometimes you cannot change these headers - for example on some shared hosting providers.

Optimization aside, the last thing you want is when you deploy a new JavaScript or CSS change, and have to notify all your website users to do a hard-refresh of cache in their browsers.

But then, even if you can control the headers, you sometimes deploy a change and need it to be available to all clients ASAP, or they will have their "version" of the site broken.

The way I've seen people overcome this obstacle is by adding some tag at the end of the static asset file, for example:

```html
<link rel="stylesheet" href="/example.css?version0.1-alpha">
```

Having that GET parameter at the end forces the client browser to download the `example.css` file as if it was brand-new, while being safely ignored by most web-servers. Not an ideal solution, but works most of the time.

## Installation

Install django-asset-versions using `pip`:

```
pip install django-asset-versions
```

Add asset_versions to INSTALLED_APPS:

```python
INSTALLED_APPS = [
    # ...
    'asset_versions',
]
```
