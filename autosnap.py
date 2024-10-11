#imports
import os
import time
import tkinter
import threading
import sys
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, WebDriverException

#establish tkinter root
root = tkinter.Tk()

#run selenium function
def run(run_autosnap):

    #destroy window
    root.destroy()

    #establish driver and option variables
    options = Options()
    options.add_argument(r"--user-data-dir=/autosnapedgedata")
    options.add_argument("--log-level=1")
    driver = webdriver.Edge(options=options)
    driver.implicitly_wait(30)
    driver.get("https://web.snapchat.com")
    driver.maximize_window()

    if run_autosnap == True:

        while True:

            try:

                #find new_snap_buttons
                new_snap_buttons = driver.find_elements(By.XPATH , "//*[contains(text(), 'New')]")
                print("There are" , len(new_snap_buttons)  , "New snap buttons")

                #click buttons
                for new_snap_button in new_snap_buttons:

                    #wait 1 second
                    time.sleep(1)
                    
                    #click new_snap_button
                    new_snap_button.click()
                    print("Clicked New Snap Button")

                    #wait 1 second
                    time.sleep(1)

                    #test for delivered
                    snaps = driver.find_elements(By.XPATH , "//div[contains(@class, 'y2oqI')]")
                    most_recent_snap = snaps[-1]
                    most_recent_snap_classes = most_recent_snap.get_attribute("class")
                    if "RyV83" not in most_recent_snap_classes and "ZSE8T" in most_recent_snap_classes: #   delivered = y2oqI RyV83 ZSE8T   opened = y2oqI   new snap = y2oqI ZSE8Ts
                        delivered_is_last = False
                    else:
                        delivered_is_last = True

                    #wait 1 second
                    time.sleep(1)
                    
                    if delivered_is_last == False:
                        #find and click camera_button
                        camera_button = driver.find_element (By.XPATH , "//button[contains(@class, 'cDumY') and contains(@class, 'EQJi_') and contains(@class, 'eKaL7') and contains(@class, 'Bnaur')]")
                        camera_button.click()
                        print("Camera Button Clicked")

                        #wait 1 second
                        time.sleep(1)

                        #find and click shutter_button
                        shutter_button = driver.find_element (By.XPATH , "//button[contains(@class, 'FBYjn') and contains(@class, 'gK0xL') and contains(@class, 'A7Cr_') and contains(@class, 'm3ODJ')]")
                        shutter_button.click()
                        print("Shutter Button Clicked")

                        #wait 1 second
                        time.sleep(1)

                        #find and click send_button
                        send_button = driver.find_element (By.XPATH , "//*[contains(text(), 'Send')]")
                        send_button.click()
                        print("Send Button Clicked")
                    else:
                        print("delivered last so skip")
                    
                    #crash_prevented_amount = 0

            except:
                mainpagediv = driver.find_elements (By.ID , "root")
                print("crash prevented")
                
    else:
        while True:
            mainpagediv = driver.find_elements (By.ID , "root")

#tkinter window
root.title("Auto Snap")
root.geometry("250x150")
root.resizable(False, False)
ttk.Label(root, text="For set up, open snapchat, sign in, and give camera access. Auto Snap might get blocked by a popup so check after you click run.", wraplength="230", justify="center").pack(ipadx="0" , ipady="0")
ttk.Button(root, text="Open Snapchat", command=lambda:run(run_autosnap=False)).pack(ipadx="20", ipady="5", expand=True)
ttk.Button(root, text="Run Auto Snap", command=lambda:run(run_autosnap=True)).pack(ipadx="20", ipady="5", expand=True)
root.mainloop()