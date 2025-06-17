
from os import path
from controll import is_otp
def otp_from_txt(otp_txt):
    otp_codes = []
    try:
        path.exists(otp_txt)
        with open(otp_txt, 'r') as txt:
            for otp in txt:
                otp = otp.strip("\n").strip()
                if(is_otp(otp_code=otp, len_code_ok=4)):
                    otp_codes.append(otp)
                else:
                    exit(f"ERRORE: Otp di lunghezza differente, primo otp incriminato: {otp}")
        return otp_codes
    except FileNotFoundError as e:
        print("File o directory specificata non esistete")
    except PermissionError as e:
        print("Non hai i permessi sufficenti sul file o sulla directory")

#Per il momento lunghezza otp fissata su 4, volendo implementare funzionalità per variazioni utente