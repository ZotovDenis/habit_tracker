from rest_framework.pagination import PageNumberPagination


class PagePagination(PageNumberPagination):
    """
    Необходимо выводить 5 привычек на странице
    """
    page_size = 5
