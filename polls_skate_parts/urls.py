from django.urls import path

from .views import shape_view, wheels_view, truck_view, bearing_view

urlpatterns = [
    path("shape-list/", shape_view.ShapeList.as_view(), name="shape-list"),
    path("shape-create/", shape_view.ShapeCreate.as_view(), name="shape-create"),
    path("shape-retrieve/<int:pk>/", shape_view.ShapeRetrieve.as_view(), name="shape-retrieve"),
    path("shape-update/<int:pk>/", shape_view.ShapeUpdate.as_view(), name="shape-update"),
    path("shape-destroy/<int:pk>/", shape_view.ShapeDestroy.as_view(), name="shape-destroy"),

    path("truck-list/", truck_view.TruckList.as_view(), name="truck-list"),
    path("truck-create/", truck_view.TruckCreate.as_view(), name="truck-create"),
    path("truck-retrieve/<int:pk>/", truck_view.TruckRetrieve.as_view(), name="truck-retrieve"),
    path("truck-update/<int:pk>/", truck_view.TruckUpdate.as_view(), name="truck-update"),
    path("truck-destroy/<int:pk>/", truck_view.TruckDestroy.as_view(), name="truck-destroy"),

    path("wheels-list/", wheels_view.WheelsList.as_view(), name="wheels-list"),
    path("wheels-create/", wheels_view.WheelsCreate.as_view(), name="wheels-create"),
    path("wheels-retrieve/<int:pk>/", wheels_view.WheelsRetrieve.as_view(), name="wheels-retrieve"),
    path("wheels-update/<int:pk>/", wheels_view.WheelsUpdate.as_view(), name="wheels-update"),
    path("wheels-destroy/<int:pk>/", wheels_view.WheelsDestroy.as_view(), name="wheels-destroy"),

    path("bearing-list/", bearing_view.BearingList.as_view(), name="bearing-list"),
    path("bearing-create/", bearing_view.BearingCreate.as_view(), name="bearing-create"),
    path("bearing-retrieve/<int:pk>/", bearing_view.BearingRetrieve.as_view(), name="bearing-retrieve"),
    path("bearing-update/<int:pk>/", bearing_view.BearingUpdate.as_view(), name="bearing-update"),
    path("bearing-destroy/<int:pk>/", bearing_view.BearingDestroy.as_view(), name="bearing-destroy"),
]
