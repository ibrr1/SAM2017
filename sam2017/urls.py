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

    url(r'^user_profile/review_list/$', 'sam2017_app.views.review_paper_list.review_paper_list', name='review_paper_list'),
    url(r'^user_profile/review_list/(?P<review_id>[a-zA-Z-0-9-.-_/]+)/$', 'sam2017_app.views.review_paper.review_paper', name='review_paper'),

    url(r'^user_profile/user_information/$', 'sam2017_app.views.update_user_info.manage_account', name='modify_user_info'),
    url(r'^user_profile/paper_submission/$', 'sam2017_app.views.paper_submission.paper_submission', name='modify_user_info'),
    url(r'^user_profile/paper_list/$', 'sam2017_app.views.paper_list.paper_list', name='modify_user_info'),
    url(r'^user_profile/paper_list/download/(?P<file_name>[a-zA-Z-0-9-. -_/]+)/$', 'sam2017_app.views.paper_list.download', name='download_file'),
    url(r'^user_profile/paper_list/assign_pcm/(?P<submission_id>[a-zA-Z-0-9]+)/$',
        'sam2017_app.views.assign_pcm.on_assign_pcm', name='assign_pcm'),
    url(r'^user_profile/paper_list/assign_pcm/(?P<submission_id>[a-zA-Z-0-9]+)/(?P<pcm_id>[a-zA-Z-0-9-.-_/]+)/$',
        'sam2017_app.views.assign_pcm.assign_paper', name='assign_paper'),
    url(r'^user_profile/paper_updating/(?P<paper_id>[a-zA-Z-0-9-.-_/]+)/$', 'sam2017_app.views.paper_updating.paper_updating_event', name='paper_updating'),
    url(r'^user_profile/paper_list/choose/(?P<submission_id>[a-zA-Z-0-9-.-_/]+)/$', 'sam2017_app.views.paper_list.chooseSubmission', name='choose_submission'),


    url(r'^user_profile/pcms_chosen_paper/$', 'sam2017_app.views.pcms_chosen_paper.pcms_chosen_paper', name='pcm_chosen_paper'),

    #pcc rating
    url(r'^user_profile/pcc_rating/$', 'sam2017_app.views.pcc_rating.pcc_rating', name='pcc_rate'),
    url(r'^user_profile/pcc_rating/(?P<paper_id>[a-zA-Z-0-9-.-_/]+)/$', 'sam2017_app.views.pcc_rating.view_rating', name='view_rating'),
    #Generate Report
    url(r'^user_profile/pcc_generate_report/$', 'sam2017_app.views.pcc_generate_report.pcc_generate_report', name='pcc_generate_report'),
    url(r'^user_profile/pcc_generate_report/(?P<paper_id>[a-zA-Z-0-9-.-_/]+)/$', 'sam2017_app.views.pcc_generate_report.view_report', name='view_rating'),






    #url(r'^user_profile/assign/$', 'sam2017_app.views.assign_pcm.AssignPaper', name='paper_updating'),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
