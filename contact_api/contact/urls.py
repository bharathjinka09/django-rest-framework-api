from rest_framework import routers
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register('contacts', views.ContactView)

urlpatterns = [
    path('',include(router.urls)),
    path('sentry-debug/', views.trigger_error),
    path('glitchtip-debug/', views.trigger_error),

]
