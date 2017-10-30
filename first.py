import requests
import json

city = 'Austin'
income = 4000
marital_status = 'single'
state = 'OR'

url = 'https://taxee.io/api/v2/state/2017/%s'%state
headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBUElfS0VZX01BTkFHRVIiLCJodHRwOi8vdGF4ZWUuaW8vdXNlcl9pZCI6IjU5MTlmMTlmZTkyMWMwMzY2NjZmMTMxZiIsImh0dHA6Ly90YXhlZS5pby9zY29wZXMiOlsiYXBpIl0sImlhdCI6MTQ5NDg3MjQ3OX0.grP0a9fG_4NdaOaRWk5H-lwG9XOfcgic8eUmhTPF7Tc'}
decoded = requests.get(url, headers=headers).json()
state_tax = 0
no_tax = decoded.get('type', 'Default value')

if no_tax == "none":
    tax_brackets = 'none'
else:
    tax_brackets = decoded[marital_status]['income_tax_brackets']
#if the state has an income tax then the information will be set to variables and used later on. The for loop runs for as many brackets as there are for if the user is single or married.
if tax_brackets == 'none':
    pass
else:
    print len(decoded[marital_status]['income_tax_brackets'])
    print decoded[marital_status]['income_tax_brackets']
    for i in range(0, len(decoded[marital_status]['income_tax_brackets'])-1):
        if(income<decoded[marital_status]['income_tax_brackets'][i]['bracket']):
            tax_array_number=i-1;
            print decoded[marital_status]['income_tax_brackets'][i]['bracket']
            break
        else:
            print 'lalal'
            tax_array_number=len(decoded[marital_status]['income_tax_brackets'])-1;

#get the state tax number and multiply by one onehundredth to get the correct decimal value.
if tax_brackets == 'none':
    print 'passed'
    pass
else:
    state_tax=.01*(float(decoded[marital_status]['income_tax_brackets'][tax_array_number]['marginal_rate']))

print state_tax




# for i in range(0, len(decoded[marital_status]['income_tax_brackets'])):
#     if income<decoded[marital_status]['income_tax_brackets'][i]['bracket']:
#         tax_array_number=i-1
#         pass
#     else:
#         tax_array_number=len(decoded[marital_status]['income_tax_brackets'])-1
#         pass

# fed_tax=.01*(float(decoded[marital_status]['income_tax_brackets'][tax_array_number]['marginal_rate']))
# #if the city is not new york then multiply by new york to get the correct COL since ny is the base standard
# if city != "New-York":
#     user_col = 842
#     rent = 1600
#     user_state = 'TX'
#     pass
# else:
#     user_col = 1800
#     rent = 2000
#     user_state = 'NY'
#     pass
# print fed_tax
