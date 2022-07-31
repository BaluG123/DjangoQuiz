from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register('upscapi',views.Quiz_view,basename="upsc")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))    
]
