# import requests


# url = "https://accounts.google.com/o/oauth2/v2/auth"

# qparams = {"client_id": "$143443373358-r284g9f9mg10c9dv3bqs4n4t6c805q5b.apps.googleusercontent.com", "client_secret": "$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", "grant_type":"refresh_token", "refresh_token":"$1//0gck11FXkopBKCgYIARAAGBASNwF-L9IrxuMidROgb1u48h8Q9UjvuSaR3JLhQVZOG6-3qPD3q5lS2tQNcaVZBXa5J33RseR9uYw"}


# response = requests.request("POST", url, params=qparams)

# print(response.text.encode('utf8'))

# import pickle
# import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request


# SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# creds = None

# if os.path.exists('token.pickle'):
#     with open('token.pickle', 'rb') as token:
#         creds = pickle.load(token)

# if not creds or not creds.valid:
#     if creds and creds.expired and creds.refresh_token:
#         creds.refresh(Request())
#     else:
#         flow = InstalledAppFlow.from_client_secrets_file(
#             '/home/arcgate/Downloads/client_secret_143443373358-r284g9f9mg10c9dv3bqs4n4t6c805q5b.apps.googleusercontent.com (1).json', SCOPES)
#         creds = flow.run_local_server(port=0)

#     with open(token.pickle, 'wb') as token:
#         pickle.dump(creds, token)

# service = build('gmail', 'v1', credentials=creds)

# results = service.users().labels().list(userId='me').execute()
# labels = results.get('labels', [])


# if not labels:
#     print('No lables')
# else:
#     print('labels :')
#     for label in labels:
#         print(label['name'])


# import pickle
# cars = ['Audi', 'BMW']
# file = 'token.pickle'
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()


# import pickle
# file = 'token.pickle'
# fileobj = open(file,'rb')
# mycar = pickle.load(fileobj)
# print(mycar,'mycar')
# print(type(mycar))


# import requests
# import pickle

# client_id = '143443373358-r284g9f9mg10c9dv3bqs4n4t6c805q5b.apps.googleusercontent.com'

# client_secret = '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'

# # scope = f'api://{client_id}/user.access'
# scope = 'https://www.googleapis.com/auth/userinfo.profile'

# token_url = 'https://login.microsoftonline.com/xxx/oauth2/v2.0/token'

# d = {
#     "client_id": client_id,
#     "scope": scope,
#     "client_secret": client_secret,
#     "grant_type": "client_credentials",
#     "refresh_token": "1//0gck11FXkopBKCgYIARAAGBASNwF-L9IrxuMidROgb1u48h8Q9UjvuSaR3JLhQVZOG6-3qPD3q5lS2tQNcaVZBXa5J33RseR9uYw"
# }

# r = requests.post(token_url, data=d)


# access_token = r.json()['access_token']
# print(access_token, 'access_token')


# import requests

# url = "https://oauth2.googleapis.com/token"

# payload='client_id=143443373358-qtuke9egbqd55ut4h0oud2m3cd7cuqn3.apps.googleusercontent.com&client_secret=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&code=4%2F0AfJohXkShtAZ9HxsftlBA3mrhD-QM8fkCK1Es9D1BlreSRMRyHnzX2h9zQw4Z4vyECr3tw&grant_type=authorization_code&redirect_uri=https%3A%2F%2Flocalhost'
# headers = {
#   'Content-Type': 'application/x-www-form-urlencoded'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

def test_data_value():
  import requests
  import json

  url = "https://gmail.googleapis.com/gmail/v1/users/me/messages/send"

  payload = json.dumps({
    "raw": "RnJvbTogc2h1YmhhbXZpamF5dmFyZ2l5YTVAZ21haWwuY29tClRvOiBzaHViaGFtdmlqYXl2YXJnaXlhNTlAZ21haWwuY29tClN1YmplY3Q6IFNheWluZyBIZWxsbwoKVGhpcyBpcyBhIG1lc3NhZ2UganVzdCB0byBzYXkgaGVsbG8uClNvLCAiSGVsbG8iLg=="
  })
  headers = {
    'Authorization': 'Bearer ya29.a0AfB_byC2KqZWQBD37O5a3hU7hcH4Bgk_vBipPrTI9Lqur6cSIN20l_Wa7bf4eNVaXJz2iVqOcQJLIFEaTAq5Apj3E4Ohll6LDB7Xz2q2ffLtDeWtj9ciKv6p_Zj7_B-av-dMSrAfDM2oONYClnGxsOROKTvEtfs7YZOd_AaCgYKAXISARESFQHGX2MiekaNXPjJZSnrdTZVeSbH7Q0173',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)





