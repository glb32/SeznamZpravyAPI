import requests


#NOTE: MULTIPLE INSTANCES HAVE TO BE IN DIFFERENT THREADS FOR BEST PERFORMANCE
class Query():


    #Template for SeznamZpravy API calls
    def Request(self,RequestType=''):
        url = 'https://api.seznamzpravy.cz/v1/{}'.format(RequestType)
        response = requests.get(url).json()
        return(response)

    '''
    QueryTopStoryHeadline()
    Queries Top headlines of seznamzpravy 

    Returns: dictionary 3 of the top headlines, as well as their timestamps
    '''
    def QueryTopStoryHeadline(self,IdOnly=True):
        #get the JSON containing the template for top stories - return a JSON
        response = self.Request('timelines?itemIds=593ea6b9d7aa9828709783b3')
        
        Result = {}
    

        for i in range(10):
    
           
           try:
               title = (response['_items'][0]['documents']['_items'][i]['title'])
               idtimestamp = self.Search(title,1,1)
               Result[title] = idtimestamp
           except IndexError:

                idtimestamp = self.Search(title,1,1)
                Result[title] = idtimestamp

     
                
        return(Result)

    #GetDocumentText(): Gets a brief description of an Article
    def GetDocumentText(self,id=0):
        
        url = "https://api.seznamzpravy.cz/v1/documents/{}".format(id)
        response = requests.get(url).json()
        text = response['content'][0]['properties']['texts'][0]
        timestamp = (response['_created'])   
        return(text)



    
    ''' 
     Search()

     Searches SeznamZpravy for a specific keyword 

     Returns: dict of count top headlines, as well as their timestamps, or the ID of a given headline

     '''   
    def Search(self,keyword=None,count=3,TopStory=False):
        if keyword == None:
            pass
        else:
            response = self.Request("search?service=zpravy&query={}".format(keyword))
            Result = {}
            try:
                for i in range(count):
                    
                    title = (response['_items'][i]['title'])
                    uid = response['_items'][i]['uid']
                    if(TopStory):
                        return(uid)
                    else:
                        Result[title] = str(uid)

            except IndexError:
                return(Result)
            

            return(Result)
