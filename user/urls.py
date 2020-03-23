from django.urls import path

from . views import *

urlpatterns = [
    path('signup/', UserListView.as_view(),name='signup'),

]
