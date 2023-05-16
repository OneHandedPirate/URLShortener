from django.urls import path
from .views import CreateListViewSet


urlpatterns = [
    path('v1/token_create/', CreateListViewSet.as_view({'post': 'create'})),
    path('v1/token_list/', CreateListViewSet.as_view({'get': 'list'}))
]
