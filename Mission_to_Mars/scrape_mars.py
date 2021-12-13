import pandas as pd
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

mars_data = {}


def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # scrape news article
    url_one = 'https://redplanetscience.com/'
    browser.visit(url_one)
    time.sleep(2)
    html_one = browser.html
    article_soup = BeautifulSoup(html_one, 'html.parser')   
    news_title = article_soup.find('div', class_='content_title').text
    news_p = article_soup.find('div', class_='article_teaser_body').text

    #insert data into dictionary
    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p

    # browser.quit()
    # return mars_data

    # scrape feature image
    url_two = 'https://spaceimages-mars.com/'
    browser.visit(url_two)
    time.sleep(2)
    html_two = browser.html
    img_soup = BeautifulSoup(html_two, 'html.parser')
    feature_image = img_soup.find('img', class_='headerimage').get("src")
    feature_img_url= url_two + feature_image
    mars_data['feature_img_url'] = feature_img_url

    # browser.quit()
    # return mars_data

    # scrape mars facts
    url_three = 'https://galaxyfacts-mars.com/'
    browser.visit(url_three)
    time.sleep(2)
    # html_three = browser.html
    # facts_soup = BeautifulSoup(html_three, 'html.parser')
    mars_facts_df = ((pd.read_html(url_three))[0]).rename(columns={0: "Attribute", 1: "Mars", 2:"Earth"}).set_index(['Attribute'])
    fact_html_table = (mars_facts_df.to_html()).replace('\n', '')
    mars_data['fact_html_table'] = fact_html_table

    # scrape hemisphere data
    hemi1_url = 'https://marshemispheres.com/cerberus.html'
    browser.visit(hemi1_url)
    time.sleep(2)
    hemi1_html = browser.html
    hemi1_soup = BeautifulSoup(hemi1_html, 'html.parser')
    cerberus_title = hemi1_soup.find('h2', class_='title').text
    cerberus_img = hemi1_soup.find('img', class_='wide-image').get('src')
    cerberus_url = "https://marshemispheres.com/" + cerberus_img
    mars_data['cerberus_title'] = cerberus_title
    mars_data['cerberus_url'] = cerberus_url

    hemi2_url = 'https://marshemispheres.com/schiaparelli.html'
    browser.visit(hemi2_url)
    time.sleep(2)
    hemi2_html = browser.html
    hemi2_soup = BeautifulSoup(hemi2_html, 'html.parser')
    schiaparelli_title = hemi2_soup.find('h2', class_='title').text
    schiaparelli_img = hemi2_soup.find('img', class_='wide-image').get('src')
    schiaparelli_url = "https://marshemispheres.com/" + schiaparelli_img
    mars_data['schiaparelli_title'] = schiaparelli_title
    mars_data['schiaparelli_url'] = schiaparelli_url

    hemi3_url = 'https://marshemispheres.com/syrtis.html'
    browser.visit(hemi3_url)
    time.sleep(2)
    hemi3_html = browser.html
    hemi3_soup = BeautifulSoup(hemi3_html, 'html.parser')
    syrtis_major_title = hemi3_soup.find('h2', class_='title').text
    syrtis_major_img = hemi3_soup.find('img', class_='wide-image').get('src')
    syrtis_major_url = "https://marshemispheres.com/" + syrtis_major_img
    mars_data['syrtis_major_title'] = syrtis_major_title
    mars_data['syrtis_major_url'] = syrtis_major_url


    hemi4_url = 'https://marshemispheres.com/valles.html'
    browser.visit(hemi4_url)
    time.sleep(2)
    hemi4_html = browser.html
    hemi4_soup = BeautifulSoup(hemi4_html, 'html.parser')  
    valles_marineris_title = hemi4_soup.find('h2', class_='title').text
    valles_marineris_img = hemi4_soup.find('img', class_='wide-image').get('src')
    valles_marineris_url = "https://marshemispheres.com/" + valles_marineris_img
    mars_data['valles_marineris_title'] = valles_marineris_title
    mars_data['valles_marineris_url'] = valles_marineris_url

    # or do i need to append the hemisphere data to a list and then add that list to the mars_data?
    return mars_data

























