import sys

from crawler.crawler import Crawler

if __name__ == "__main__":
    seed = sys.argv[1]
    print(seed)
    crawl = Crawler(seed, 4)
    crawl.start_crawl()
