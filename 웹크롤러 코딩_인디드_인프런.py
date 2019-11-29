#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
from time import sleep
from collections import Counter
import requests
import bs4
from bs4 import BeautifulSoup
import time
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

#skillset dictionary
#thanks to 'https://github.com/yuanyuanshi/Data_Skills' for this dictionary idea
program_languages=['R','Python','Java','C++','C','C#','Ruby','Perl','Matlab','Javascript','Scala','PHP','Julia']
analysis_software=['Excel','Tableau','D3.js','SAS','SPSS','SAAS','Pandas','Numpy','SciPy','SPS','Spotfire','Scikits-learn','Splunk','H2O']
bigdata_tool=['Hadoop','MapReduce','Spark','Pig','Apache Hive','HiveQL','Shark','Oozie','Zookeeper','Flume','Apache Mahout']
databases=['SQL','NoSQL','HBase','Cassandra','MongoDB','MySQL','MSSQL','PostgreSQL','Oracle DB','RDBMS']
overall_dict = program_languages + analysis_software + bigdata_tool + databases

#indeed webcrawler
#thanks to 'https://medium.com/@msalmon00/web-scraping-job-postings-from-indeed-96bd588dcb4b' for this fuction
max_results_per_city = 20
city_set = ['New+York', 'San+Francisco']
job_post=[] 

for city in city_set :
    for start in range(0,max_results_per_city,10):
        page = requests.get('https://www.indeed.com/jobs?q=data+scientist&l='+str(city)+ '&start=' + str(start))
        html = page.text
        time.sleep(1)
        soup = BeautifulSoup(html, "lxml")
        for div in soup.find_all(name="div", attrs={"class":"summary"}):
            job_post.append(div.text.strip())
            
words=[]

#extracting words that are not stopwords
for text in job_post :
    tokenizer = RegexpTokenizer(r'\w+')
    text_no_punc = tokenizer.tokenize(text)
    text = list(set(w for w in text_no_punc if w.lower() not in stopwords.words()))
    words.append(text)

ntext=sum(words,[])
keywords=[str(word) for word in ntext if word in overall_dict]

#top 5 keywords analysis by counting words that match skillset dictionary
from collections import Counter
word_count_dict = Counter(keywords)
word_count_dict.most_common(5)
tmp_key=dict(word_count_dict.most_common(5))
inflearn_key=list(tmp_key.keys())
inflearn_key


# inflearn webcrawler + result print

skills = inflearn_key
for skill in skills :
    num1=0
    print("================="+skill+"=================")
    page = requests.get('https://www.inflearn.com/courses?order=search&s='+str(skill))
    html = page.text
    time.sleep(1)
    soup = BeautifulSoup(html, "lxml")
    
    prices=soup.find_all(name='div', attrs={"class":"price has-text-right column is-half"})
    
    for course_name in soup.find_all(name='div', attrs={"class":"course_title"}):
        print(course_name.text.strip() + "   " + prices[num1].text.strip())
        num1=num1+1
        
    print("===========================================")





