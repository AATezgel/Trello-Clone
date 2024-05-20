from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from boards.views import BoardViewSet, ListViewSet, CardViewSet

router = DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'lists', ListViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
