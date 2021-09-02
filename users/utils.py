from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .models import Profile,Skills


def searchProfiles(request):
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skills.objects.filter(name__icontains = search_query)
    profiles = Profile.objects.filter(Q(name__icontains = search_query) |
    Q(short_intro__icontains = search_query) | Q(skills__in = skills)).distinct()

    return search_query, profiles

def paginateDevs(request,profiles,amount):

    page = request.GET.get('page')
    pagination = Paginator(profiles, amount)
    try:
        profiles = pagination.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = pagination.page(page)
    except EmptyPage:
        page = pagination.num_pages
        profiles = pagination.page(page)

    leftIndex = int(page)-1
    if leftIndex <= 0:
        leftIndex = 1

    rightIndex = int(page) + 2
    if rightIndex > pagination.num_pages:
        rightIndex = pagination.num_pages+1

    custom_range = range(leftIndex,rightIndex)

    return custom_range,profiles