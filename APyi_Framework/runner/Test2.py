import xlrd
import json
import requests
import pytest
from apyifunctions import petstore3
response_cap=[]

@pytest.mark.run(order=1)
def test_create():
        response=petstore3.methodForPost('wt','create')
        a=petstore3.verifyResponse(response, 'http://192.168.0.155:3334/workstationType/createWorkstationType','wt','create')

@pytest.mark.run(order=3)
def test_update():
    petstore3.verifyResponse(petstore3.upmethodForPost('upwt','create',response_cap), "http://192.168.0.155:3334/workstationType/updateWorkstationType",'upwt','create')
        
        
    