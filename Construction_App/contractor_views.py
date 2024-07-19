from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from Construction_App.models import Category, worker_Registration, Contractor_Registration, Request, feedback, \
    con_feedback, Blacklist_workers


class IndexView(TemplateView):
    template_name = 'contractor/index.html'

class Search_Worker(TemplateView):
    template_name = 'contractor/seach_workers.html'

    def get_context_data(self, **kwargs):
        pro = Category.objects.all()
        context = {
            'pro': pro,
        }
        return context


class Workers_list(TemplateView):
    template_name = 'contractor/workers.html'


    def get_context_data(self, **kwargs):

        context = super(Workers_list, self).get_context_data(**kwargs)

        id =self.request.GET['id']


        wor = worker_Registration.objects.filter(category_id=id)
        context['wor'] = wor
        return context

    def post(self, request, *args, **kwargs):
        con = Contractor_Registration.objects.get(user_id=self.request.user.id)
        id = request.POST['id']

        action = request.POST['action']
        if Request.objects.filter(worker_id=id,status1='unavailable'):
            return render(request, 'contractor/index.html', {'message': "Already Added"})
        else:
            act = Request()
            act.contractor_id = con.id
            act.worker_id = id
            act.message = action
            act.status = 'sent'
            act.status1='null'
            act.save()
            return render(request, 'contractor/index.html', {'message': "Request Sent"})


class Request_Status(TemplateView):
    template_name = 'contractor/request_status.html'
    def get_context_data(self, **kwargs):

        context = super(Request_Status, self).get_context_data(**kwargs)


        con = Contractor_Registration.objects.get(user_id=self.request.user.id)

        wor = Request.objects.filter(contractor_id=con.id)
        context['wor'] = wor
        return context

class view_feed(TemplateView):
    template_name = 'contractor/feedback.html'
    def get_context_data(self, **kwargs):

        context = super(view_feed, self).get_context_data(**kwargs)


        con = Contractor_Registration.objects.get(user_id=self.request.user.id)

        wor = feedback.objects.filter(contractor_id=con.id)
        context['pro'] = wor
        return context
class add_feedback(TemplateView):
    template_name = 'contractor/con_feedback.html'
    def get_context_data(self, **kwargs):

        context = super(add_feedback, self).get_context_data(**kwargs)

        worker = Contractor_Registration.objects.get(user_id=self.request.user.id)

        wor = Request.objects.filter(contractor_id=worker.id)

        context['wor'] = wor
        return context

    def post(self, request, *args, **kwargs):
        won = Contractor_Registration.objects.get(user_id=self.request.user.id)
        con = request.POST['con']

        feed = request.POST['feed']
        act = con_feedback()
        act.contractor_id = won.id
        act.worker_id = con
        act.feedback=feed
        act.save()
        return render(request, 'contractor/index.html', {'message': "Feedback"})


class add_blackList(TemplateView):
    template_name = 'contractor/black_list.html'
    def get_context_data(self, **kwargs):

        context = super(add_blackList, self).get_context_data(**kwargs)

        worker = Contractor_Registration.objects.get(user_id=self.request.user.id)

        wor = Request.objects.filter(contractor_id=worker.id)

        context['wor'] = wor
        return context

    def post(self, request, *args, **kwargs):
        won = Contractor_Registration.objects.get(user_id=self.request.user.id)
        con = request.POST['con']

        feed = request.POST['reason']
        act = Blacklist_workers()
        act.contractor_id = won.id
        act.worker_id = con
        act.reason=feed
        act.count=+1
        act.save()
        return render(request, 'contractor/index.html', {'message': "Black Listed"})


class reply(TemplateView):
    template_name = 'contractor/con_feed_reply.html'
    def get_context_data(self, **kwargs):

        context = super(reply, self).get_context_data(**kwargs)


        worker = Contractor_Registration.objects.get(user_id=self.request.user.id)

        wor = con_feedback.objects.filter(contractor_id=worker.id)
        context['wor'] = wor
        return context
