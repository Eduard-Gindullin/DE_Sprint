from bs4 import BeautifulSoup
from requests_tor import RequestsTor as reqt
import json
import tqdm
import time

data = {
    "data":[]
}

rt = reqt(tor_ports=(9050,), tor_cport=9051)

for page in range(0,1):
    time.sleep(2)
    url = f'https://hh.ru/search/vacancy?text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&salary=&clusters=true&no_magic=true&ored_clusters=true&enable_snippets=true&page={page}&hhtmFrom=vacancy_search_list'
    resp = rt.get(url)
    soup = BeautifulSoup(resp.text, "lxml")
    tags = soup.find_all("a",class_="serp-item__title")
    #(attrs={"data-qa":"bloko-header-3"})
#    print(tags)
    for iter in tqdm.tqdm(tags):
        time.sleep(2)
     #   links = [a['href'] for a in tags if a.has_key('href')]
     #   url_object = "https://hh.ru/" + iter.attrs["href"]
     #   resp_object = reqt.get(url_object)
        
        print(iter.text, iter.attrs['href'])

 #       soup_object = BeautifulSoup(resp_object.text, "lxml")
 #       tag_price = soup_object.find(attrs={"data-qa":"vacancy-salary-compensation-type-net"}).find_all().text
 #       tag_region = soup_object.find(attrs={"data-qa":"vacancy-serp__vacancy-address"}).find_all()[0].text 
 #       data["data"].append({"Title":iter.text, "Salary":tag_price, "Region":tag_region})
        







