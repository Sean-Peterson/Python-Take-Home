import requests
import json

#  Test variables
# city = 'portland'
# state = "or"
# income = 50
# marital_status = 'single'



city = raw_input("Which city do you live in? ")
state = raw_input("2 letter abbreviation of your state: ")
income = input("What is your annual income? ")
def maritals():
    marital_status = raw_input("single or married? ")
    marital_status = str(marital_status.lower())
    if marital_status == 'single' or 'married':
        return marital_status
    else:
        pass
marital_status = maritals()
# break.............................................................................

url = 'https://taxee.io/api/v2/state/2017/%s'%state
headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBUElfS0VZX01BTkFHRVIiLCJodHRwOi8vdGF4ZWUuaW8vdXNlcl9pZCI6IjU5MTlmMTlmZTkyMWMwMzY2NjZmMTMxZiIsImh0dHA6Ly90YXhlZS5pby9zY29wZXMiOlsiYXBpIl0sImlhdCI6MTQ5NDg3MjQ3OX0.grP0a9fG_4NdaOaRWk5H-lwG9XOfcgic8eUmhTPF7Tc'}
decoded = requests.get(url, headers=headers).json()
state_tax = 0

if 'income_tax_brackets' in decoded[marital_status]:
    tax_brackets = decoded[marital_status]['income_tax_brackets']
else:
    tax_brackets = 'none'
#if the state has an income tax then the information will be set to variables and used later on. The for loop runs for as many brackets as there are for if the user is single or married.
if tax_brackets == 'none':
    pass
else:
    for i in range(0, len(decoded[marital_status]['income_tax_brackets'])-1):
        if(income<decoded[marital_status]['income_tax_brackets'][i]['bracket']):
            tax_array_number = i-1;
            break
        else:
            tax_array_number=len(decoded[marital_status]['income_tax_brackets'])-1;

#get the state tax number and multiply by one onehundredth to get the correct decimal value.
if tax_brackets == 'none':
    pass
else:
    state_tax=.01*(float(decoded[marital_status]['income_tax_brackets'][tax_array_number]['marginal_rate']))

print state_tax

# break..............................................................................

url = 'https://taxee.io/api/v2/federal/2017/'
headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBUElfS0VZX01BTkFHRVIiLCJodHRwOi8vdGF4ZWUuaW8vdXNlcl9pZCI6IjU5MTlmMTlmZTkyMWMwMzY2NjZmMTMxZiIsImh0dHA6Ly90YXhlZS5pby9zY29wZXMiOlsiYXBpIl0sImlhdCI6MTQ5NDg3MjQ3OX0.grP0a9fG_4NdaOaRWk5H-lwG9XOfcgic8eUmhTPF7Tc'}
decoded = requests.get(url, headers=headers).json()
fed_tax = 0
no_tax = decoded.get('type', 'Default value')


for i in range(0, len(decoded[marital_status]['income_tax_brackets'])):
    if income<decoded[marital_status]['income_tax_brackets'][i]['bracket']:
        tax_array_number=i-1
        break
    else:
        tax_array_number=len(decoded[marital_status]['income_tax_brackets'])-1

fed_tax=.01*(float(decoded[marital_status]['income_tax_brackets'][tax_array_number]['marginal_rate']))

print fed_tax

# break..........................................................................................
