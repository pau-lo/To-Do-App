from django.urls import include, path
from . import views

urlpatterns = [
    # path('tasks/', include('tasks.urls')),
    path('', views.index, name='index'),
    # path('admin/', admin.site.urls),
]
