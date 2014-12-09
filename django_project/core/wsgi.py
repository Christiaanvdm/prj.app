"""
WSGI config for projecta project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "projecta.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.

# Customised by Tim so we can access env vars set in apache
import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()


def application(environ, start_response):
    """Factory for the application instance.

    :param environ: os environment passed in by web server.
    :type environ: dict

    :param start_response: ?
    :type start_response: ?

    Places env vars defined in apache conf into a context accessible by django.
    """
    if 'GITHUB_URL' in environ:
        os.environ['GITHUB_URL'] = environ['GITHUB_URL']
    if 'GITHUB_USER' in environ:
        os.environ['GITHUB_USER'] = environ['GITHUB_USER']
    if 'GITHUB_PASSWORD' in environ:
        os.environ['GITHUB_PASSWORD'] = environ['GITHUB_PASSWORD']
    return _application(environ, start_response)

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
