from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import user_views, tags_views

app_name = 'user'


router = DefaultRouter()
router.register('tags', tags_views.TagViewSet)


urlpatterns = [
    path('create/', user_views.CreateUserView.as_view(), name='create'),
    path('token/', user_views.CreateTokenView.as_view(), name='token'),
    path('me/', user_views.ManageUserView.as_view(), name='me'),
    path('', include(router.urls))
]