import xlrd
import json
import requests
import pytest
from apyifunctions import petstore3
resbody=''
p=[{"name": "ismart"}, {"name": "oversamart"},{"name": "lafoot"}]
'''@pytest.mark.run(order=1)
def test_create():
        response=petstore3.methodForPost('pet','abd')
        resbody=petstore3.upverifyResponse(response, "https://petstore.swagger.io/v2/pet",'pet','abd')
        #petstore3.verres(resbody,'pet','abd')

@pytest.mark.run(order=2)
def test_update():
    petstore3.verifyResponse(petstore3.upmethodForPost('pat','abd',resbody), "https://petstore.swagger.io/v2/pet",'pet','abd')
        
        
        #response=petstore3.upmethodForPost('pet','abd',p)
        #petstore3.upverifyResponse(response, "http://192.168.0.155:3337/order-management-service/getMoByNumber",'mo','abd')'''
    


@pytest.mark.run(order=1)
def test_create():
        response=petstore3.methodForPost('wt','create')
        resbody=petstore3.upverifyResponse(response, 'http://192.168.0.155:3334/workstationType/createWorkstationType','wt','create')


@pytest.mark.run(order=3)
def test_update():
    petstore3.verifyResponse(petstore3.upmethodForPost('upwt','create',resbody), "http://192.168.0.155:3334/workstationType/updateWorkstationType",'upwt','create')
        
        
    