from django.urls import path
from . import views

app_name='similar_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('matched_data', views.matched_data, name='matched_data'),
]