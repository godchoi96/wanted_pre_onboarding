from django.urls import include, path

from api import views


api_name = 'api'
urlpatterns = [
    path('list/', views.APIListView.as_view(), name="list"),
]