from django.urls import path
from .views import TokenCreateView, TokenListView, short_url_redirect

urlpatterns = [
    path('', TokenCreateView.as_view(), name='token_create'),
    path('list/', TokenListView.as_view(), name='token_list'),
    path('<str:short_url>/', short_url_redirect, name='short_url_redirect'),
]
