from django.urls import path 
from .views import ListaTarefasAPIView
from .views import ContagemTarefasAPIView
# Namespace do app (útil para reverse()) 
app_name = 'core' 
urlpatterns = [ 
# /api/tarefas/ → ListaTarefasAPIView 
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/contagem/', ContagemTarefasAPIView.as_view(), name='contagem-tarefas'),
]