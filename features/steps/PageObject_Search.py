#!/usr/bin/python
# -*- coding: utf-8 -*-


from page_objects import PageObject, PageElement
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

delay_min = 3  # sec
delay_medium = 5  # sec
delay_max = 9  # sec


class SearchPage(PageObject):
    text_box_searchkey = PageElement(xpath="//div[@id='sb_ifc0']/div[1]/input[@title='Search']")
    drop_down_option = PageElement(xpath="//div[@id='sb_ifc0']/div[1]/input[@title='Search']")
    search_button = PageElement(xpath="//div[@class='tsf-p']/div[3]/center/input[@value= 'Google Search']")

    # result_count = PageElement(xpath="//div[@id='rso']/div/div[1]")


    """
    Launching the Google.co.in to perform search
    """
    def method_search_page_launch_search_url(self, current_web_driver, url_search_page):
        self.get(url_search_page)
        # time.sleep(delay_max)
        WebDriverWait(current_web_driver, delay_max).until(expected_conditions.title_contains('Google'))
        return

    """
        Here Im performing a search of https://www.instawork.com/ and waiting for the search result 
        and matching the entered search is present in the url 
    """
    def method_search_page_search(self, current_web_driver):
        self.text_box_searchkey = 'https://www.instawork.com/'
        self.search_button.click()
        WebDriverWait(current_web_driver, delay_medium).until(expected_conditions.url_contains('www.instawork.com'))
        return

    """
    check_exists_by_xpath function is to find if the searched link is present in the page and print all the 
    links of format " https://www.instawork.com/" and print the position . with position 0 being the first search link
    
    """

    @staticmethod
    def check_exists_by_xpath(current_web_driver):
        # print("check this execution")
        elems = current_web_driver.find_elements_by_xpath("//a[starts-with(@href,'https://www.instawork.com/')]")
        count_pos = 0
        for elem in elems:
            link = elem.get_attribute("href")
            print(link)
            if link == "https://www.instawork.com/":
                print("The link is %s and is present at position %s" % (link, count_pos))
            else:
                count_pos = count_pos + 1

