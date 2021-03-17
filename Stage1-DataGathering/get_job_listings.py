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

    def select_category(self, category: str, e_index: int):
        self.driver.execute_script(open("category_selection.js").read(), category, e_index)
        search_button = self.driver.find_element_by_xpath('/html/body/div[3]/header/section/form/div[1]/button')
        search_button.send_keys(Keys.RETURN)
        time.sleep(6)

    def remove_category(self):
        """Search page for delete button on selected category and click it"""
        filter_reset_button = self.driver.find_element_by_xpath('/html/body/div[3]/header/section/form/div[2]/div[5]/span')
        filter_reset_button.click()
        time.sleep(6)

    def get_jobs(self, category: str, e_index: int):
        self.select_category(category, e_index)
        # scrape current category job listing
        job_section = self.driver.find_element_by_xpath('/html/body/div[3]/div/section')
        jobs = job_section.find_elements_by_tag_name('li')
        # add code to extract content of a href tags in each list
        # open csv file in write mode and append content to file...include the category as a column
        self.remove_category()

    def main(self):
        for i in range(len(categories)):
            self.get_jobs(categories[i], i)

            
Search().main()