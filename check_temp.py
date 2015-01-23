#!/usr/bin/python3

import subprocess
import re
#import collections
import sys
sensorsOutput = subprocess.check_output("sensors", universal_newlines=True)
#print('sensors output is:')
#print(sensorsOutput)

#pattern = re.compile('Core \d:\s+\+\d{2,3}')
#print(pattern.findall(sensorsOutput))
#temps = pattern.findall(sensorsOutput)

warning = 40
critical = 45

temps = re.findall('(Core \d):\s+\+(\d{2,3})', sensorsOutput)

#print('what gets returned from re is:')
#print(temps)
#print('turn that into dictionary:')
D = dict(temps)
#print(D)

status = {}
message = ''

for i in D:
  if int(D[i]) > critical:
    status[i] = 'critical'
  elif int(D[i]) > warning:
    status[i] = 'warning'
  else:
    status[i] = 'ok'

if 'critical' in status.values():
  message = 'CRITICAL'
elif 'warning' in status.values():
  message = 'WARNING'
else:
  message = 'OK'

#print(status)
print('TEMP', message, '|', " ".join(["'%s'=%s" % t for t in temps]))
#for (k, v) in D.items(): print("'",k,"'","=", v, sep='', end=' ')
if message == 'CRITICAL':
  sys.exit(2)
elif message == 'WARNING':
  sys.exit(1)
