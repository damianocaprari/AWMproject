"""AWMproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy

###
# Overrides of default values of admin.site
###
# Text to put at the end of each page's <title>.
admin.site.site_title = gettext_lazy('AWMproject site admin')

# Text to put in each page's <h1>.
admin.site.site_header = gettext_lazy('AWMproject administration')

# Text to put at the top of the admin index page.
#admin.site.index_title = gettext_lazy('Site administration')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('storefront/', include('storefront.urls', namespace='sf')),
]
