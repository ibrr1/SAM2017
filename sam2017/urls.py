from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'sam2017_app.views.login.user_login', name='login'),

    url(r'^registration/$', 'sam2017_app.views.registration.user_registration', name='registration'),

    url(r'^user_profile/$', 'sam2017_app.views.user_profile.user_profile', name='profile'),

    url(r'^user_profile/logout/$', 'sam2017_app.views.logout.logout', name='logout'),

    url(r'^user_profile/user_information/$', 'sam2017_app.views.update_user_info.manage_account', name='modify_user_info'),
    url(r'^user_profile/paper_submission/$', 'sam2017_app.views.paper_submission.paper_submission', name='modify_user_info'),
    url(r'^user_profile/paper_list/$', 'sam2017_app.views.paper_list.paper_list', name='modify_user_info'),
    url(r'^user_profile/paper_list/download/(?P<file_name>[a-zA-Z-0-9-.-_/]+)/$', 'sam2017_app.views.paper_list.download', name='download_file'),
    url(r'^user_profile/paper_list/assign_pcm/(?P<submission_id>[a-zA-Z-0-9-.-_/]+)/$', 'sam2017_app.views.assign_pcm.onAssignPCM', name='assign_pcm'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
