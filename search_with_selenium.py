#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Python 3


from selenium import webdriver
from time import sleep

import os
import subprocess
import traceback
import msvcrt


def moveControlToLastTab():
    handles = driver.window_handles
    size = len(handles)
    for x in range(size):
	    if handles[x] != driver.current_window_handle:
		    driver.switch_to.window(handles[x])

def moveCotrolToFirstTab():
    handles = driver.window_handles
    driver.switch_to.window(handles[0])

def getTabsTitle():
    handles = driver.window_handles
    size = len(handles)
    for x in range(size):
    	driver.switch_to.window(handles[x])
    	print(driver.title)
    

browserRunning = False
def opne_link(link):
    global browserRunning
    global driver
    
    if browserRunning:
        moveCotrolToFirstTab()
        moveControlToLastTab()
        driver.execute_script("window.open("+ "'" +link+ "'" +",'_blank')")
        moveControlToLastTab()
        sleep(0.3)

    else:
        print("wait a second ...")
        driver = webdriver.Firefox()    # if you are chrome user then chnage it to chrome
        driver.get(link)
        browserRunning = True



def help():
    print("""
     _____________________________________________________________________________________________
    |  keyword    |   website              keyword    |   website                                 |
    |  --------------------------          --------------------------                             |
    |  gg         |   google.com           error      |   google, stackoverflow, github           |
    |  yt         |   youtube.com                                                                 |
    |  stack      |   stackoverflow.com                                                           |
    |  w3         |   w3schools.com                                                               |
    |  gfg        |   geeksforgeeks.com                                                           |
    |  fb         |   facebook.com           --------------------------------------               |
    |  github     |   github.com             | 0          |   exit                |               |
    |  fb         |   facebook.com           | *restart   |   re open gecko       |               |
    |  wiki       |   wikipedia.com          | title      |   get all tabs title  |               |
    |  quora      |   quora.com              --------------------------------------               |
    |_____________________________________________________________________________________________|
    """)


def restart():
    print("wait a second ...")
    driver = webdriver.Firefox(executable_path=r'C:/Python38/geckodriver.exe')

def closeAllTabs():
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        driver.close()

def clickOnFirstSite():
    sleep(0.8)
    results = driver.find_elements_by_xpath('//div[@class="r"]/a/h3')  # finds webresults
    results[0].click() # clicks the first one

def google_search(search):
    print("searching...")
    link = 'https://www.google.com/'
    opne_link(link)
    search_field = driver.find_element_by_name("q")
    search_field.send_keys(search)
    search_field.submit()

def facebook_search(name):
    print("facebook...")
    link = 'https://www.google.com/'
    opne_link(link)
    search_field = driver.find_element_by_name("q")
    name = "facebook " + name
    search_field.send_keys(name)
    search_field.submit()

def instagram_search(name):
    print("Instagram...")
    link = 'https://www.google.com/'
    opne_link(link)
    search_field = driver.find_element_by_name("q")
    name = name + " instagram"
    search_field.send_keys(name)
    search_field.submit()
    clickOnFirstSite()

def twitter_search(name):
    print("twitter...")
    link = 'https://www.google.com/'
    opne_link(link)
    search_field = driver.find_element_by_name("q")
    name = name + " twitter"
    search_field.send_keys(name+" twitter")
    search_field.submit()
    clickOnFirstSite()

    
def w3schools_search(search):
    print("w3schools...")
    link = 'https://www.google.com/'
    opne_link(link)
    search_field = driver.find_element_by_name("q")
    search_field.send_keys("w3schools "+search)
    search_field.submit()
    clickOnFirstSite()

def geeksforgeeks_search(search):
    print("geeksforgeeks...")
    link = 'https://www.google.com/'
    opne_link(link)
    search_field = driver.find_element_by_name("q")
    search_field.send_keys("geeksforgeeks "+search)
    search_field.submit()
    clickOnFirstSite()

def linkdin_search(name):
    print("Linkedin...")
    link = 'https://www.google.com/'
    opne_link(link)
    search_field = driver.find_element_by_name("q")
    name = name + " linkedin"
    search_field.send_keys(name)
    search_field.submit()

def youtube_search(search):
    search = search.replace(' ', '+')
    print("Youtube search...")
    link = "https://www.youtube.com/results?search_query=" + search
    opne_link(link)

def stackoverflow_search(search):
    print("stackoverflow...")
    search = search.replace(' ','+')
    link = "https://stackoverflow.com/search?q=" + search
    opne_link(link)

def github_search(search):
    # if search word is less than 2 then its a name and greater then it is issue
    print("github...")
    search_type = "Issues" if len(search.split()) > 2 else "Users"
    link = "https://github.com/search?q=" + search + "&type=" + search_type
    opne_link(link)


    
def error_search(search):
    google_search(search)
    stackoverflow_search(search)
    github_search(search)


try:
    while 1:
        # asking
        my_string = input(":> ")
        first_word = my_string.split()[0]

        # exit
        if my_string == "0":
            closeAllTabs()
            exit(0)

        # google search
        elif first_word == "gg":
            google_search(my_string[3:])

        elif my_string == "help":
            help()

        elif my_string == "title":
            getTabsTitle()

        elif my_string == "restart":
            restart()

        # Youtube search
        elif first_word == "yt":
            youtube_search(my_string[3:])

        # stack for stackoverflow seacrh
        elif first_word == "stack":
            stackoverflow_search(my_string[len(first_word)+1:])


        elif first_word == "w3":
            w3schools_search(my_string[3:])

        elif first_word == "gfg":
            geeksforgeeks_search(my_string[4:])

        elif first_word == "error":
            error_search(my_string[len(first_word)+1:])

        # github for github search
        elif first_word == "github":
            github_search(my_string[7:])

        elif first_word == "fb":
            facebook_search(my_string[3:])

        # wiki for search in wikipedia
        elif first_word == "wiki":
            search = my_string[5:]
            search = search.replace(' ','+')
            link = "https://en.wikipedia.org/wiki/Special:Search?search="+search+"&go=Go&ns0=1"
            opne_link(link)
        # quora to quora search
        elif first_word == "quora":
            search = my_string[6:]
            search = search.replace(' ','+')
            link = "https://www.quora.com/search?q="+search
            opne_link(link)
        else:
            print("\n\tWrong input")
            print("\ttype help to see all commands\n")

except Exception:
    print("\n\n*********** ERROR ***********\n")
    traceback.print_exc()
    print("\nPress any key to continue...")
    msvcrt.getch()   




