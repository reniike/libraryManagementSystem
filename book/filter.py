from django_filters import FilterSet


class AuthorFilter(FilterSet):
class Meta:
        model = AuthorFilter
        fields = ['first_name', 'last_name']