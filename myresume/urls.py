from django.contrib import admin
from django.urls import path,include

from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('employers.urls')),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
]
