from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView

from Construction_App.models import Category, Contractor_Registration, worker_Registration, feedback, Blacklist_workers,con_feedback


class IndexView(TemplateView):
    template_name = 'admin/index.html'

class Add_Category(TemplateView):
    template_name = 'admin/work_category.html'
    def post(self, request, *args, **kwargs):
        category=request.POST['category']
        se=Category()
        se.category=category
        se.save()
        return render(request, 'admin/index.html', {'message': "category Added"})

class contractor_views(TemplateView):
    template_name = 'admin/view_contractors.html'

    def get_context_data(self, **kwargs):
        context = super(contractor_views,self).get_context_data(**kwargs)

        con = Contractor_Registration.objects.all()

        context['user'] = con
        return context


class contractor_varifiction(TemplateView):
    template_name = 'admin/contractor_varify.html'

    def get_context_data(self, **kwargs):
        context = super(contractor_varifiction,self).get_context_data(**kwargs)

        con = Contractor_Registration.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['user'] = con
        return context

class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/index.html',{'message':" Account Approved"})

class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        User.objects.get(pk=id).delete()
        return redirect('admin:index')
      
class delete(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        Category.objects.get(id=id).delete()

        return render(request, 'admin/index.html', {'message': " deleted"})

class Worker_varifiction(TemplateView):
    template_name = 'admin/worker_varify.html'

    def get_context_data(self, **kwargs):
        context = super(Worker_varifiction,self).get_context_data(**kwargs)

        con = worker_Registration.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['user'] = con
        return context


class Workerview(TemplateView):
    template_name = 'admin/view_worker.html'

    def get_context_data(self, **kwargs):
        context = super(Workerview,self).get_context_data(**kwargs)

        con = worker_Registration.objects.all()

        context['jj'] = con
        return context

class view_feed(TemplateView):
    template_name = 'admin/worker_feedback.html'
    def get_context_data(self, **kwargs):

        context = super(view_feed, self).get_context_data(**kwargs)

        wor = feedback.objects.all()
        context['pro'] = wor
        return context

class view_work(TemplateView):
    template_name = 'admin/view_works.html'
    def get_context_data(self, **kwargs):

        context = super(view_work, self).get_context_data(**kwargs)

        wor = Category.objects.all()
        context['pro'] = wor
        return context
class view_workers(TemplateView):
    template_name = 'admin/view_workers.html'
    def get_context_data(self, **kwargs):

        context = super(view_workers, self).get_context_data(**kwargs)

        wor = worker_Registration.objects.all()
        context['jj'] = wor
        return context


class view_blacklist(TemplateView):
    template_name = 'admin/view_black List_Detals.html'
    def get_context_data(self, **kwargs):

        context = super(view_blacklist, self).get_context_data(**kwargs)
        id = self.request.GET['id']
        wok = worker_Registration.objects.get(id=id)

        wor = Blacklist_workers.objects.filter(worker_id=id)
        context['p'] = wok
        context['pro'] = wor

        return context



class Delete_aacount(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        User.objects.get(pk=id).delete()
        return render(request, 'admin/index.html', {'message': "deleted"})

class view_feed(TemplateView):
    template_name = 'admin/worker_feedback.html'
    def get_context_data(self, **kwargs):

        context = super(view_feed, self).get_context_data(**kwargs)
        wor = feedback.objects.all()
        context['pro'] = wor
        return context

    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        feed = request.POST['action']
        act = feedback.objects.get(id=id)
        act.reply = feed
        act.save()
        return render(request, 'admin/index.html', {'message': "Feedback"})

class view_feed_con(TemplateView):
    template_name = 'admin/con_feedback.html'
    def get_context_data(self, **kwargs):

        context = super(view_feed_con, self).get_context_data(**kwargs)
        wor = con_feedback.objects.all()
        context['pro'] = wor
        return context

    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        feed = request.POST['action']
        act = con_feedback.objects.get(id=id)
        act.reply = feed
        act.save()
        return render(request, 'admin/index.html', {'message': "Feedback"})