from django.urls import path

from Construction_App.admin_views import IndexView, Add_Category, contractor_varifiction, ApproveView, RejectView, \
    Worker_varifiction, view_workers, view_blacklist, Delete_aacount, view_feed, view_feed_con, view_work, delete,Workerview,contractor_views

urlpatterns = [

    path('',IndexView.as_view(),name='index'),
    path('Category',Add_Category.as_view()),
    path('con', contractor_varifiction.as_view()),
    path('approve', ApproveView.as_view()),
    path('reject',RejectView.as_view()),
    path('wor', Worker_varifiction.as_view()),
    path('view_workers',view_workers.as_view()),
    path('view_blacklist',view_blacklist.as_view()),
    path('Delete_aacount',Delete_aacount.as_view()),
    path('view_feed',view_feed.as_view()),
    path('view_feed_con',view_feed_con.as_view()),
    path('view_work', view_work.as_view()),
    path('delete',delete.as_view()),
    path('Workerview',Workerview.as_view()),
    path('contractor_views',contractor_views.as_view())

]

def urls():
    return urlpatterns, 'admin','admin'
