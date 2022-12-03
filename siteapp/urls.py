from django.urls import path
from .views import *

app_name = 'siteapp'
urlpatterns = [
    path('destination-area/<int:destareaid>/sites', 
        sites, name='site_list'),
    path('destination-area/<int:destareaid>/sites/<int:siteid>', 
        site_detail, name='site_detail'),
    path('destination-area/<int:destareaid>/sites/<int:siteid>/add-review', 
        add_site_review, name='site_review'),
]