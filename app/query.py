import requests
import json


class Query():
    def __init__(self):
       pass
    '''
    @Brief:
    Queries Topstory of seznamzpravy 

    Return: dict 3 of the top headlines, and their timestamps
    '''
    def QueryTopStory(self):
        #get the JSON containing the template for top stories - return a JSON
       
        response = requests.get("http://api.seznamzpravy.cz/v1/timelines?itemIds=593ea6b9d7aa9828709783b3").json()
        
        Result = {}
        
        for i in range(3):
           title = (response['_items'][0]['documents']['_items'][i]['title'])
           timestamp = (response['_items'][0]['documents']['_items'][i]['dateOfPublication'])    
           Result[title] = timestamp
          
        return(Result)

    ''' 
     @Brief:
     Searches for a specific thing in a specific range

     Return: dict of count top headlines, as well as their timestamps
     '''   
    def Search(self,keyword=None,count=3):
        if keyword == None:
            pass
        else:
            url = "https://api.seznamzpravy.cz/v1/search?service=zpravy&query={}".format(keyword)
            response = requests.get(url).json()
            
            Result = {}
            try:
                for i in range(count):
                    title = (response['_items'][i]['title'])
                    timestamp = (response['_items'][i]['dateOfPublication'])    
                    Result[title] = timestamp
            except IndexError:
                return(Result)
            
            return(Result)
            


    
