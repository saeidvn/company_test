import unittest
import json
import http.client
import requests
from requests import status_codes
from requests.api import delete, get
import random

class TestStringMethods(unittest.TestCase):

    def test_createPet(self):
        # Enter Data
        print("create")

        petData = {
            "id": 1000,
            "category": {
                "id": 2000,
                "name": "bulldog"
            },
            "name": "bonnie",
            "tags": [
                {
                    "id": 3000,
                    "name": "black"
                },
                {
                    "id": 4000,
                    "name": "female" 
                }
            ],
            "status": "available"
        }
        
        # Request
        baseUrl = "https://petstore.swagger.io/v2"
        response = requests.post(baseUrl+"/pet", json=petData)

        # TestPass 
        self.assertEqual(response.status_code, 200)

    def test_findPet(self):
        # Enter Data
        print("find")

        petData = {
            "id": 1000,
            "category": {
                "id": 2000,
                "name": "bulldog"
            },
            "name": "bonnie",
            "tags": [
                {
                    "id": 3000,
                    "name": "black"
                },
                {
                    "id": 4000,
                    "name": "female" 
                }
            ],
            "status": "available"
        }
        
        # Request
        baseUrl = "https://petstore.swagger.io/v2"
        response = requests.get(baseUrl+"/pet/1000", json=petData)
        
        # TestPass 
        self.assertEqual(response.status_code, 200)

    def test_updatePet(self):
        # Enter Data
        print("update")

        petData = {
            "id": 1000,
            "category": {
                "id": 2000,
                "name": "bulldog"
            },
            "name": "bonnie",
            "tags": [
                {
                    "id": 3000,
                    "name": "black"
                },
                {
                    "id": 4000,
                    "name": "female" 
                }
            ],
            "status": "available"
        }
        
        # Request
        baseUrl = "https://petstore.swagger.io/v2"
        response = requests.put(baseUrl+"/pet", json=petData)

        # TestPass 
        self.assertEqual(response.status_code, 200)

    # I didn't know how to run tests in order and had to add Z to make it alphabetical
    def test_z_deletePet(self):
        # Enter Data
        print("delete")
        
        petData = {
            "id": 1000
        }
        
        # Request
        baseUrl = "https://petstore.swagger.io/v2"

        response = requests.delete(baseUrl+"/pet/1000", json=petData)

        # TestPass 
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()