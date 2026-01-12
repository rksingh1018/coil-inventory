from rest_framework.routers import DefaultRouter
from .views import CoilViewSet

router = DefaultRouter()
router.register('coils', CoilViewSet)

urlpatterns = router.urls
