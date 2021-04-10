# pip install google-api-python-client
from googleapiclient.discovery import build
import pprint
 
#define key
api_key = "AIzaSyDZY4tCSmJPQ1KHKfYFTTfyK3spMBRzlo8"
cse_key = "669745d1113150082"
 
resource = build("customsearch", 'v1', developerKey=api_key).cse()
result = resource.list(q='ABACAXI', cx=cse_key, num= 10).execute()
 
for item in result['items']:
    print(item['title'], item['link'])