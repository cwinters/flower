from tests.unit import AsyncHTTPTestCase


class HealthCheckTests(AsyncHTTPTestCase):
    def test_healthy(self):
        r = self.get('/health')
        self.assertEqual(200, r.code)
        self.assertTrue('Healthy!', str(r.body))
