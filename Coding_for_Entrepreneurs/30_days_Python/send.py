# def my_print(txt):
#     print(txt)

# msg_template="""Hello {name}, thank you for joining {website}"""

# def format_msg(my_name, my_website):
#     my_msg=msg_template.format(name=my_name, website=my_website)
#     return my_msg

#Sending 
import sys
import requests
from datetime import datetime

#Requests sirve para poder acceder al contenido URL

from requests.models import Response

from formatting import format_msg

def send(name,website,verbose=False):
    if website != None:
        msg = format_msg(my_name=name, my_website=website)
        
    else:
        msg=format_msg(my_name=name,my_website="Facebook")
      
    if verbose:
        print(name,website)
    #send the message
    r = requests.get("http://httpbin.org/json")
    if r.status_code==200:
        return r.json()
    else:
        return "there was an error "



if __name__=="__main__":
    print(sys.argv)
    name="Luciano"
    if len(sys.argv)>1:
        name=sys.argv[1]
    response=send(name,"Facebook",verbose=True)
    print(response)