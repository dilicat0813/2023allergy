# Python3 샘플 코드 #
# key = 'SDqWmmlSMlsBobBnB0DwlV9IVwFkxNwn42%2BKrK%2F5WMV0AxecYPKMJ2tAurfLvCGOt2hvyBLvi9oG7R%2Bn%2FG4ZUA%3D%3D'

import requests

url = 'http://apis.data.go.kr/B553748/CertImgListService/getCertImgListService'
params ={'serviceKey' : 'SDqWmmlSMlsBobBnB0DwlV9IVwFkxNwn42+KrK/5WMV0AxecYPKMJ2tAurfLvCGOt2hvyBLvi9oG7R+n/G4ZUA==', 'returnType' : 'xml', 'pageNo' : '1', 'numOfRows' : '100' }

response = requests.get(url, params=params)
print(response.content)
