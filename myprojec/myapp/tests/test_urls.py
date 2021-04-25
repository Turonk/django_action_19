from django.test import Client, TestCase
from django.urls import reverse


class StaticPagesURLTests(TestCase):
    def setUp(self):
        # Создаем неавторизованый клиент
        self.guest_client = Client()

    def test_about_url_exists_at_desired_location(self):
        """Проверка доступности главной страницы."""
        response = self.guest_client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

# просто файл test.py и добавить еще 2 теста на неглавную страничку и контекст
# добавить тест на URL