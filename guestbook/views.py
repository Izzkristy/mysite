# coding:utf8
from django.views.generic import View
from django.template.response import TemplateResponse
from .models import Guestbook
import math
from django.http import JsonResponse
from datetime import datetime


# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        template = 'index.html'
        try:
            page = int(request.GET.get('p', 1))
        except:
            page = 1
        if page < 1:
            page = 1
        limit = 5
        offset = (page - 1) * limit
        content = {}
        result = []
        q = Guestbook.objects.all()
        count = q.count()
        guestbooks = q.order_by('-id')[offset:offset+limit]
        for guestbook in guestbooks:
            result.append(guestbook)
        content['message'] = result
        content['count'] = count
        content['range'] = range(1, math.ceil(count/limit)+1)
        content['page'] = page
        return TemplateResponse(request, template, content)

    def post(self, request, *args, **kwargs):
        template = 'submit.html'
        try:
            nickname = request.POST['nickname']
            email = request.POST['email']
            content = request.POST['content']
            clientip = request.META.get('REMOTE_ADDR')
            face = request.POST['face']

            guestbook = Guestbook()
            guestbook.nickname = nickname
            guestbook.face = face
            guestbook.content = content
            guestbook.clientip = clientip
            guestbook.email = email
            guestbook.save()
            return TemplateResponse(request, template, {'msg': '留言成功！非常感谢您的留言。'})
        except Exception as e:
            msg = '%s，留言失败' % e
            return TemplateResponse(request, template, {'msg': msg})
