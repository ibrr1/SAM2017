from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'sam2017_app.views.user_login', name='login'),

    url(r'^registration/$', 'sam2017_app.views.user_registration', name='registration'),

    url(r'^user_profile/$', 'sam2017_app.views.user_profile', name='profile'),

    url(r'^user_profile/logout/$', 'sam2017_app.views.logout', name='logout'),

    url(r'^user_profile/user_information/$', 'sam2017_app.views.manage_account', name='modify_user_info'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
