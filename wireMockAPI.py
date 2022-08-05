# 1 - Baixar Wiremock Standalone.
# 2 - Abrir Git Bash e executar o arquivo .jar baixado com o seguinte comando:
#       >> java -jar wiremock-jre8-standalone-2.33.2.jar

import requests
import json
from requests.structures        import CaseInsensitiveDict

def testJsonFile():
    with open(r'./GitHub/Wiremock-Standalone-MockAPI/_jarStandalone/idreq_2980.json', 'r') as file:
        parseJson = json.load(file)
        return json.dumps(parseJson)

def createMock():
    URL = 'http://localhost:8080/__admin/mappings/new'

    headers = CaseInsensitiveDict()
    headers['Content/Type'] = 'apllication/json'

    #jsonData = testJsonFile()

    #data = r'{ "request": { "url": "/get/this", "method": "GET" }, "response": { "status": 200, "bodyFileName": "' + f'{jsonData}' + '"}}'
    data = r'{ "request": { "url": "/get/this", "method": "GET" }, "response": { "status": 200, "bodyFileName": "/idreq.json" }}'
    #data = r'{ "request": { "url": "/get/this", "method": "GET" }, "response": { "status": 200, "body": "Here it is!\n" }}'

    resp = requests.post(url=URL, data=data)

    print(f' Status code: {resp.status_code} \n request: {resp.request} \n Aparent encoding: {resp.apparent_encoding} \n Encoding: {resp.encoding} \n Content: {resp.content} \n Cookies: {resp.cookies} \n Elapsed: {resp.elapsed} \n' +
           f' Headers: {resp.headers} \n History: {resp.history} \n RAW: {resp.raw} \n Json: {resp.json} \n Links: {resp.links} \n')

def testMock():
    URL = 'http://localhost:8080/get/this'

    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/json'

    resp = requests.get(url=URL, headers=headers)
    
    jsonData = json.dumps(resp.json(), indent=4)
    testeDict = dict(resp.json())

    print(testeDict['data']['idCotacao'])
    #print(json.dumps(resp.json(), indent=4))

def myTestMock():
    URL = 'http://localhost:8080/api/mytest'

    resp = requests.get(url=URL)

    print(resp.content)

def shutDownWireMock():
    URL = 'http://localhost:8080/__admin/shutdown'

    #TODO - try/except
    resp = requests.post(url=URL)

    print(f"{resp.content} \n {resp.status_code}")

createMock()
#testMock()
#myTestMock()
#shutDownWireMock()
