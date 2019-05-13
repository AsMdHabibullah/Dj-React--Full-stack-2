from django.urls import path
from protfolio.views import IndexViews


urlpatterns = [
    path('', IndexViews, name='index'),
]

