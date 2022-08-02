import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()


# FOR CODES

API_ID = int(getenv("API_ID")) 
API_HASH = getenv("API_HASH") 
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5391883908").split()))
LOGGER = int(getenv("LOGGER", None)) 
OWNER = int(getenv("OWNER_ID")) 
NAME = getenv("ALIVE_NAME")
OWN_USERNAME= getenv("OWN_USERNAME")
ALIVE_PIC = getenv("ALIVE_PIC") 

# FOR SPAMBOT

TOKEN1 = getenv("TOKEN1", None) 
TOKEN2 = getenv("TOKEN2", None) 
TOKEN3 = getenv("TOKEN3", None) 
TOKEN4 = getenv("TOKEN4", None) 
TOKEN5 = getenv("TOKEN5", None) 
TOKEN6 = getenv("TOKEN6", None) 
TOKEN7 = getenv("TOKEN7", None) 
TOKEN8 = getenv("TOKEN8", None) 
TOKEN9 = getenv("TOKEN9", None) 
TOKEN10 = getenv("TOKEN10", None) 
