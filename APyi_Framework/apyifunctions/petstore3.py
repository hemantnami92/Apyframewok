import xlrd
import json
import requests
from json import loads
from pathlib import WindowsPath 
import os
from pathlib import Path
#url="https://petstore.swagger.io/v2/pet"
headers={'Content-type':'application/json', 'Accept':'application/json'}
dir_name='./datafiles/'
js = '.json'
xl='.xlsx'
add=()
def methodForPost(filename,sheetname):
    #print('../datafiles/'+filename+'.xlsx')
    wb = xlrd.open_workbook(os.path.join(dir_name, filename + xl)) 
    sheet = wb.sheet_by_name(sheetname) 
    sheet.cell_value(0, 1)
    for i in range(1,sheet.nrows):
        test_data=sheet.cell_value(i, 5)
        lookup=eval(test_data)
        with open(os.path.join(dir_name, filename + js),'r') as f1:
            read_json=json.load(f1)
            read_json.update(lookup)
            #print(read_json)
            #yield read_json
            #for read_json in methodForPost:
            request_json=json.dumps(read_json)
            yield request_json
            '''print(request_json)
            response=requests.post(url,request_json,headers=headers)
            print(response)
            assert response.status_code==200
            #yield response
            #yield response '''

def upmethodForPost(filename,sheetname,add):
    wb = xlrd.open_workbook(os.path.join(dir_name, filename + xl)) 
    sheet = wb.sheet_by_name(sheetname) 
    sheet.cell_value(0, 1)
    for i in range(1,sheet.nrows):
        test_data=sheet.cell_value(i, 5)
        lookup=eval(test_data)
        with open(os.path.join(dir_name, filename + js),'r') as f1:
            read_json=json.load(f1)
            read_json.update(lookup)
            read_json.update(add)
            request_json=json.dumps(read_json)
            yield request_json


    
def expectedres(filename,sheetname):
     wb = xlrd.open_workbook(os.path.join(dir_name, filename + xl)) 
     sheet = wb.sheet_by_name(sheetname) 
     sheet.cell_value(0, 1)
     for i in range(1,sheet.nrows):
        test_data=sheet.cell_value(i, 6)
        lop=int(test_data)
        print( lop)
        yield lop




def verifyResponse(response,url,filename,sheetname):
    for i in response:
        
#    for  i in methodForPost(filename,sheetname):
        #print(i)
        response=requests.post(url,i,headers=headers)
        

        #yield response
        #print(response)
        #assert response.status_code==200
    for expectedresult in expectedres(filename,sheetname):
        response_body = response.json()
        #assert response_body["moNumber"] ==expectedresult, "verificatio of status code got failed and response is code is"

        assert response.status_code==expectedresult, "verificatio of status code got failed and response is code is"
        
        
def upverifyResponse(response,url,filename,sheetname):
    for i in response:
        
#    for  i in methodForPost(filename,sheetname):
        #print(i)
        response=requests.post(url,i)
        yield response
        #response_body = response.json()
        #yield response
        #print(response)
        #assert response.status_code==200
def verres(response,filename,sheetname):
    
    for expectedresult in expectedres(filename,sheetname):
        #assert response.status_code==expectedresult, "verificatio of status code got failed and response is code is" 
        assert response["internalMessage"] ==eval(expectedresult), "verificatio of status code got failed and response is code is"

    
