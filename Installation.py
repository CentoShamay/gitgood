###########################################################
##                                                      ##
##   Porpuse : Components Installation                  ##
##   Version : 0.0.1                                    ##
##   Creator : DorShamay                                ##
##                                                      ##
##########################################################
import sys
import os
import shutil
import time
import psutil
from subprocess import Popen

BalancerID = 0
NavigatorID = 0
TanglesID = 0

def main_menu():


    choice = '0'
    while choice == '0':
        print("Installation program, 1 to proceed or 2 to exit")

        choice = input("Please make a choice: ")

    if choice == "1":
        print("Proceed to installation ...")
        deploydebug()
    elif choice == "2":
        print("Installation exited")
        sys.exit()
    else:
        print("Didn't understand your choice.")

def deploydebug():
    path = input("Please write the DeployDebug path here : ")
    print(os.path.exists(path))
    if os.path.exists(path) == True:
        shutil.rmtree(path)
        os.system("C:\\Code\\Cobwebs\\Cobwebs_Release_V5\\cobwebs\\cobwebs\\deploy_debug.bat")
        time.sleep(2)
        components()
    else:
        print("Oops didn't find the DeployDebug folder please try again... ")

def components():
    print("Now lets install the components for Tangles")

    PROCESS_NAME = "NavigatorBalancingService"
    for p in psutil.process_iter():
        if p.name() == PROCESS_NAME:
            print("The Balancer service is running Let's kill it ... ")
            p.kill()
            time.sleep(7)
            proc = Popen("InstallBalancingServer.bat", cwd=r"C:\\Code\\Cobwebs\\Cobwebs_Release_V5\\cobwebs\\cobwebs\\DeployDebug\\Cobwebs")
            stdout, stderr = proc.communicate()
            break
    time.sleep(7)
    PROCESS_NAME = "ProxiesConnectorService"
    for p in psutil.process_iter():
        if p.name() == PROCESS_NAME:
            print("The Proxy Connector service is running Let's kill it ... ")
            p.kill()
            time.sleep(7)
            proc = Popen("InstallProxiesConnectorService.bat", cwd=r"C:\\Code\\Cobwebs\\Cobwebs_Release_V5\\cobwebs\\cobwebs\\DeployDebug\\Cobwebs")
            stdout, stderr = proc.communicate()
            break
    time.sleep(7)
    PROCESS_NAME = "NavigatorService"
    for p in psutil.process_iter():
        if p.name() == PROCESS_NAME:
            print("The Navigator Service is running Let's kill it ... ")
            p.kill()
            time.sleep(7)
            proc = Popen("InstallNavigationServer.bat", cwd=r"C:\\Code\\Cobwebs\\Cobwebs_Release_V5\\cobwebs\\cobwebs\\DeployDebug\\Cobwebs")
            stdout, stderr = proc.communicate()
            break
    time.sleep(7)
    PROCESS_NAME = "TanglesServerService"
    for p in psutil.process_iter():
        if p.name() == PROCESS_NAME:
            print("The Tangles Server service is running Let's kill it ... ")
            p.kill()
            time.sleep(7)
            proc = Popen("InstallTanglesServer.bat", cwd=r"C:\\Code\\Cobwebs\\Cobwebs_Release_V5\\cobwebs\\cobwebs\\DeployDebug\\Cobwebs")
            stdout, stderr = proc.communicate()
            break
    time.sleep(7)
main_menu()
