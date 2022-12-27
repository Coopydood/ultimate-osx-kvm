#!/usr/bin/env python3
# pylint: disable=C0301,C0116,C0103,R0903

# AUTOPILOT BY COOPYDOOD

"""
This script was created by Coopydood as part of the ultimate-macOS-KVM project.
It will not work outside of this project.

https://github.com/user/Coopydood
https://github.com/Coopydood/ultimate-macOS-KVM
Signature: 4CD28348A3DD016F

"""


import os
import time
import subprocess
import re 
import json
import sys
import argparse

#parser = argparse.ArgumentParser("gpu-check")
#parser.add_argument("-a", "--auto", dest="auto", help="Detect GPU(s) automatically",action="store_true")
#parser.add_argument("-m", "--manual", dest="manual", help="Enter GPU model manually", metavar="<model>", type=str)
#parser.add_argument("-f", "--force", dest="forceModel", metavar="<model>", help="Override auto-detected GPU with a custom model. Pretty useless, mostly for debugging.", type=str)

#args = parser.parse_args()

detectChoice = 1
latestOSName = "Ventura"
latestOSVer = "13"
runs = 0

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def startup():
    global detectChoice
    print("\n\nWelcome to"+color.BOLD+color.PURPLE,"AutoPilot"+color.END,"(BETA)")
    print("Created by",color.BOLD+"Coopydood\n"+color.END)
    print("\nThe purpose of this script is to automatically guide you through \nthe process of",color.BOLD+"creating and running a basic macOS VM",color.END+"using settings \nbased on answers to a number of questions. \n\nMany of the values can be left to default - especially if you are unsure.\nIt won't be perfect, but it's supposed to make it as"+color.BOLD,"easy as possible.\n"+color.END)
    print(color.BOLD+"\n"+"Profile:"+color.END,"https://github.com/Coopydood")
    print(color.BOLD+"   Repo:"+color.END,"https://github.com/Coopydood/ultimate-macOS-KVM")
    print("\nContinue whenever you're ready, or return to the main menu.")
    print(color.BOLD+"\n   1. Start")
    print(color.END+"      Begin creating a new QEMU-based macOS config file \n")
    print(color.END+"   2. Main menu")
    print(color.END+"   3. Exit\n")
    detectChoice = int(input(color.BOLD+"Select> "+color.END))

def clear(): print("\n" * 150)

startup()
clear()

def autopilot():
   global USR_CPU_SOCKS
   global USR_CPU_CORES
   global USR_CPU_THREADS
   global USR_CPU_MODEL
   global USR_CPU_FEATURE_ARGS
   global USR_ALLOCATED_RAM
   global USR_REPO_PATH
   global USR_NETWORK_DEVICE
   global USR_ID
   global USR_NAME
   global USR_CFG
   global USR_TARGET_OS
   global USR_HDD_SIZE
   global USR_BOOT_FILE

   USR_CPU_SOCKS = 1
   USR_CPU_CORES = 2 
   USR_CPU_THREADS = 1
   USR_CPU_MODEL = "Penryn"
   USR_CPU_FEATURE_ARGS = "+ssse3,+sse4.2,+popcnt,+avx,+aes,+xsave,+xsaveopt,check"
   USR_ALLOCATED_RAM = "4G"
   USR_REPO_PATH = "."
   USR_NETWORK_DEVICE = "e1000-82545em"
   USR_ID = "macOS"
   USR_NAME = "macOS"
   USR_CFG = "boot.sh"
   USR_TARGET_OS = 1015
   USR_HDD_SIZE = "80G"
   USR_BOOT_FILE = "BaseSystem.img"
   

   global currentStage
   currentStage = 1
   
   global customValue
   customValue = 0

   def generate():
      print(color.BOLD+color.PURPLE+"Not implemented yet! I'm working on it- I swear!\n"+color.END)

   def stage11():
      global USR_CPU_SOCKS
      global USR_CPU_CORES
      global USR_CPU_THREADS
      global USR_CPU_MODEL
      global USR_CPU_FEATURE_ARGS
      global USR_ALLOCATED_RAM
      global USR_REPO_PATH
      global USR_NETWORK_DEVICE
      global USR_ID
      global USR_NAME
      global USR_CFG
      global USR_TARGET_OS
      global USR_HDD_SIZE
      global USR_BOOT_FILE

      USR_ALLOCATED_RAM_F = USR_ALLOCATED_RAM.replace("G","")
      USR_HDD_SIZE_F = USR_HDD_SIZE.replace("G","")
      USR_CPU_TOTAL = USR_CPU_CORES * USR_CPU_THREADS
      USR_CPU_TOTAL_F = str(USR_CPU_TOTAL)

      USR_TARGET_OS_F = USR_TARGET_OS / 100

      if USR_BOOT_FILE == "-1":
         USR_BOOT_FILE_F = "Download from Apple..."
      else:
         USR_BOOT_FILE_F = "Local image file"

      clear()
      print("   "+"\n   "+color.BOLD+"Ready to generate config file"+color.END)
      print("   "+"Review your preferences")
      print("   "+"\n   The config wizard is complete.\n   Review your preferences below and continue when ready."+color.END)
      print("   "+"\n   "+color.BOLD+"──────────────────────────────────────────────────────────────",color.END)
      print("   "+color.BOLD+color.PURPLE+"FILE    ",color.END+color.END+USR_CFG+color.END)
      print("   "+color.BOLD+color.GREEN+"OS      ",color.END+color.END+"macOS",USR_TARGET_OS_F,color.END)
      print("   "+color.BOLD+color.YELLOW+"BOOT    ",color.END+color.END+USR_BOOT_FILE_F,color.END)
      print("   "+color.BOLD+color.CYAN+"CPU     ",color.END+color.END+USR_CPU_MODEL+",",USR_CPU_CORES,"cores,",USR_CPU_THREADS,"threads","("+USR_CPU_TOTAL_F+")"+color.END)  
      #print("   "+color.BOLD+color.CYAN+"        ",color.END+color.BOLD+USR_CPU_FEATURE_ARGS+color.END)
      print("   "+color.BOLD+color.CYAN+"RAM     ",color.END+color.END+USR_ALLOCATED_RAM_F+" GB"+color.END)
      print("   "+color.BOLD+color.CYAN+"DISK    ",color.END+color.END+USR_HDD_SIZE_F+" GB (dynamic)"+color.END)
      print("   "+color.BOLD+color.CYAN+"NETWORK ",color.END+color.END+USR_NETWORK_DEVICE+color.END+"")
      print("   "+color.BOLD+"──────────────────────────────────────────────────────────────",color.END)
      if USR_BOOT_FILE == "-1":
         print(color.BOLD+"\n      1. Download and generate...")
         print(color.END+"         Fetch a new recovery image, then create the config\n         and hard disk file in the repo folder\n")
      else:
         print(color.BOLD+"\n      1. Generate")
         print(color.END+"         Copy the local recovery image, then create the config\n         and hard disk file in the repo folder\n")
      
      print("    "+color.END+"  2. Back")
      print("    "+color.END+"  X. Start Over")
      print("    "+color.END+"  Q. Exit\n")
      stageSelect = str(input(color.BOLD+"Select> "+color.END))
   
      if stageSelect == "1":
         handoff()

      elif stageSelect == "2":
         stage10()

      elif stageSelect == "x" or stageSelect == "X":
         currentStage = 1
         stage1()
         
      elif stageSelect == "q" or stageSelect == "Q":
         exit   

   def stage10():
      global customValue
      global currentStage
      global USR_BOOT_FILE
      defaultValue = "BaseSystem.img"

      clear()
      print("\n   "+color.BOLD+"macOS Recovery image file"+color.END)
      print("   Step 10")
      print("\n   Choose a bootable image file the virtual machine should boot to. \n   You need a macOS Recovery image (BaseSystem.img). You can either\n   select an existing one or the wizard can download one for you.\n   It must be in the *.img file format."+color.END)
      print("\n   "+color.BOLD+color.CYAN+"DEFAULT:",color.END+color.BOLD+defaultValue+color.END)
      if customValue == 1:
      #   print(color.BOLD+color.PURPLE+"\n   FORMAT:"+color.YELLOW+""+color.END+color.BOLD,"<file>"+color.YELLOW+".img"+color.END+"\n   Enter a custom value.\n   \n   ")
         print(color.BOLD+color.PURPLE+"\n   FORMAT:",color.YELLOW+""+color.END+color.BOLD+"<file>"+color.YELLOW+".img"+color.END+"\n   Enter the full path to a bootable macOS Recovery image file.\n   It will be automatically copied into the root repo directory, or you\n   can place it there now and type \"BaseSystem.img\" without a path.\n   You",color.UNDERLINE+color.BOLD+"must"+color.END,"include any text in"+color.YELLOW,"yellow"+color.END+".\n\n      "+color.BOLD+"TIP:"+color.END,"You can drag and drop a file onto this window.\n   \n   ")
         customInput = str(input(color.BOLD+"Value> "+color.END))
         USR_BOOT_FILE = customInput               #+".sh" #<--- change required prefix/suffix
         currentStage = currentStage + 1
         customValue = 0
         blob = open("./blobs/USR_BOOT_FILE.apb","w")
         blob.write(USR_BOOT_FILE)
         blob.close()
         stage11()
      else:
         print(color.BOLD+"\n      1. Download from Apple...")
         print(color.END+"      2. Select existing...")
         print(color.END+"      3. Skip")
         print(color.END+"      4. Back")
         print(color.END+"      Q. Exit\n   ")
         stageSelect = str(input(color.BOLD+"Select> "+color.END))
      
         if stageSelect == "1":
            USR_BOOT_FILE = "-1"
            blob = open("./blobs/USR_BOOT_FILE.apb","w")
            blob.write(USR_BOOT_FILE)
            blob.close()
            blob = open("./blobs/CDN_CONTROL","w")
            blob.write("fresh_cdn")
            blob.close()
            currentStage = currentStage + 1
            stage11()

         elif stageSelect == "2":
            customValue = 1
            stage10()

         elif stageSelect == "3":
            stage11()

         elif stageSelect == "4":
            currentStage = 1
            stage9()
            
         elif stageSelect == "q" or stageSelect == "Q":
            exit   

   def stage9():
      global USR_NETWORK_DEVICE
      global customValue
      global currentStage
      global USR_TARGET_OS

      if USR_TARGET_OS >= 1014:
         defaultValue = "e1000-82545em"
      else:
         defaultValue = "vmxnet3"

      clear()
      print("\n   "+color.BOLD+"Set network adapter model"+color.END)
      print("   Step 9")
      print("\n   Set the model of the virtual network adapter. \n   The default below has been selected based on your target OS,\n   so there shouldn't be a need to change it."+color.END)
      print("\n   "+color.BOLD+color.CYAN+"DEFAULT:",color.END+color.BOLD+defaultValue+color.END)
      if customValue == 1:
         print(color.BOLD+color.PURPLE+"\n   FORMAT:"+color.YELLOW+""+color.END+color.BOLD,"<model name>"+color.YELLOW+""+color.END+"\n   Enter a custom value.\n   \n   ")
      #   print(color.BOLD+color.PURPLE+"\n   FORMAT:",color.YELLOW+""+color.END+color.BOLD+"<model name>"+color.YELLOW+""+color.END+"\n   Enter a custom value. You",color.UNDERLINE+color.BOLD+"must"+color.END,"include any text in"+color.YELLOW,"yellow"+color.END+".\n   \n   ")
         customInput = str(input(color.BOLD+"Value> "+color.END))
         USR_NETWORK_DEVICE = customInput               #+".sh" #<--- change required prefix/suffix
         currentStage = currentStage + 1
         customValue = 0
         blob = open("./blobs/USR_NETWORK_DEVICE.apb","w")
         blob.write(USR_NETWORK_DEVICE)
         blob.close()
         stage10()
      else:
         print(color.BOLD+"\n      1. Use default value")
         print(color.END+"      2. Custom value...")
         print(color.END+"      3. Back")
         print(color.END+"      Q. Exit\n   ")
         stageSelect = str(input(color.BOLD+"Select> "+color.END))
      
         if stageSelect == "1":
            USR_NETWORK_DEVICE = defaultValue
            blob = open("./blobs/USR_NETWORK_DEVICE.apb","w")
            blob.write(USR_NETWORK_DEVICE)
            blob.close()
            currentStage = currentStage + 1
            stage10()

         elif stageSelect == "2":
            customValue = 1
            stage9()

         elif stageSelect == "3":
            currentStage = 1
            stage8()
            
         elif stageSelect == "q" or stageSelect == "Q":
            exit    

   def stage8():
      global USR_HDD_SIZE
      global customValue
      global currentStage
      defaultValue = "80G"

      clear()
      print("\n   "+color.BOLD+"Set hard disk capacity"+color.END)
      print("   Step 8")
      print("\n   Set the maximum virtual hard disk size (capacity). \n   Change this based on how much storage you think you'll need.\n   NOTE: The file will grow dynamically, and is not allocated in full."+color.END)
      print("\n   "+color.BOLD+color.CYAN+"DEFAULT:",color.END+color.BOLD+defaultValue+color.END)
      if customValue == 1:
      #   print(color.BOLD+color.PURPLE+"\n   FORMAT:"+color.YELLOW+""+color.END+color.BOLD,"<>"+color.YELLOW+""+color.END+"\n   Enter a custom value.\n   \n   ")
         print(color.BOLD+color.PURPLE+"\n   FORMAT:",color.YELLOW+""+color.END+color.BOLD+"<number>"+color.YELLOW+"G"+color.END+"\n   Enter a custom value. You",color.UNDERLINE+color.BOLD+"must"+color.END,"include any text in"+color.YELLOW,"yellow"+color.END+".\n   \n   ")
         customInput = str(input(color.BOLD+"Value> "+color.END))
         USR_HDD_SIZE = customInput               #+".sh" #<--- change required prefix/suffix
         currentStage = currentStage + 1
         customValue = 0
         blob = open("./blobs/USR_HDD_SIZE.apb","w")
         blob.write(USR_HDD_SIZE)
         blob.close()
         stage9()
      else:
         print(color.BOLD+"\n      1. Use default value")
         print(color.END+"      2. Custom value...")
         print(color.END+"      3. Back")
         print(color.END+"      Q. Exit\n   ")
         stageSelect = str(input(color.BOLD+"Select> "+color.END))
      
         if stageSelect == "1":
            USR_HDD_SIZE = defaultValue
            blob = open("./blobs/USR_HDD_SIZE.apb","w")
            blob.write(USR_HDD_SIZE)
            blob.close()
            currentStage = currentStage + 1
            stage9()

         elif stageSelect == "2":
            customValue = 1
            stage8()

         elif stageSelect == "3":
            currentStage = 1
            stage7()
            
         elif stageSelect == "q" or stageSelect == "Q":
            exit   

   def stage7():
      global USR_ALLOCATED_RAM
      global customValue
      global currentStage
      defaultValue = "4G"

      clear()
      print("\n   "+color.BOLD+"Set amount of allocated RAM"+color.END)
      print("   Step 7")
      print("\n   Set how much memory the guest can use. \n   As a general rule and for max performance, use no\n   more than half of your total host memory."+color.END)
      print("\n   "+color.BOLD+color.CYAN+"DEFAULT:",color.END+color.BOLD+defaultValue+color.END)
      if customValue == 1:
      #   print(color.BOLD+color.PURPLE+"\n   FORMAT:"+color.YELLOW+""+color.END+color.BOLD,"<>"+color.YELLOW+""+color.END+"\n   Enter a custom value.\n   \n   ")
         print(color.BOLD+color.PURPLE+"\n   FORMAT:",color.YELLOW+""+color.END+color.BOLD+"<number>"+color.YELLOW+"G"+color.END+"\n   Enter a custom value. You",color.UNDERLINE+color.BOLD+"must"+color.END,"include any text in"+color.YELLOW,"yellow"+color.END+".\n   \n   ")
         customInput = str(input(color.BOLD+"Value> "+color.END))
         USR_ALLOCATED_RAM = customInput               #+".sh" #<--- change required prefix/suffix
         currentStage = currentStage + 1
         customValue = 0
         blob = open("./blobs/USR_ALLOCATED_RAM.apb","w")
         blob.write(USR_ALLOCATED_RAM)
         blob.close()
         stage8()
      else:
         print(color.BOLD+"\n      1. Use default value")
         print(color.END+"      2. Custom value...")
         print(color.END+"      3. Back")
         print(color.END+"      Q. Exit\n   ")
         stageSelect = str(input(color.BOLD+"Select> "+color.END))
      
         if stageSelect == "1":
            USR_ALLOCATED_RAM = defaultValue
            blob = open("./blobs/USR_ALLOCATED_RAM.apb","w")
            blob.write(USR_ALLOCATED_RAM)
            blob.close()
            currentStage = currentStage + 1
            stage8()

         elif stageSelect == "2":
            customValue = 1
            stage7()

         elif stageSelect == "3":
            currentStage = 1
            stage6()
            
         elif stageSelect == "q" or stageSelect == "Q":
            exit     

   def stage6():
      global USR_CPU_FEATURE_ARGS
      global customValue
      global currentStage
      defaultValue = "+ssse3,+sse4.2,+popcnt,+avx,+aes,+xsave,+xsaveopt,check"

      clear()
      print("\n   "+color.BOLD+"Set CPU feature arguments"+color.END)
      print("   Step 6")
      print("\n   Set the virtual CPU's feature arguments. \n   Do not change this unless you know what you're doing.\n   The default is more than enough for most people."+color.END)
      print("\n   "+color.BOLD+color.CYAN+"DEFAULT:",color.END+color.BOLD+defaultValue+color.END)
      if customValue == 1:
      #   print(color.BOLD+color.PURPLE+"\n   FORMAT:"+color.YELLOW+""+color.END+color.BOLD,"<>"+color.YELLOW+""+color.END+"\n   Enter a custom value.\n   \n   ")
         print(color.BOLD+color.PURPLE+"\n   FORMAT:",color.YELLOW+"+"+color.END+color.BOLD+"<arg>"+color.YELLOW+","+color.END+"\n   Enter a custom value. You",color.UNDERLINE+color.BOLD+"must"+color.END,"include any text in"+color.YELLOW,"yellow"+color.END+".\n   \n   ")
         customInput = str(input(color.BOLD+"Value> "+color.END))
         USR_CPU_FEATURE_ARGS = customInput               #+".sh" #<--- change required prefix/suffix
         currentStage = currentStage + 1
         customValue = 0
         blob = open("./blobs/USR_CPU_FEATURE_ARGS.apb","w")
         blob.write(USR_CPU_FEATURE_ARGS)
         blob.close()
         stage7()
      else:
         print(color.BOLD+"\n      1. Use default value")
         print(color.END+"      2. Custom value...")
         print(color.END+"      3. Back")
         print(color.END+"      Q. Exit\n   ")
         stageSelect = str(input(color.BOLD+"Select> "+color.END))
      
         if stageSelect == "1":
            USR_CPU_FEATURE_ARGS = defaultValue
            blob = open("./blobs/USR_CPU_FEATURE_ARGS.apb","w")
            blob.write(USR_CPU_FEATURE_ARGS)
            blob.close()
            currentStage = currentStage + 1
            stage7()

         elif stageSelect == "2":
            customValue = 1
            stage6()

         elif stageSelect == "3":
            currentStage = 1
            stage5()
            
         elif stageSelect == "q" or stageSelect == "Q":
            exit    

   def stage5():
      global USR_CPU_MODEL
      global customValue
      global currentStage
      defaultValue = "Penryn"

      clear()
      print("\n   "+color.BOLD+"Set CPU model"+color.END)
      print("   Step 5")
      print("\n   Set the model of the virtual CPU. \n   Unless your host CPU is supported in macOS, leave this alone.\n   Use \"host\" to expose the host CPU model to the guest."+color.END)
      print("\n   "+color.BOLD+color.CYAN+"DEFAULT:",color.END+color.BOLD+defaultValue+color.END)
      if customValue == 1:
         print(color.BOLD+color.PURPLE+"\n   FORMAT:"+color.YELLOW+""+color.END+color.BOLD,"<model name>"+color.YELLOW+""+color.END+"\n   Enter a custom value.\n   \n   ")
      #   print(color.BOLD+color.PURPLE+"\n   FORMAT:"+color.YELLOW+""+color.END+color.BOLD,"<number>"+color.YELLOW+""+color.END+"\n   Enter a custom value. You",color.UNDERLINE+color.BOLD+"must"+color.END,"include any text in"+color.YELLOW,"yellow"+color.END+".\n   \n   ")
         customInput = str(input(color.BOLD+"Value> "+color.END))
         USR_CPU_MODEL = customInput               #+".sh" #<--- change required prefix/suffix
         currentStage = currentStage + 1
         customValue = 0
         blob = open("./blobs/USR_CPU_MODEL.apb","w")
         blob.write(USR_CPU_MODEL)
         blob.close()
         stage6()
      else:
         print(color.BOLD+"\n      1. Use default value")
         print(color.END+"      2. Custom value...")
         print(color.END+"      3. Back")
         print(color.END+"      Q. Exit\n   ")
         stageSelect = str(input(color.BOLD+"Select> "+color.END))
      
         if stageSelect == "1":
            USR_CPU_MODEL = defaultValue
            blob = open("./blobs/USR_CPU_MODEL.apb","w")
            blob.write(USR_CPU_MODEL)
            blob.close()
            currentStage = currentStage + 1
            stage6()

         elif stageSelect == "2":
            customValue = 1
            stage5()

         elif stageSelect == "3":
            currentStage = 1
            stage4()
            
         elif stageSelect == "q" or stageSelect == "Q":
            exit    

   def stage4():
      global USR_CPU_THREADS
      global customValue
      global currentStage
      defaultValue = 2

      clear()
      print("\n   "+color.BOLD+"Set number of CPU threads"+color.END)
      print("   Step 4")
      print("\n   Set the desired number of virtual CPU threads. \n   Like cores, more threads can dramatically improve guest performance if\n   your host can handle it."+color.END)
      print("\n   "+color.BOLD+color.CYAN+"DEFAULT:",color.END+color.BOLD,defaultValue,color.END)
      if customValue == 1:
         print(color.BOLD+color.PURPLE+"\n   FORMAT:"+color.YELLOW+""+color.END+color.BOLD,"<number>"+color.YELLOW+""+color.END+"\n   Enter a custom value.\n   \n   ")
      #   print(color.BOLD+color.PURPLE+"\n   FORMAT:"+color.YELLOW+""+color.END+color.BOLD,"<number>"+color.YELLOW+""+color.END+"\n   Enter a custom value. You",color.UNDERLINE+color.BOLD+"must"+color.END,"include any text in"+color.YELLOW,"yellow"+color.END+".\n   \n   ")
         customInput = int(input(color.BOLD+"Value> "+color.END))
         USR_CPU_THREADS = customInput               #+".sh" #<--- change required prefix/suffix
         currentStage = currentStage + 1
         customValue = 0
         blob = open("./blobs/USR_CPU_THREADS.apb","w")
         blob.write(str(USR_CPU_THREADS))
         blob.close()
         stage5()
      else:
         print(color.BOLD+"\n      1. Use default value")
         print(color.END+"      2. Custom value...")
         print(color.END+"      3. Back")
         print(color.END+"      Q. Exit\n   ")
         stageSelect = str(input(color.BOLD+"Select> "+color.END))
      
         if stageSelect == "1":
            USR_CPU_THREADS = defaultValue
            blob = open("./blobs/USR_CPU_THREADS.apb","w")
            blob.write(str(USR_CPU_THREADS))
            blob.close()
            currentStage = currentStage + 1
            stage5()

         elif stageSelect == "2":
            customValue = 1
            stage4()

         elif stageSelect == "3":
            currentStage = 1
            stage3()
            
         elif stageSelect == "q" or stageSelect == "Q":
            exit

   def stage3():
      global USR_CPU_CORES
      global USR_TARGET_OS
      global customValue
      global currentStage
      defaultValue = 2


      if USR_TARGET_OS >= 11 and USR_TARGET_OS <= 99:
         USR_TARGET_OS = USR_TARGET_OS * 100

      clear()
      print("\n   "+color.BOLD+"Set number of CPU cores"+color.END)
      print("   Step 3")
      print("\n   Set the desired number of virtual CPU cores. \n   More cores can dramatically improve guest performance if\n   your host can handle it."+color.END)
      print("\n   "+color.BOLD+color.CYAN+"DEFAULT:",color.END+color.BOLD,defaultValue,color.END)
      if customValue == 1:
         print(color.BOLD+color.PURPLE+"\n   FORMAT:"+color.YELLOW+""+color.END+color.BOLD,"<number>"+color.YELLOW+""+color.END+"\n   Enter a custom value.\n   \n   ")
      #   print(color.BOLD+color.PURPLE+"\n   FORMAT:"+color.YELLOW+""+color.END+color.BOLD,"<number>"+color.YELLOW+""+color.END+"\n   Enter a custom value. You",color.UNDERLINE+color.BOLD+"must"+color.END,"include any text in"+color.YELLOW,"yellow"+color.END+".\n   \n   ")
         customInput = int(input(color.BOLD+"Value> "+color.END))
         USR_CPU_CORES = customInput               #+".sh" #<--- change required prefix/suffix
         currentStage = currentStage + 1
         customValue = 0
         blob = open("./blobs/USR_CPU_CORES.apb","w")
         blob.write(str(USR_CPU_CORES))
         blob.close()
         stage4()
      else:
         print(color.BOLD+"\n      1. Use default value")
         print(color.END+"      2. Custom value...")
         print(color.END+"      3. Back")
         print(color.END+"      Q. Exit\n   ")
         stageSelect = str(input(color.BOLD+"Select> "+color.END))
      
         if stageSelect == "1":
            USR_CPU_CORES = defaultValue
            blob = open("./blobs/USR_CPU_CORES.apb","w")
            blob.write(str(USR_CPU_CORES))
            blob.close()
            currentStage = currentStage + 1
            stage4()

         elif stageSelect == "2":
            customValue = 1
            stage3()

         elif stageSelect == "3":
            currentStage = 1
            stage2()
            
         elif stageSelect == "q" or stageSelect == "Q":
            exit

   def stage2():
      global USR_TARGET_OS
      global customValue
      global currentStage
      defaultValue = 1015

      clear()
      print("\n   "+color.BOLD+"Set target OS"+color.END)
      print("   Step 2")
      print("\n   This is only really important for networking. \n   If you are installing macOS Mojave (10.14) or later, you can leave this alone.\n   If you are installing macOS High Sierra (10.13) or earlier, enter it as a custom value."+color.END)
      print("\n   "+color.BOLD+color.CYAN+"DEFAULT:",color.END+color.BOLD,defaultValue,color.END)
      if customValue == 1:
         print(color.BOLD+color.PURPLE+"\n   FORMAT:"+color.YELLOW+""+color.END+color.BOLD,"<number>"+color.YELLOW+""+color.END+"\n   Enter a custom value.\n   \n   ")
         customInput = int(input(color.BOLD+"Value> "+color.END))
         USR_TARGET_OS = customInput               #+".sh" #<--- change required prefix/suffix
         currentStage = 3
         customValue = 0
         blob = open("./blobs/USR_TARGET_OS.apb","w")
         blob.write(str(USR_TARGET_OS))
         blob.close()
         stage3()
      else:
         print(color.BOLD+"\n      1. Use default value")
         print(color.END+"      2. Custom value...")
         print(color.END+"      3. Back")
         print(color.END+"      Q. Exit\n   ")
         stageSelect = str(input(color.BOLD+"Select> "+color.END))
      
         if stageSelect == "1":
            USR_TARGET_OS = defaultValue
            blob = open("./blobs/USR_TARGET_OS.apb","w")
            blob.write(str(USR_TARGET_OS))
            blob.close()
            currentStage = 3
            stage3()

         elif stageSelect == "2":
            customValue = 1
            stage2()

         elif stageSelect == "3":
            currentStage = 1
            stage1()
            
         elif stageSelect == "q" or stageSelect == "Q":
            exit   

   def stage1():
      global USR_CFG
      global customValue
      global currentStage

      # remove stale blobs
      os.system("mv -f ./blobs/*.apb ./blobs/stale/")
      os.system("mv -f /blobs/CDN_CONTROL ./blobs/stale/")

      clear()

      print("\n   "+color.BOLD+"Name your config file"+color.END)
      print("   Step 1")
      print("\n   This is simply the name of your config file. \n   You can name it whatever you want. It's used to boot your\n   VM and will be the basis of this AutoPilot configuration."+color.END)
      if customValue == 1:
         print("\n   "+color.BOLD+color.CYAN+"DEFAULT:",color.END+color.BOLD+"boot.sh"+color.END)
         print(color.BOLD+color.PURPLE+"\n   FORMAT:"+color.YELLOW+""+color.END+color.BOLD,"<filename>"+color.YELLOW+".sh"+color.END+"\n   Enter a custom value. You",color.UNDERLINE+color.BOLD+"must"+color.END,"include any text in"+color.YELLOW,"yellow"+color.END+".\n\n")
         customInput = str(input(color.BOLD+"Value> "+color.END))
         USR_CFG = customInput               #+".sh" #<--- change required prefix/suffix
         currentStage = 2
         customValue = 0
         blob = open("./blobs/USR_CFG.apb","w")
         blob.write(USR_CFG)
         blob.close()
         stage2()

      else:
         print("\n   "+color.BOLD+color.CYAN+"DEFAULT:",color.END+color.BOLD+"boot.sh"+color.END)
         print(color.BOLD+"\n      1. Use default value")
         print(color.END+"      2. Custom value...")
         print(color.END+"      Q. Exit\n")
         stageSelect = str(input(color.BOLD+"Select> "+color.END))
      
         if stageSelect == "1":
            USR_CFG = "boot.sh"
            blob = open("./blobs/USR_CFG.apb","w")
            blob.write(USR_CFG)
            blob.close()
            currentStage = 2
            stage2()

         elif stageSelect == "2":
            customValue = 1
            stage1()

         elif stageSelect == "q" or stageSelect == "Q":
            exit


   global PROC_PREPARE
   global PROC_CHECKBLOBS
   global PROC_GENCONFIG
   global PROC_LOCALCOPY
   global PROC_FETCHDL
   global PROC_GENHDD
   global PROC_APPLYPREFS
   global PROC_FIXPERMS
   global PROC_CLEANUP

   PROC_PREPARE = 0
   PROC_CHECKBLOBS = 0
   PROC_GENCONFIG = 0
   PROC_LOCALCOPY = -1
   PROC_FETCHDL = -1
   PROC_GENHDD = 0
   PROC_APPLYPREFS = 0
   PROC_FIXPERMS = 0
   PROC_CLEANUP = 0


   def handoff():
      global PROC_PREPARE
      global PROC_CHECKBLOBS
      global PROC_GENCONFIG
      global PROC_LOCALCOPY
      global PROC_FETCHDL
      global PROC_GENHDD
      global PROC_APPLYPREFS
      global PROC_FIXPERMS
      global PROC_CLEANUP

      PROC_PREPARE = 0
      PROC_CHECKBLOBS = 0
      PROC_GENCONFIG = 0
      PROC_LOCALCOPY = -1
      PROC_FETCHDL = -1
      PROC_GENHDD = 0
      PROC_APPLYPREFS = 0
      PROC_FIXPERMS = 0
      PROC_CLEANUP = 0

      clear()
      time.sleep(3)


      if USR_BOOT_FILE == "-1":
         PROC_FETCHDL = 0
         PROC_LOCALCOPY = -1
      elif USR_BOOT_FILE != "-2":
         PROC_FETCHDL = -1
         PROC_LOCALCOPY = 0

      def refreshStatusGUI():
         clear()
         print("   "+"\n   "+color.BOLD+"Status"+color.END)
         print("   "+"AutoPilot is performing the requested actions.")
         print("   "+"\n   This may take a few moments."+color.END)
         print("   "+"\n   "+color.BOLD+"──────────────────────────────────────────────────────────────",color.END)

         if PROC_PREPARE == 0:
            print("      "+color.BOLD+color.RED+"● ",color.END+color.END+"Preparing files"+color.END)
         elif PROC_PREPARE == 1:
            print("      "+color.BOLD+color.YELLOW+"● ",color.END+color.BOLD+"Preparing files"+color.END)
         elif PROC_PREPARE == 2:
            print("      "+color.BOLD+color.GREEN+"● ",color.END+color.END+"Preparing files"+color.END)

         if PROC_CHECKBLOBS == 0:
            print("      "+color.BOLD+color.RED+"● ",color.END+color.END+"Checking preferences"+color.END)
         elif PROC_CHECKBLOBS == 1:
            print("      "+color.BOLD+color.YELLOW+"● ",color.END+color.BOLD+"Checking preferences"+color.END)
         elif PROC_CHECKBLOBS == 2:
            print("      "+color.BOLD+color.GREEN+"● ",color.END+color.END+"Checking preferences"+color.END)

         if PROC_GENCONFIG == 0:
            print("      "+color.BOLD+color.RED+"● ",color.END+color.END+"Generating config script"+color.END)
         elif PROC_GENCONFIG == 1:
            print("      "+color.BOLD+color.YELLOW+"● ",color.END+color.BOLD+"Generating config script"+color.END)
         elif PROC_GENCONFIG == 2:
            print("      "+color.BOLD+color.GREEN+"● ",color.END+color.END+"Generating config script"+color.END)

         if PROC_LOCALCOPY == 0:
            print("      "+color.BOLD+color.RED+"● ",color.END+color.END+"Copying recovery image into place"+color.END)
         elif PROC_LOCALCOPY == 1:
            print("      "+color.BOLD+color.YELLOW+"● ",color.END+color.BOLD+"Copying recovery image into place"+color.END)
         elif PROC_LOCALCOPY == 2:
            print("      "+color.BOLD+color.GREEN+"● ",color.END+color.END+"Copying recovery image into place"+color.END)

         if PROC_FETCHDL == 0:
            print("      "+color.BOLD+color.RED+"● ",color.END+color.END+"Downloading recovery image"+color.END)
         elif PROC_FETCHDL == 1:
            print("      "+color.BOLD+color.YELLOW+"● ",color.END+color.BOLD+"Downloading recovery image"+color.END)
         elif PROC_FETCHDL == 2:
            print("      "+color.BOLD+color.GREEN+"● ",color.END+color.END+"Downloading recovery image"+color.END)

         if PROC_GENHDD == 0:
            print("      "+color.BOLD+color.RED+"● ",color.END+color.END+"Creating virtual hard disk"+color.END)
         elif PROC_GENHDD == 1:
            print("      "+color.BOLD+color.YELLOW+"● ",color.END+color.BOLD+"Creating virtual hard disk"+color.END)
         elif PROC_GENHDD == 2:
            print("      "+color.BOLD+color.GREEN+"● ",color.END+color.END+"Creating virtual hard disk"+color.END)

         if PROC_APPLYPREFS == 0:
            print("      "+color.BOLD+color.RED+"● ",color.END+color.END+"Applying preferences"+color.END)
         elif PROC_APPLYPREFS == 1:
            print("      "+color.BOLD+color.YELLOW+"● ",color.END+color.BOLD+"Applying preferences"+color.END)
         elif PROC_APPLYPREFS == 2:
            print("      "+color.BOLD+color.GREEN+"● ",color.END+color.END+"Applying preferences"+color.END)

         if PROC_FIXPERMS == 0:
            print("      "+color.BOLD+color.RED+"● ",color.END+color.END+"Fixing up permissions"+color.END)
         elif PROC_FIXPERMS == 1:
            print("      "+color.BOLD+color.YELLOW+"● ",color.END+color.BOLD+"Fixing up permissions"+color.END)
         elif PROC_FIXPERMS == 2:
            print("      "+color.BOLD+color.GREEN+"● ",color.END+color.END+"Fixing up permissions"+color.END)

         if PROC_CLEANUP == 0:
            print("      "+color.BOLD+color.RED+"● ",color.END+color.END+"Cleaning up"+color.END)
         elif PROC_CLEANUP == 1:
            print("      "+color.BOLD+color.YELLOW+"● ",color.END+color.BOLD+"Cleaning up"+color.END)
         elif PROC_CLEANUP == 2:
            print("      "+color.BOLD+color.GREEN+"● ",color.END+color.END+"Cleaning up"+color.END)

         print("   "+color.BOLD+"──────────────────────────────────────────────────────────────\n\n\n",color.END)

      refreshStatusGUI()

      time.sleep(3)

      def apcPrepare():# PREPARE
         global PROC_PREPARE
         PROC_PREPARE = 1
         global errorMessage
         errorMessage = "Couldn't prepare files. (Insufficient permissions?)"
         refreshStatusGUI()
         os.system("cp resources/baseConfig resources/config.sh")
         time.sleep(2)
         integrityConfig = 1
         if os.path.exists("resources/config.sh"):
            integrityConfig = integrityConfig + 0
         else:
            integrityConfig = integrityConfig - 1
            throwFail()
         PROC_PREPARE = 2
         refreshStatusGUI()

      def apcBlobCheck():      # CHECK BLOBS
         global PROC_CHECKBLOBS
         PROC_CHECKBLOBS = 1
         global errorMessage
         errorMessage = "The integrity of the wizard preference files could not be verified."
         integrity = 1
         refreshStatusGUI()
         time.sleep(4)
         if os.path.exists("blobs/USR_ALLOCATED_RAM.apb"):
            integrity = integrity + 0
         else:
            integrity = integrity - 1
            #print("DEBUG: FOUND")
         if os.path.exists("blobs/USR_BOOT_FILE.apb"):
            integrity = integrity + 0
         else:
            integrity = integrity - 1
         if os.path.exists("blobs/USR_CFG.apb"):
            integrity = integrity + 0
         else:
            integrity = integrity - 1
         if os.path.exists("blobs/USR_CPU_CORES.apb"):
            integrity = integrity + 0
         else:
            integrity = integrity - 1
         if os.path.exists("blobs/USR_CPU_FEATURE_ARGS.apb"):
            integrity = integrity + 0
         else:
            integrity = integrity - 1
         if os.path.exists("blobs/USR_CPU_MODEL.apb"):
            integrity = integrity + 0
         else:
            integrity = integrity - 1
         if os.path.exists("blobs/USR_CPU_THREADS.apb"):
            integrity = integrity + 0
         else:
            integrity = integrity - 1
         if os.path.exists("blobs/USR_HDD_SIZE.apb"):
            integrity = integrity + 0
         else:
            integrity = integrity - 1
         if os.path.exists("blobs/USR_NETWORK_DEVICE.apb"):
            integrity = integrity + 0
         else:
            integrity = integrity - 1
         if os.path.exists("blobs/USR_TARGET_OS.apb"):
            integrity = integrity + 0
         else:
            integrity = integrity - 1

         if integrity == 1:
            PROC_CHECKBLOBS = 2
            refreshStatusGUI()
         else:
            throwFail()

      def apcGenConfig():
         global PROC_GENCONFIG
         PROC_GENCONFIG = 1
         global errorMessage
         errorMessage = "The config file could not be written to."
         integrity = 1
         refreshStatusGUI()
         time.sleep(4)



      apcPrepare()
      apcBlobCheck()
      apcGenConfig()

   stage1()

if detectChoice == 1:
   autopilot()
elif detectChoice == 2:
    os.system('./setup.py')

elif detectChoice == 3:
    exit
