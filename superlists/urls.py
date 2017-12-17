from django.conf.urls import url
from django.contrib import admin
from lists import views
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', views.home_page, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
]
