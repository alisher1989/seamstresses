from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from webapp.models import Seamstress


class ListView(View):
    def get(self, request, *args, **kwargs):
        queryset = Seamstress.objects.all()
        paginator = Paginator(queryset, 8)
        page_num = request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'index.html', context={'page': page})

