from django.shortcuts import render

from django.views.generic import TemplateView

class IndexView(TemplateView):
    '''トップページのビュー'''
    # index.htmlをレンダリングする
    template_name = 'index.html'
