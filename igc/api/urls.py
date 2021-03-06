from django.conf.urls import url

from .views import FellowList, FellowDetail, PublicationDetail, PublicationList

fellow_detail = FellowDetail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

publications_detail = PublicationDetail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^$', FellowList.as_view()),
    url(r'^(?P<user__slug>[\w-]+)/publications/(?P<pk>[0-9]+)/$', publications_detail),
    url(r'^(?P<user__slug>[\w-]+)/publications/$', PublicationList.as_view()),
    url(r'^(?P<user__slug>[\w-]+)/$', fellow_detail),
]
