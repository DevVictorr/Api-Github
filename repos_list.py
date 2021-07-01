from requests import status_codes
import requests


class repo(): 

    def __init__(self, user):
        
        self.user = user

    def repos(self):

        request = requests.get('https://api.github.com/users/'+self.user+'/repos')
        json = request.json()
        for i in range(0,len(json)):
            print("Project Name:",json[i]["name"])