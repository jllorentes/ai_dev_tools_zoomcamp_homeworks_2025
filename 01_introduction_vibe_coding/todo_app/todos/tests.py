from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoTests(TestCase):
    def setUp(self):
        # Creamos una tarea inicial para usarla en los tests de lectura/edición
        self.todo = Todo.objects.create(
            title="Tarea de prueba",
            description="Descripción inicial"
        )

    def test_todo_content(self):
        # Verificamos que el modelo guarda los datos correctamente
        self.assertEqual(self.todo.title, "Tarea de prueba")
        self.assertEqual(self.todo.description, "Descripción inicial")
        self.assertEqual(str(self.todo), "Tarea de prueba")

    def test_todo_list_view(self):
        # Verificamos que la home carga y muestra la tarea
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tarea de prueba")
        self.assertTemplateUsed(response, 'todo_list.html')

    def test_todo_create_view(self):
        # Intentamos crear una nueva tarea vía formulario
        response = self.client.post(reverse('todo_create'), {
            'title': 'Nueva tarea desde test',
            'description': 'Probando creación',
        })
        # Debería redirigir (código 302) tras crearla
        self.assertEqual(response.status_code, 302)
        # Debería haber 2 tareas ahora (la del setUp + esta nueva)
        self.assertEqual(Todo.objects.count(), 2)

    def test_todo_update_view(self):
        # Intentamos editar la tarea existente para marcarla como resuelta
        response = self.client.post(reverse('todo_update', args=[self.todo.pk]), {
            'title': 'Tarea de prueba editada',
            'is_resolved': True
        })
        self.assertEqual(response.status_code, 302)
        
        # Recargamos la tarea desde la BD para ver si cambió
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Tarea de prueba editada')
        self.assertTrue(self.todo.is_resolved)

    def test_todo_delete_view(self):
        # Intentamos borrar la tarea
        response = self.client.post(reverse('todo_delete', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        # Debería haber 0 tareas
        self.assertEqual(Todo.objects.count(), 0)