#!/usr/bin/env/ python3 

from bs4 import BeautifulSoup
import requests

class UltaCrawler:
    def __init__(self):
        self.product_brand = []
        self.product_name = []
        self.old_price = []
        self.new_price = []
        self.url = "https://www.ulta.com/promotion/sale"

    def print_results(self):
        result_str = ""
        for i in range(len(self.product_brand)):
            result_str += ""+self.product_brand[i].rstrip()+": "+self.product_name[i]
            result_str += "Old price: "+self.old_price[i]+"\tSale price: "+self.new_price[i]+"\n\n"

        print(result_str)

    def scrape(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')

        item_list = soup.find_all("ul", id="foo16")

        for li in item_list:
            for item in li.find_all("li"):
                for product in item.find_all('div', attrs={"class":"prod-title-desc"}):
                    self.product_brand.append("".join(product.h4.text.strip())+"\n")
                    self.product_name.append("".join(product.p.text.strip())+"\n")

                for price in item.find_all('div', attrs={"class":"productPrice"}):
                    old_item_price = price.find_all('span', attrs={"class":"pro-old-price"})
                    new_item_price = price.find_all('span', attrs={"class":"pro-new-price"})
                    self.old_price.append(old_item_price[0].text.strip())
                    self.new_price.append(new_item_price[0].text.strip())

                if (len(self.product_brand) >= 10):
                    break;

        self.print_results()
        cont = input("")
