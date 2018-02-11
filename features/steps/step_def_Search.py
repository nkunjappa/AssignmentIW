#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import given, when, then
from step_impl_Search import *

global_list_variables = []


@given(u'Perform initial browser setup')
def step_impl(context, ):
    obj_handle_impl.perform_initial_setup(global_list_variables)


@when(u'Perform some action on search page "{url_search_page}"')
def step_impl(context, url_search_page):
    print(url_search_page)
    obj_handle_impl.perform_some_action_on_search_page(global_list_variables, url_search_page)


@then(u'All actions should be successful')
def step_impl(context, ):
    obj_handle_impl.final_verification(global_list_variables)
