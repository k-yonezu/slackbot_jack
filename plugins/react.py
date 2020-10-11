from slackbot.bot import respond_to
from slackbot.bot import listen_to
import urllib.request
import requests
import json
import random
import numpy as np

REACT_LIST = ['bangbang', 'thumbsup', 'eyes', 'heavy_check_mark']

@listen_to('http')
def reply_recommend(message):
    message.react(random.choice(REACT_LIST))
