from django_filters import FilterSet


class AuthorFilter:
    pass


class AuthorFilter(FilterSet):
    pass


class Meta:
    model = AuthorFilter
    fields = ['first_name', 'last_name']
