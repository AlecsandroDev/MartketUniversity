# tests/test_base.py
import unittest
from app import create_app

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        """Configuração inicial para todos os testes"""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self):
        """Limpeza após cada teste"""
        pass