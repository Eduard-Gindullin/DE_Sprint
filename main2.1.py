for page in range(0,1):
    time.sleep(2)
    url = 
    headers = {'User-Agent': }
    resp = rt.get(url, headers=headers)
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
 #       tag_sal=soup_object.find(attrs={"data-qa":"vacancy-salary"}) 
 #       data["data"].append({"Title":iter.text, "Salary":tag_price, "Region":tag_region})