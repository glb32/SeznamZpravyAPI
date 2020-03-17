import requests
import json


class Query():
    def __init__(self,LastId):
        self.LastId = str(LastId)

    #Query headlines with HTTP GET
    def Request(self,RequestType=''):
        url = 'https://api.seznamzpravy.cz/v1/{}'.format(RequestType)
        response = requests.get(url).json()
        return(response)

    '''
    QueryTopStoryHeadline
    Queries Top headlines of seznamzpravy 

    Return: dict 3 of the top headlines, and their timestamps
    '''
    def QueryTopStoryHeadline(self):
        #get the JSON containing the template for top stories - return a JSON
        response = self.Request('timelines?itemIds=593ea6b9d7aa9828709783b3')
        
        Result = {}


        for i in range(3):
           title = (response['_items'][0]['documents']['_items'][i]['title'])
           self.LastId = self.Search(title,1,1)

           Result[title] = self.LastId


           return(Result)
    def GetDocumentText(self):
        url = "https://api.seznamzpravy.cz/v1/documents/{}".format(self.LastId)
        response = requests.get(url).json()
        text = response['content'][0]['properties']['texts'][0]
        return(text)


    
    ''' 
     Search

     Searches for a specific thing in a specific range

     Return: dict of count top headlines, as well as their timestamps, or the ID of a given headline

     '''   
    def Search(self,keyword=None,count=3,ReturnId=False):
        if keyword == None:
            pass
        else:
            response = self.Request("search?service=zpravy&query={}".format(keyword))
            
            
            Result = {}
            try:
                for i in range(count):
                    title = (response['_items'][i]['title'])
                    timestamp = (response['_items'][i]['dateOfPublication'])    
                    Result[title] = timestamp
            except IndexError:
                return(Result)
            
            if(ReturnId):
                self.LastId=response['_items'][0]['uid']
                return(self.LastId)

            return(Result)
            
