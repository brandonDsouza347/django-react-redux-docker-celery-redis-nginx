from django.urls import path

from .views import (ListAgentsPropertiesAPIView, ListAllPropertiesAPIView,
                    PropertyDetailView, PropertySearchAPIView,
                    create_property_api_view, delete_property_api_view,
                    update_property_api_view)

urlpatterns = [
    path("all/", ListAllPropertiesAPIView.as_view(), name="all_properties"),
    path("agents/", ListAgentsPropertiesAPIView.as_view(), name="agents-properties"),
    path("create/", create_property_api_view, name="property-create"),
    path("details/<slug:slug>/", PropertyDetailView.as_view(), name="property-details"),
    path("update/<slug:slug>/", update_property_api_view, name="update-property-api"),
    path("delete/<slug:slug>/", delete_property_api_view, name="delete-property"),
    path("search/", PropertySearchAPIView.as_view(), name="property-search"),
]
