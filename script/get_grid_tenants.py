#!/usr/bin/env python
import requests
import sys
import json


if __name__ == "__main__":
  # prepare authentication data

  with open('global.vars') as json_file:
         global_vars = json.load(json_file)
         

  auth_body = {
	"username":    global_vars['sgadmin_user'],
	"password":    global_vars['sgadmin_pwd'],
	"cookie":      "false",
	"csrfToken":   "false"
              }
  headers = {'Content-Type':'application/json', 'accept':'application/json'}
  grid_base_url = 'https://cbc-sgdemo-adm/'
  rest_url = 'api/v3/grid/accounts'

  # Get GRID auth token
  grid_auth = requests.post(grid_base_url + '/api/v3/authorize',
                            data=json.dumps(auth_body),
                            headers=headers,
                            verify=False).json()['data']

  # REST call to GRID
  res = requests.get(grid_base_url + rest_url,
                     verify=False,
                     headers={'accept': 'application/json', 'authorization': 'Bearer {}'.format(grid_auth)})

  #print tenants details
  for t in res.json()['data']:
       print('{0:25}{1:5}{2:15}'.format(t['id'],' = ',t['name']))


else:
   print('ELSE IS HERE')
