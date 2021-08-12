import django_filters
from timeline.comments.models import Comment


class CommentFilter(django_filters.FilterSet):
    post_id = django_filters.NumberFilter(required=True, )

    class Meta:
        model = Comment
        fields = ['user']
