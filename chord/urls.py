from django.urls import path
from . import views

urlpatterns = [
    path('api/',views.api.as_view(),name='api')
]