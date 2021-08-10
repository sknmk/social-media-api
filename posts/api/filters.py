import django_filters
from posts.models import Post


class PostFilter(django_filters.FilterSet):
    published = django_filters.BooleanFilter(field_name='published_date', label='is_published', lookup_expr='isnull')

    class Meta:
        model = Post
        fields = ['user']



