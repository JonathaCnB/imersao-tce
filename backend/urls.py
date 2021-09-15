from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from schedule import viewset as sc
from services import viewset as s
from users import viewsets as v

router = routers.DefaultRouter()
router.register(r"users", v.ListUserViewSet, basename="User")
router.register(r"services", s.ServiceViewSet, basename="Service")
router.register(r"schedule", sc.ScheduleViewSet)
router.register(r"review", sc.ReviewViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/users/", include("users.urls")),
]
