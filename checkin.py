#!/usr/bin/env python
# coding=utf-8
# Created Time:    2019-05-29 09:34:40
# Modified Time:   2019-05-29 09:40:21

import time
import random
from selenium import webdriver
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger


def check_in():
    # config url,name,password
    url = ""
    name = ""
    password ""

    print("start check in.")
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome("./chromedriver")
    driver.maximize_window()
    driver.get(url)
    driver.find_element("name", "username").send_keys(name)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element_by_css_selector("input.formsubmit_btn").submit()
    time.sleep(random.randint(5, 20))

    driver.find_element("id", "clockLink").click()
    driver.quit()
    print("quit")


if __name__ == '__main__':
    h = 21
    m = random.randint(5, 10)
    s = random.randint(20, 50)
    scheduler = BlockingScheduler()
    print(h, ":", m, ":", s)
    trigger = CronTrigger(hour=h, minute=m, second=s)
    scheduler.add_job(check_in, trigger)
    scheduler.start()


