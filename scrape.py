from bs4 import BeautifulSoup
import requests
import time
from csv import writer

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=C%2B%2B&txtLocation='  #change URL here

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')  #Just want company name , skill , go to inspect and find infomation that u want and change html tags , class

with open('csv/test1.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Company Name', 'Skill']
    thewriter.writerow(header)
    for job in jobs:
        comp_name = job.find('h3', class_='joblist-comp-name').text.replace('\n', '')
        skill = job.find('span', class_='srp-skills').text.replace('\n', '')

        info = [comp_name, skill]
        thewriter.writerow(info)