import unittest
from app import app

class ApiTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_demandas_returns_list(self):
        response = self.client.get("/api/demandas")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)
        self.assertGreater(len(response.get_json()), 0)

    def test_filter_by_area(self):
        response = self.client.get("/api/demandas?area=Dados")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(all(x["area"] == "Dados" for x in response.get_json()))

if __name__ == "__main__":
    unittest.main()
