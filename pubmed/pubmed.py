import urllib
import json
import requests
import time
import asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class PubMedInfo():
    def __init__(self, KeywordList):
        self.target_urls = []
        self.start_url = 'https://www.ncbi.nlm.nih.gov/pubmed/?term='
        self.base_url = 'https://www.ncbi.nlm.nih.gov'
        self.temp = [urllib.parse.quote(i) for i in KeywordList]
        self.keyword = '%2C'.join(self.temp)
        self.url = self.start_url + self.keyword
        self.browser = webdriver.Chrome()
        self.browser.get(self.url)
        self.wait = WebDriverWait(self.browser, 10)

    def page_size_click(self):
        perpage = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//ul[@class="inline_list left display_settings"]/li[3]/a/span[4]')))
        perpage.click()
        page_200 = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#display_settings_menu_ps > fieldset > ul > li:nth-child(6) > label')))
        page_200.click()

    def next_page(self):
        try:
            nextpage = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title="Next page of results"]')))
            nextpage.click()
        except TimeoutException:
            self.next_page()

    def get_target_urls(self):
        html = self.browser.page_source
        soup = BeautifulSoup(html, "html5lib")
        for link in soup.find_all('a'):
            if(link.get('href') is not None and  len(link.get('href')) > 10 and link.get('href')[:10] == '/pubmed/31'): 
                self.target_urls.append(self.base_url + link.get('href')) 

    def gethtmltext(self, url):
        try:
            r = requests.get(url)
            r.raise_for_status()
            r.encoding = 'utf-8'
            return r.text
        except:
            return ""

    def fillfile(self, html, soup, counter):
        try:
            # with open(str(counter) + ". " + soup.find_all('h1')[1].get_text() + '.txt', 'w+') as f:
            #     f.write(soup.find('div', 'abstr').get_text()[8:])
            print(str(counter) + ". " + soup.find_all('h1')[1].get_text())
        except:
            pass

    def get_abstract(self, link, counter):
        html = self.gethtmltext(link)
        soup = BeautifulSoup(html, "html5lib")
        self.fillfile(html, soup, counter)

    def main(self):
        self.page_size_click()
        for i in range(1):
            self.get_target_urls()
            print(len(self.target_urls))
            # if i != 2:
            #     self.next_page()
        self.target_urls = list(set(self.target_urls))
        print("---------------------------")    
        print("去重后剩余：")
        print(len(self.target_urls))
        for link, counter in zip(self.target_urls, range(1, 1600)):
            self.get_abstract(link, counter) 

if __name__ == '__main__':
    a = PubMedInfo(['virus'])
    a.main()