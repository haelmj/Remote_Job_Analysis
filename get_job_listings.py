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
PATH = 'path_to_chrome_driver'
driver = webdriver.Chrome(PATH)

driver.get(STARTPAGE)
default_search_window = driver.window_handles[0]
FOLDER = 'findings'
