# -*- coding: utf-8 -*-
## Iris Startup Lab 
'''
<(*)
  ( >)
  /|
'''

####### Here we store the secrets and the main variables of the Forecasting Models 

import os
from pathlib import Path
from dotenv import load_dotenv #### Load the environment

load_dotenv()

TIMEGPT_API_KEY = os.getenv('timegpt_api_key')



