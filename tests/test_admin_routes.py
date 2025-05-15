from tests.test_base import BaseTestCase
from os import getenv as env

class TestPageAdminRoutes(BaseTestCase):
  def test_admin_load_page_status(self):
    response = self.client.get('/admin', follow_redirects=True)
    self.assertEqual(response.status_code, 200)

  def test_admin_acess_page_succefuly(self):
    payload = {
      'username': env('USERNAME_TEST'),
      'password': env('PASSWORD_TES')
    }

    response = self.client.post('/admin-form', data=payload)

    self.assertEqual(response.status_code, 302)


  def test_admin_acess_page_failed(self):
    payload = {
     'username': 'random',
     'password': 'random'
    }

    response = self.client.post('/admin-form', data=payload)

    self.assertEqual(response.status_code, 302)


  def test_admin_access_dashboard_without_login(self):
    response = self.client.get('/admin/dashboard')
    self.assertEqual(response.status_code, 302)
    self.assertIn('/admin', response.headers['Location'])


  def test_admin_acess_dashboard_acess(self):
    with self.client as c:
        with c.session_transaction() as sess:
            sess['username'] = 'admin'
        response = c.get('/admin/dashboard')
        self.assertEqual(response.status_code, 200)
  
  def test_admin_logout_route(self):
     with self.client as c:
        with c.session_transaction() as sess:
           sess['username'] = 'admin'
        response = c.get('/admin/dashboard')
        status_code_logon = response.status_code
        response = c.post('/logout')
        status_code_logout = response.status_code
        self.assertNotEqual(status_code_logon, status_code_logout)
  
  def test_admin_request_sql_users(self):
    with self.client as c:
        with c.session_transaction() as sess:
            sess['username'] = 'admin'
        response = c.get('/users')
        self.assertEqual(response.status_code, 200)

  def test_admin_request_sql_products(self):
    with self.client as c:
        with c.session_transaction() as sess:
            sess['username'] = 'admin'
        response = c.get('/products')
        self.assertEqual(response.status_code, 200)
  
  def test_admin_request_sql_reports(self):
    with self.client as c:
        with c.session_transaction() as sess:
            sess['username'] = 'admin'
        response = c.get('/reports')
        self.assertEqual(response.status_code, 200)

  def test_admin_request_sql_manage_users(self):
    with self.client as c:
        with c.session_transaction() as sess:
            sess['username'] = 'admin'
        response = c.get('/admin/dashboard/users/manage_users/1')
        self.assertEqual(response.status_code, 200)

    
  def test_admin_request_sql_manage_users(self):
    with self.client as c:
        with c.session_transaction() as sess:
            sess['username'] = 'admin'
        payload = {
          'id': 1,
          'nome': 'random',
          'email': 'random',
          'telefone': 'random',
          'cidade': 'random',
          'estado': 'random',
          'idade': 1,
        }

        response = c.post('/update_user', data=payload)
        self.assertEqual(response.status_code, 200)

