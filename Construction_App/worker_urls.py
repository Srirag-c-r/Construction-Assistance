from django.urls import path

from Construction_App.admin_views import view_work
from Construction_App.worker_views import IndexView, view_Request, Approve_Request, Reject_Request, add_feedback, reply, \
    my_work, complete

urlpatterns = [

    path('', IndexView.as_view()),
    path('view_Request',view_Request.as_view()),
    path('accept',Approve_Request.as_view()),
    path('reject',Reject_Request.as_view()),
    path('feedback_add',add_feedback.as_view()),
    path('reply',reply.as_view()),
    path('my_work',my_work.as_view()),
    path('complete',complete.as_view())


]


def urls():
    return urlpatterns, 'worker', 'worker'
