import unittest
from urllib import response
import requests

class Testrotas(unittest.TestCase):
    
    #rota users?nome com parâmetro
    def teste_get_notoken_param_name_user(self):
        self.response = requests.get('http://127.0.0.1:5000/users?nome=Kurtis')
        self.assertEqual(401, self.response.status_code)
    def teste_get_token_param_name_user(self):
        self.response = requests.get('http://127.0.0.1:5000/users?nome=Kurtis', headers={"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NSwiZXhwIjoxNjYzNTI5NTE2fQ.b3WVXZccuoV7gWduxjI4bvbukL9vwVMIat32423423"})
        self.assertEqual(200, self.response.status_code)
    def teste_notfound_param_name_user(self):
         self.response = requests.get('http://127.0.0.1:5000/users?nome=teste', headers={"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NSwiZXhwIjoxNjYzNTI5NTE2fQ.b3WVXZccuoV7gWduxjI4bvbukL9vwVMIat32423423"})
         self.assertEqual(404, self.response.status_code)
    
    #rota users/website
    def teste_get_notoken_website(self):
        self.response = requests.get('http://127.0.0.1:5000/users/website')
        self.assertEqual(401, self.response.status_code)
    def teste_get_token_website(self):
        self.response = requests.get('http://127.0.0.1:5000/users/website', headers={"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NSwiZXhwIjoxNjYzNTI5NTE2fQ.b3WVXZccuoV7gWduxjI4bvbukL9vwVMIat32423423"} )
        self.assertEqual(200, self.response.status_code)

    #rota users/details
    def teste_get_notoken_details(self):
        self.response = requests.get('http://127.0.0.1:5000/users/detail')
        self.assertEqual(401, self.response.status_code)
    def teste_get_token_details(self):
        self.response = requests.get('http://127.0.0.1:5000/users/detail',  headers={"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NSwiZXhwIjoxNjYzNTI5NTE2fQ.b3WVXZccuoV7gWduxjI4bvbukL9vwVMIat32423423"})
        self.assertEqual(200, self.response.status_code)

if __name__ == "__main__":
    unittest.main()