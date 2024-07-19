from django.urls import path

from Construction_App.contractor_views import IndexView, Search_Worker, Workers_list, Request_Status, view_feed, \
    add_feedback, add_blackList, reply

urlpatterns = [

    path('',IndexView.as_view()),
    path('Search_Worker',Search_Worker.as_view()),
    path('Workers',Workers_list.as_view()),
    path('Request_Status',Request_Status.as_view()),
    path('view_feed',view_feed.as_view()),
    path('add_feedback',add_feedback.as_view()),
    path('add_blackList',add_blackList.as_view()),
    path('reply',reply.as_view())

]
def urls():
    return urlpatterns, 'contractor','contractor'
