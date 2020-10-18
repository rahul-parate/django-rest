

from django.urls import include, path

from rest_framework import routers
from initial_app import views

from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),

    url(r'rahul/',views.DummyClass.as_view(),name='rahul'),
    url(r'register/', views.Registration.as_view(), name='registration'),
]
