import requests
import re
import sys,argparse
import bcolors

def banner():
    print("""

        █▀ ▀█▀ █▀█ █ █▀▀ ▀█▀ ▄▄ █▀ █▀▀ █▀▀ █░█ █▀█ █ ▀█▀ █▄█ ▄▄ █▀▀ █ █▄░█ █▀▄ █▀▀ █▀█
        ▄█ ░█░ █▀▄ █ █▄▄ ░█░ ░░ ▄█ ██▄ █▄▄ █▄█ █▀▄ █ ░█░ ░█░ ░░ █▀░ █ █░▀█ █▄▀ ██▄ █▀▄
                                                                            Code by NG          
          """)
if len(sys.argv) > 1:
    banner()
    if(sys.argv[1] =='-u'):
        try:
              input_url = sys.argv[2]

              parser= argparse.ArgumentParser()
              parser.add_argument("-u" , required=True)

              input_header = requests.get(input_url)
              h_text= input_header.headers['Strict-Transport-Security']
              DAYS_IN_WEEK = 7

              def find(number_of_days):
                # Assume that years is
                # of 365 days
                year = int(number_of_days / 365)
                week = int((number_of_days % 365) /
                       DAYS_IN_WEEK)
                days = (number_of_days % 365) % DAYS_IN_WEEK

                print("Years in HSTS value = ", year,
                      "\nweeks in HSTS value = ", week,
                      "\ndays in HSTS value= ", days)

              if 'max-age' in h_text:
                    input_max_age = re.findall(r'\w+',h_text)
                    print(bcolors.OKMSG + 'Strict Transport Security Header Found with max life of  :',input_max_age[2])
                    it = int(input_max_age[2])
                    year= it/86400
                    print(bcolors.OKMSG + 'Value of HSTS after Conversion in Years, month and days')
                    find(year)
              else:
                    print('Strict Transport Security Header not found ')
        except:
                 print('Please enter python hsts.py -u <valid URL with http:// or https://> ')

    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: hsts.py [-h] -u URL' '\n' 'OPTIONS:' '\n' '-h,--help    '
                         'show this help message and exit' '\n''-u URL,   --url URL' )
    elif (sys.argv[1] != '-u') :
        print('Please enter -u < valid URL with https:// ot https:// >')
else:
    banner()
    print(bcolors.ERR + 'Please select at-least 1 option from -u or -h, with a valid URL')
