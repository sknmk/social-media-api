import django_filters
from timeline.posts.models import Post


class PostFilter(django_filters.FilterSet):
    only_following_users = django_filters.BooleanFilter(method='only_following_users_filter', label='Only Following '
                                                                                                    'Users')

    class Meta:
        model = Post
        fields = ['user']

    def only_following_users_filter(self, queryset, name, value):
        if value is True:
            return queryset.filter(**{'user__pk__in': self.request.user.user_follower.values_list('following')})
        return queryset
