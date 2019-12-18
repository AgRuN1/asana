from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import SimpleRouter
from . import views
from . import api

router = SimpleRouter()
router.register('api/tasks', api.TasksView, basename='tasks')
static = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('', views.index, name='index'),
    path('api', views.api, name='api'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
] + static + router.urls