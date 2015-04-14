from django.conf.urls import include, url
from django.contrib import admin
import os

from settings import BASE_DIR

urlpatterns = [
    # Examples:
    # url(r'^$', 'OdontoCaixa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]


admin.site.index_template = os.path.join(BASE_DIR, 'templates/admin/index.html')