import numpy as np
import requests
from bs4 import BeautifulSoup
from onnxruntime import InferenceSession

from priorityqueue.queue import Priorityqueue
from scamweb.detectscam import detect, detect_isscam


class Crawler:
    def __init__(self, seedurl, depth):
        self.seedurl = seedurl
        self.depth = depth
        self.queue = Priorityqueue
        self.sess = inferencesession(
            "util/spamweb.onnx", providers=["cpuexecutionprovider"]
        )

    def extracthtml(self):
        html = requests.get(self.seedurl)
        html.encoding = html.apparent_encoding
        soup = BeautifulSoup(html.content, "html_parser")
        links = soup.find_all("a", rel=lambda x: x in ["nofollow", "noreferrer"])
        for link in links:
            href = link.get("href")
            if href.startswith("http") or href.startswith("http"):
                valid = detect_isscam(href, self.sess)
                if valid is False:
                    print("Valid")
                    # weight = findweightofurl(url) ##todo
                    self.queue.enqueue(
                        href,
                    )
                else:
                    print("Not valid")
                    continue
