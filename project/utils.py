from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .models import Project,Tags


def searchProject(request):
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tags.objects.filter(name__icontains = search_query)
    projects = Project.objects.filter(Q(title__icontains = search_query) | 
    Q(owner__name__icontains = search_query) |
    Q(tags__in = tags)).distinct()

    return search_query, projects


def paginateProject(request,projects,amount):

    page = request.GET.get('page')
    pagination = Paginator(projects, amount)
    try:
        projects = pagination.page(page)
    except PageNotAnInteger:
        page = 1
        projects = pagination.page(page)
    except EmptyPage:
        page = pagination.num_pages
        projects = pagination.page(page)

    leftIndex = int(page)-1
    if leftIndex <= 0:
        leftIndex = 1

    rightIndex = int(page) + 2
    if rightIndex > pagination.num_pages:
        rightIndex = pagination.num_pages+1

    custom_range = range(leftIndex,rightIndex)

    return custom_range,projects