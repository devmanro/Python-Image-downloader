#!/usr/bin/env python3

import sys
if sys.version_info < (3, 0):
    raise SystemError("Please use python3\n")

import random
import time
import urllib.parse

try:
    import bs4 as bs
    import requests
except:
    raise ImportError("Please install beautifulsoup4 \n and requests modules for python3")

user_agents = [
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/61.0.3163.91 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/61.0.3163.79 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/62.0.3202.94 Safari/537.36 OPR/49.0.2725.56"]


class ImageDownloader:
    """scans a web page for all image links and downloads the images to a folder"""
    def __init__(self, url:str):
        self.url = url
        self.domain_name = urllib.parse.urlparse(self.url).hostname
        self.seq = 0

    def page_source(self):
        print("Trying to connect to page...")
        try:
            req = self.intermediate_connector(self.url)
        except:
            try:
                print("error reconnecting...")
                req = self.intermediate_connector(self.url)
            except:
                raise ConnectionError("Check Your Internet Connection and URL")
        #print(req)
        return req

    @staticmethod
    def intermediate_connector(link:str):
        time.sleep(random.randrange(1, 5))
        headers = {"User-Agent": random.choice(user_agents)}
        response = requests.get(link, headers=headers)
        print("Connected")
        return response.content
    
    def find_images(self):
        source = self.page_source()
        soup = bs.BeautifulSoup(source, 'lxml')
        for image in soup.find_all("img"):
            tmp = image.get("src")
            if tmp[:1] == "/":
                img_link = self.domain_name + tmp
            else:
                img_link = tmp
            self.seq += 1
            print("{} image found, starting downloading...".format(str(self.seq)))
            self.save_image(img_link)

    @staticmethod
    def get_file_type(img_link: str):
        if ".jpg" in img_link:
            print(".jpg")
            return ".jpg"
        elif ".png" in img_link:
            print(".png")
            return ".png"
        elif ".gif" in img_link:
            print(".gif")
            return ".gif"
        else:
            return None

    def save_image(self, img_link: str):
        time.sleep(random.randrange(1, 5))
        #img_link = "https://thechive.files.wordpress.com/2018/01/bikinis.jpg?quality=85&strip=info&w=600&h=450&crop=1"
        headers = {"User-Agent": random.choice(user_agents)}
        img_req = requests.get(img_link, stream=True, headers=headers)
        if img_req.status_code == 200:
            file_type = self.get_file_type(img_link)
            #print(img_link)
            #print(file_type)
            if file_type != None:
                print("image downloaded, saving to file...")
                with open(str(self.seq)+file_type, 'wb') as img_file:
                    for chunk in img_req :
                        img_file.write(chunk)
                print("image saved")
            else:
                print("not a supported image")

    
if __name__ == "__main__":
    url = ""
    ImageDownloader(url).find_images()
    
        
