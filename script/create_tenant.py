#!/usr/bin/env python
import requests
import sys
import json
import os

'''
'''

if __name__ == "__main__":
  # preapare variables to pass to Ansible AWX
  
  with open('global.vars') as json_file:
       global_vars = json.load(json_file)
  with open('extra_tenant.vars') as json_file_extra:
       extra_vars = json.load(json_file_extra)
  
  
  new_data = {
          "extra_vars":
          { 
            "tenant_acc":      extra_vars['tenant_acc'],
            "tenant_user":      extra_vars['tenant_user'],
            "tenant_pwd":      extra_vars['tenant_pwd'],
            "tenant_qs":      extra_vars['tenant_qs'],
            "tenant_proto":      extra_vars['tenant_proto'],
            "sgadmin_user":   global_vars['sgadmin_user'],
            "sgadmin_pwd":    global_vars['sgadmin_pwd']
          }
         }
  # basic REST call parameters
  headers = {'content-type':'application/json'}
  base_url = global_vars['tower_base_url']
  api_url = '/api/v2/job_templates/15/launch/'
  
  # REST call to Ansible AWX
  res = requests.post(base_url + api_url,
                      auth=(global_vars['tower_user'],global_vars['tower_pwd']),
                      verify=False,
                      data=json.dumps(new_data),
                      headers=headers)
  
  #print job status
  # debug
  #print(res.content)
  try:
    print('{0:25}{1}'.format('Job ID started:',res.json()['job']))
    print('{0:25}{1:25}'.format('Job NAME: ',res.json()['summary_fields']['job_template']['name']))
  except:
    print(res.content)

else:
	print('ELSE IS HERE')