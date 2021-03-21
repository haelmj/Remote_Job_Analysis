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
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import csv
import time

STARTPAGE = 'https://weworkremotely.com/remote-jobs/search'
PATH = os.getenv('CHROME_DRIVER')
FOLDER = 'findings'
categories = ['Design', 'Programming', 'Customer Support', 'Copywriting', 'DevOps and Sysadmin', 
                'Sales and Marketing', 'Business, Management and Finance', 'Product']


class Search():
    """
    The Search object holds all job scraping related functionality

    Attributes:
        driver (WebDriver): Controls the ChromeDriver and allows you to drive the browser
        search_window (str): The starter page for all searches    
    """
    def __init__(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(STARTPAGE)
        self.search_window = self.driver.window_handles[0]

    def select_category(self, category: str, e_index: int):
        """Executes javascript to select category and clicks the search button
        
        Args:
            category(str):  The category to be selected.
            e_index(int):   The index of the category in it's list. 
        """
        self.driver.execute_script(open("category_selection.js").read(), category, e_index)
        search_button = self.driver.find_element_by_xpath('/html/body/div[3]/header/section/form/div[1]/button')
        search_button.send_keys(Keys.RETURN)
        time.sleep(6)

    def remove_category(self):
        """Search page for delete button on selected category and click it"""
        filter_reset_button = self.driver.find_element_by_xpath('/html/body/div[3]/header/section/form/div[2]/div[5]/span')
        filter_reset_button.click()
        time.sleep(6)

    def get_job_list(self, category: str, e_index: int):
        """Loop through the list of job postings and return list of job elements
        
        Args:
            category(str):  The category to be selected.
            e_index(int):   The index of the category in it's list.

        """
        self.select_category(category, e_index)
        job_section = self.driver.find_element_by_xpath('/html/body/div[3]/div/section')
        jobs = job_section.find_elements_by_tag_name('li')
        return jobs
    
    def get_jobs_info(self, jobs: list, category: str):
        """Loop through the list of jobs and extract individual job elements
        
        Args:
            jobs(list): A list containing job elements in the form of li webelements
        
        Returns:
            jobs_info(list): A 2-d list where each item is the info relating to a specific job.
        """
        jobs_info_section = [jobs[i].find_element_by_xpath(f'/html/body/div[3]/div/section/article/ul/li[{i+1}]/a') for i in range(len(jobs))]
        # extract content of anchor tags in each list item
        jobs_info = []
        for job in jobs_info_section:
            single_job_info = self.get_job_info(job, category)
            jobs_info.append(single_job_info)
        return jobs_info
            

    def get_job_info(self, job: WebElement, category: str):
        """Extract Job Info from a given element and return it in a list
        
        Args:
            job(WebElement): A webelement reference to a tag consisting of job info.
            category(str): The category the job fits into.
        
        Returns:
            info(list): A list containing the following info: company_name, title, job_type, region and category.
        """
        
        company_and_job_type = job.find_elements_by_class_name('company')
        company_name = company_and_job_type[0].get_attribute('textContent')
        job_type = company_and_job_type[1].get_attribute('textContent')
        title = job.find_element_by_class_name('title').get_attribute('textContent')
        try:
            region = job.find_element_by_css_selector('section.jobs article ul li span.region.company').get_attribute('textContent')
        except NoSuchElementException:
            region = ''
        return [company_name, title, job_type, region, category]
        
    def main(self):
        """Core method of class: executes entire workflow.

        Ports final gathered data to csv file.
        """
        columns = ['company', 'title', 'job-type', 'company-region', 'category']
        with open('data.csv', 'w', newline='', encoding='utf-8') as d_file:
            csv_writer = csv.writer(d_file)
            csv_writer.writerow(columns)

            for i in range(len(categories)):
                jobs = self.get_job_list(categories[i], i)
                jobs_info = self.get_jobs_info(jobs, categories[i])
                for info in jobs_info:
                    csv_writer.writerow(info)
                self.remove_category()

            
Search().main()