from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

# Create your tests here.
class LaboratorioTest(TestCase):
    databases = '__all__'
    @classmethod

    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(nombre='Laboratorio9', ciudad='Ciudad9', pais='Pais9')

    def test_model_content(self):
        self.assertEqual(self.laboratorio.nombre, 'Laboratorio9')
        self.assertEqual(self.laboratorio.ciudad, 'Ciudad9')
        self.assertEqual(self.laboratorio.pais, 'Pais9')

    def test_url_exists_at_correct_location(self):
        response = self.client.get('/laboratorio/mostrar/')
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse('mostrar_laboratorio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio/index.html')
        self.assertContains(response, 'Información de los Laboratorios')