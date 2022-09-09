from django.shortcuts import render
from rest_framework import pagination, viewsets

from api.serializers import SeamstressSerializer
from webapp.models import Seamstress


class PaginationMainPage(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'


class SeamstressViewSet(viewsets.ModelViewSet):
    """Список швей"""
    queryset = Seamstress.objects.all()
    serializer_class = SeamstressSerializer
    pagination_class = PaginationMainPage
