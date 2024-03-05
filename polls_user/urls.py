from django.urls import path

from .user_views import *

urlpatterns = [
    path("user-list/", UserList.as_view(), name="user-list"),
    path("user-retrieve/<int:pk>/", UserRetrieve.as_view(), name="user-retrieve"),
    path("user-create/", UserCreate.as_view(), name="user-create"),
    path("user-update/<int:pk>/", UserUpdate.as_view(), name="user-update"),
    path("user-destroy/<int:pk>/", UserDestroy.as_view(), name="user-destroy"),
]
