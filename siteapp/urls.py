from django.urls import path
from .views import *

app_name = 'accommodation'
urlpatterns = [
    path('destination-area/<int:destareaid>/sites', 
        sites, name='accommodation_list'),
    path('destination-area/<int:destareaid>/sites/<int:accommid>', 
        sites, name='accommodation_detail'),
    path('destination-area/<int:destareaid>/sites/<int:accommid>/add-review', 
        sites, name='add_accommodation_review'),
]