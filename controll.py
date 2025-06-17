import re
from custom_exception import ArgumentsException
def is_email(email):
    regexp = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+')
    if(re.fullmatch(regexp, email)):
        return email
    else:
        raise ArgumentsException("Errore nel parametro email, hai inserito: ", email)
    

def is_path_txt(otp_txt):
    if("/" in otp_txt or "\\" in otp_txt):
        regexp = re.compile(r'^[/a-zA-Z0-9._-]+$') 
        if(not re.fullmatch(regexp, otp_txt)):
                raise ArgumentsException("Errore nel parametro otp_txt, hai inserito: ", otp_txt)
    if(otp_txt.endswith(".txt")):
        return otp_txt
    else:
        raise ArgumentsException("Errore nel parametro otp_txt, hai inserito: ", otp_txt)

def is_otp(otp_code, len_code_ok):
    n_char_code = len(otp_code)
    if(n_char_code < len_code_ok or n_char_code > len_code_ok):
        return False
    else:
        return True

def is_url(url):
    regexp = re.compile(r'^https?:\/\/[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*$', re.IGNORECASE)
    if(re.fullmatch(regexp, url)):
            return url
    else:
            raise ArgumentsException("Errore nel parametro url, hai inserito: ", url)

def is_method(method):
     method_accepted = ["POST", "GET"]
     if(method in method_accepted):
          return method
     else:
          raise ArgumentsException("Method not accepted, hai inserito: ", method)

#TODO:
#Inserire possibilità di backslash
#Stampa Eccezione con una virgola, elminare
#Migliorare RegExp per terminazione url senza estensione (es. http://10.10.253.39:1337/reset_password)
