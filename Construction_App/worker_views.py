from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from Construction_App.models import Request, worker_Registration, Contractor_Registration, feedback


class IndexView(TemplateView):
    template_name = 'worker/index.html'

class view_Request(TemplateView):
    template_name = 'worker/view_request.html'
    def get_context_data(self, **kwargs):

        context = super(view_Request, self).get_context_data(**kwargs)


        worker = worker_Registration.objects.get(user_id=self.request.user.id)

        wor = Request.objects.filter(worker_id=worker.id,status='sent')
        context['wor'] = wor
        return context

class Approve_Request(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        id2 = self.request.GET['id2']
        aa = worker_Registration.objects.get(pk=id2)
        aa.status = 'Unavailable'
        aa.save()
        accept = Request.objects.get(pk=id)
        accept.status = 'Accept'
        accept.status1='unavailable'
        accept.save()
        return render(request, 'worker/index.html', {'message': "Approve"})


class Reject_Request(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        id2 = self.request.GET['id2']
        aa = worker_Registration.objects.get(pk=id2)
        aa.status = 'Available'
        aa.save()
        accept = Request.objects.get(pk=id)
        accept.status = 'Reject'
        accept.status1='available'
        accept.save()
        return render(request, 'worker/index.html', {'message': "Reject"})

class add_feedback(TemplateView):
    template_name = 'worker/worker_reg.html'
    def get_context_data(self, **kwargs):

        context = super(add_feedback, self).get_context_data(**kwargs)

        worker = worker_Registration.objects.get(user_id=self.request.user.id)

        wor = Request.objects.filter(worker_id=worker.id)

        context['wor'] = wor
        return context

    def post(self, request, *args, **kwargs):
        won = worker_Registration.objects.get(user_id=self.request.user.id)
        con = request.POST['con']

        feed = request.POST['feed']
        act = feedback()
        act.contractor_id = con
        act.worker_id = won.id
        act.feedback=feed
        act.save()
        return render(request, 'worker/index.html', {'message': "Feedback"})

class reply(TemplateView):
    template_name = 'worker/worker_feedback.html'
    def get_context_data(self, **kwargs):

        context = super(reply, self).get_context_data(**kwargs)


        worker = worker_Registration.objects.get(user_id=self.request.user.id)

        wor = feedback.objects.filter(worker_id=worker.id)
        context['wor'] = wor
        return context

class my_work(TemplateView):
    template_name = 'worker/my_work.html'
    def get_context_data(self, **kwargs):

        context = super(my_work, self).get_context_data(**kwargs)


        worker = worker_Registration.objects.get(user_id=self.request.user.id)

        wor = Request.objects.filter(worker_id=worker.id,status1='unavailable')
        context['wor'] = wor
        return context

class complete(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        id2 = self.request.GET['id2']
        accept = Request.objects.get(pk=id)
        aa=worker_Registration.objects.get(pk=id2)
        aa.status='Available'
        aa.save()
        accept.status1='Available'
        accept.save()
        return render(request, 'worker/index.html', {'message': "Work Completed"})