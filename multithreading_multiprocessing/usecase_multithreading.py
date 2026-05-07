''' 
Real world example : Multithreading for I/O bound Tasks
Scenario : Web Scraping
Web scraping often involves making numerous network requests to 
fetch web pages.These tasks are I/O boud because they spend a lot of 
time waiting for reponses from servers , Multithreading can significantly
improve the performance by allowing multiple web pages to be fetch concurrently.

'''

'''
https://docs.langchain.com/langsmith/observability

https://docs.langchain.com/langsmith/observability-llm-tutorial

https://docs.langchain.com/langsmith/observability-concepts

'''

import threading
import requests


from bs4 import BeautifulSoup

urls = [
    'https://docs.langchain.com/langsmith/observability',
    'https://docs.langchain.com/langsmith/observability-llm-tutorial',
    'https://docs.langchain.com/langsmith/observability-concepts'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content , 'html.parser')
    print(f'Fetches {(len(soup.text))}  characters from {url}')

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")