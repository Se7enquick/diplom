from django.urls import path, include
from .views import TaskView, CreateTask, UpdateStatus, UpdateTaskArticle, UpdateTaskPerformer, DeleteTask 
from .api.routers import router
app_name = 'main'

urlpatterns = [       
    path('update/task/<int:pk>/status', UpdateStatus.as_view(), name='update_status'),
    path('add/', CreateTask.as_view(), name='create'),
    path('delete/task/<int:pk>', DeleteTask.as_view(), name='delete'),
    path('update/task/<int:pk>/article', UpdateTaskArticle.as_view(), name='update_article'),
    path('update/task/<int:pk>/performer', UpdateTaskPerformer.as_view(), name = 'upd_performer'),
    path('', TaskView.as_view(), name = 'index'),
    path('api/', include(router.urls)),
]


