import django_filters
from django_filters import CharFilter
from .models import Post


class PostFilter(django_filters.FilterSet):
    movie=CharFilter(field_name='movie',lookup_expr='icontains'),
    theater_location=CharFilter(field_name='theater_location',lookup_expr='icontains'),
    theater=CharFilter(field_name='theater',lookup_expr='icontains'),

    class Meta:
        model = Post
        fields =('tickets','language','movie','district','theater_location','theater')
