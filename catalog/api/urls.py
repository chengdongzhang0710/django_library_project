from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet, BookViewSet

router = DefaultRouter()
app_name = 'catalog-api'

router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)

urlpatterns = router.urls
