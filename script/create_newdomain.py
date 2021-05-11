#!/usr/bin/env python
import requests
import sys
import json
import os

'''
newdomain: testdomain.com
sgadmin_pwd: $encrypted$
sgadmin_user: root
'''

if __name__ == "__main__":
  # preapare variables to pass to Ansible AWX
  
  with open('global.vars') as json_file:
       global_vars = json.load(json_file)
  with open('extra_newdomain.vars') as json_file_extra:
       extra_vars = json.load(json_file_extra)
  
  
  new_data = {
          "extra_vars":
          { 
            "newdomain":      extra_vars['newdomain'],
            "sgadmin_user":   global_vars['sgadmin_user'],
            "sgadmin_pwd":    global_vars['sgadmin_pwd']
          }
         }
  # basic REST call parameters
  headers = {'content-type':'application/json'}
  base_url = global_vars['tower_base_url']
  api_url = '/api/v2/job_templates/17/launch/'
  
  # REST call to Ansible AWX
  res = requests.post(base_url + api_url,
                      auth=(global_vars['tower_user'],global_vars['tower_pwd']),
                      verify=False,
                      data=json.dumps(new_data),
                      headers=headers)
  
  #print job status
  print('{0:25}{1}'.format('Job ID started:',res.json()['job']))
  print('{0:25}{1:25}'.format('Job NAME: ',res.json()['summary_fields']['job_template']['name']))

else:
	print('ELSE IS HERE')