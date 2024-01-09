#!/usr/local/bin/python3.7
# -*- coding: UTF-8 -*-

import sys, json

result_json = {'key': 'value'}

print('Content-Type:application/json\n\n')
print(json.dumps(result_json))