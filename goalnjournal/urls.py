from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('goal.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
]

urlpatterns += staticfiles_urlpatterns()