import threading
from queue import Queue

from spider import Spider
from domain import *
from general import *


PROJECT_NAME = 'imdb'
HOME_PAGE = 'https://imdb.com/'
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8


# Thread Queue
queue = Queue()     # Queue of jobs

Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)


# Create a worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target = work)
        t.daemon = True     # die when main exits
        t.start()

# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()       # Job is done

# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)     # Adding job to job queue
    queue.join()
    crawl()

# Crawl the items in the queue
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print("{} links in the queue.".format(len(queued_links)))
        create_jobs()


create_workers()
crawl()