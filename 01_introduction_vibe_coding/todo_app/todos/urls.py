from django.urls import path
from .views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    # La ruta vacía '' será nuestra página principal (la lista)
    path('', TodoListView.as_view(), name='todo_list'),
    
    # Rutas para acciones específicas
    path('create/', TodoCreateView.as_view(), name='todo_create'),
    
    # <int:pk> significa que esperamos el ID (Primary Key) de la tarea en la URL
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='todo_update'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='todo_delete'),
]