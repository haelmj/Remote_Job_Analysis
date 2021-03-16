"""
author: Michael Ndon
title: Remote Job Scraper
subject-website: weworkremotely.com // remote.io
description: collates job postings by category

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import csv
import time

STARTPAGE = 'https://weworkremotely.com/remote-jobs/search'
PATH = os.getenv('CHROME_DRIVER')
FOLDER = 'findings'
categories = ['Design', 'Programming', 'Customer Support', 'Copywriting', 'DevOps and Sysadmin', 
                'Sales and Marketing', 'Business, Management and Finance', 'Product']


class Search():
    def __init__(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(STARTPAGE)
        self.search_window = self.driver.window_handles[0]

    def select_category(self, category):
        category_field = self.driver.find_element_by_xpath('/html/body/div[3]/header/section/form/div[2]/div[1]/div/ul/li/input')
        category_field.send_keys(category)
        category_field.send_keys(Keys.RETURN)
        search_button = self.driver.find_element_by_xpath('/html/body/div[3]/header/section/form/div[1]/button')
        search_button.send_keys(Keys.RETURN)
        time.sleep(10)

    def remove_category(self):
        # find selected category and remove it//optionally reset driver window
        pass

    def get_jobs(self, category):
        self.select_category(category)
        # scrape current category job listing

    def main(self):
        for category in categories:
            self.get_jobs(categories)
            # append category cleanup function

Search().main()