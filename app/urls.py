from django.urls import path
from . import views

urlpatterns = [
    path("customers-list/", views.CustomersListAPIViews.as_view())
]





