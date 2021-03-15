"""
author: Michael Ndon
title: Blackfridayscrape
subject-website: weworkremotely.com // remote.io
description: collates job postings by category

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import csv
import time

STARTPAGE = 'https://weworkremotely.com/remote-jobs/search'
PATH = './assets/chromedriver.exe'
FOLDER = 'findings'
categories = ['Design', 'Programming', 'Customer Support', 'Copywriting', 'DevOps and Sysadmin', 
                'Sales and Marketing', 'Business, Management and Finance', 'Product']


class Search():
    def __init__(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(STARTPAGE)
        self.search_window = driver.window_handles[0]