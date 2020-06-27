import xlrd
import json
import requests
import pytest
from apyifunctions import petstore3
response=[]
@pytest.mark.run(order=1)
def test_create():
        response=petstore3.methodForPost('pet','abd')
        petstore3.verifyResponse(response, "https://petstore.swagger.io/v2/pet",'pet','abd')

@pytest.mark.run(order=2)
def test_update():
    petstore3.verifyResponse(petstore3.upmethodForPost('pat','abd',response), "https://petstore.swagger.io/v2/pet",'pet','abd')
        
        
       
    


