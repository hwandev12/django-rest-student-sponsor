from unicodedata import name
from .models import Sponsor, Student
from .serializers import StudentSerializer, UserSerializer, SponsorSerializer
from rest_framework import permissions, renderers, viewsets, generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination

from django.db.models import Count

# django filters
from django_filters import rest_framework as filter


# for caches
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers


User = get_user_model()

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'students':   reverse('student-list', request=request, format=format),
        'users':   reverse('user-list', request=request, format=format),
        'sponsors': reverse('sponsor-list', request=request, format=format),
        'filter': reverse('filter-users', request=request, format=format)
    })
    
    
# for pagination change resolution
class SmallResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10000
    
    
# Customize filters
class StudentFilter(filter.FilterSet):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']
        
# user filter
class UserFilter(filter.FilterSet):
    class Meta:
        model = User
        fields = {
            'username': ['exact', 'contains'],
            'last_login': ['exact', 'year__gt'],
        }

# sponsor filter
class SponsorFilter(filter.FilterSet):
    class Meta:
        model = Sponsor
        fields = ['first_name', 'last_name', 'students__first_name']

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # filterset_fields = ['first_name', 'last_name'] this is for filtering per given names
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['first_name', 'last_name', 'specification']
    filterset_class = StudentFilter
    pagination_class = SmallResultsSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

        
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # filterset_fields = ['username', 'email'] # default filter view
    filterset_class = UserFilter    
    pagination_class = SmallResultsSetPagination
        

class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['first_name', 'students__first_name'] # this is for nested manytomany fields search filter
    filterset_class = SponsorFilter
    pagination_class = SmallResultsSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class FilterPerUserProduction(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(owner=user)


    