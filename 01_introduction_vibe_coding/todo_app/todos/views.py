from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Todo

# 1. Listar las tareas (Read)
class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todos'
    ordering = ['due_date'] # Ordenar por fecha de vencimiento

# 2. Crear una tarea (Create)
class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'description', 'due_date']
    template_name = 'todo_form.html'
    success_url = reverse_lazy('todo_list') # Redirigir a la lista al terminar

# 3. Editar una tarea (Update / Resolve)
class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'description', 'due_date', 'is_resolved']
    template_name = 'todo_form.html'
    success_url = reverse_lazy('todo_list')

# 4. Borrar una tarea (Delete)
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')