import requests
from bs4 import BeautifulSoup
from onnxruntime import InferenceSession

from priorityqueue.queue import Priorityqueue
from scamweb.detectscam import detect_isscam
from weight.weight import findweight


class Crawler:
    def __init__(self, seedurl, depth):
        self.seedurl = seedurl
        self.depth = depth
        self.queue = Priorityqueue()
        self.sess = InferenceSession(
            "util/spamweb.onnx", providers=["CPUExecutionProvider"]
        )
        self.visited = set()

    def extracthtml(self, url):
        if url is None or url in self.visited or self.depth == 0:
            return
        try:
            html = requests.get(url)
            html.encoding = html.apparent_encoding
            soup = BeautifulSoup(html.content, "html.parser")
            links = soup.find_all("a")
            for link in links:
                href = link.get("href")
                if href and (href.startswith("http") or href.startswith("https")):
                    print(href)
                    valid = detect_isscam(href, self.sess)
                    if valid is False:
                        print("Valid")
                        weight = findweight(url)
                        self.queue.enqueue(href, weight)
                    else:
                        print("Not valid")
                        continue
                else:
                    continue
            self.visited.add(url)
            self.depth = self.depth - 1
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {url}: {e}")

    def start_crawl(self):
        self.queue.enqueue(self.seedurl, 0)

        while not self.queue.is_empty():
            next_url = self.queue.dequeue()
            self.extracthtml(next_url[0])
        print("Crawling complete")
