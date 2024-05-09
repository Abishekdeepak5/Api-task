from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('',views.index,name='index'),
    
# ]