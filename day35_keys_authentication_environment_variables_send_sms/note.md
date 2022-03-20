# About Environment Variables

## Create a secure api key
type in terminal

export OWN_API_KEY = XXXXXXXXXX

type env in terminal to see the key you stored.

## Use key in python
import os

api_key = os.environ.get("OWN_API_KEY")