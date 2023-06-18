from django.urls import path
from .views import TokenCreateView, TokenListView, short_url_redirect, main_page

urlpatterns = [
    path('', main_page, name='main'),
    path('list', TokenListView.as_view(), name='token_list'),
    path('<str:short_url>', short_url_redirect, name='short_url_redirect'),
]

htmx_patterns = [
    path('/token_create', TokenCreateView.as_view(), name='token_create')
]

urlpatterns += htmx_patterns