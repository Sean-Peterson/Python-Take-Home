import requests
import json

income = 50000
marital_status = 'single'

url = 'https://taxee.io/api/v2/state/2017/Or'
headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBUElfS0VZX01BTkFHRVIiLCJodHRwOi8vdGF4ZWUuaW8vdXNlcl9pZCI6IjU5MTlmMTlmZTkyMWMwMzY2NjZmMTMxZiIsImh0dHA6Ly90YXhlZS5pby9zY29wZXMiOlsiYXBpIl0sImlhdCI6MTQ5NDg3MjQ3OX0.grP0a9fG_4NdaOaRWk5H-lwG9XOfcgic8eUmhTPF7Tc'}
r = requests.get(url, headers=headers).json()
# print r['single']

# for(i=0;i<count(r[marital_status]['income_tax_brackets']);i++){
#     if(income<r[marital_status]['income_tax_brackets'][i]['bracket']):
#         tax_array_number=i-1;
#         break;
#     else:
#         tax_array_number=count(r[marital_status]['income_tax_brackets'])-1;

for i in range(0, len(r[marital_status]['income_tax_brackets'])):
    if income<r[marital_status]['income_tax_brackets'][i]['bracket']:
        tax_array_number=i-1
        pass
    else:
        tax_array_number=len(r[marital_status]['income_tax_brackets'])-1
print tax_array_number
# r = requests.get('https://api.github.com/events')
# print r.json()
