#!/usr/bin/python
# -*- coding: utf-8 -*-


from selenium import webdriver
from PageObject_Search import *
from utilities_custom_usage import *

chrome_driver_path_used = '/Users/neethkunjappa/Documents/AssignmentIW/features/utilities/chromedriver'
firefox_driver_path_used = ''
delay_min = 3  # sec
delay_medium = 5  # sec
delay_max = 9  # sec


class HandleClassImpl:
    def __init__(self):
        pass

    def perform_initial_setup(self, global_list_variables,):
        print ('Performing initial set up, invoking browser')
        global_list_variables.append(webdriver.Chrome(executable_path=chrome_driver_path_used))
        # global_list_variables.append(webdriver.Firefox(executable_path=firefox_driver_path_used))
        global_list_variables[0].maximize_window()
        global_list_variables.append('success')
        return True

    def perform_some_action_on_search_page(self, global_list_variables, url_search_page):
        print ('Performing some action on search page')
        chrome_web_driver = global_list_variables[0]
        search_page = SearchPage(chrome_web_driver)
        search_page.method_search_page_launch_search_url(chrome_web_driver, url_search_page)
        search_page.method_search_page_search(chrome_web_driver, )
        search_page.check_exists_by_xpath(chrome_web_driver,)
        global_list_variables.append('success')
        return

    def final_verification(self, global_list_variables,):
        print ('Performing final verification for each step pass or fail')
        chrome_web_driver = global_list_variables[0]
        chrome_web_driver.close()
        chrome_web_driver.quit()
        compare_success = UtilitiesCustom()
        compare_success.method_utilities_compare_all_success_failure(global_list_variables)
        return


obj_handle_impl = HandleClassImpl()
