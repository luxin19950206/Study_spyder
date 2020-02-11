from multiprocessing.dummy import Pool as ThreadPool
import threading
import requests
import time


def getsource(url):
    global hasViewed  # 修改全局变量,需要使用global关键字
    print(url)
    html = requests.get(url)
    hasViewed.append(url)


def threadGetSource(url):
    print(url)
    x = threading.Thread(target=getsource, args=(url,))  # 这里的args=(url,) 逗号是必须的,因为加了逗号才是只有一个元素的元组
    x.start()


urls = []
hasViewed = []

for i in range(1, 21):
    newpage = 'http://tieba.baidu.com/p/3522395718?pn={}'.format(i)
    urls.append(newpage)

# ==========单线程=====================================
time1 = time.time()
hasViewed = []
for i in urls:
    getsource(i)
print('单线程耗时：{}'.format(time.time() - time1))

# ============Python multiprocessing.dumpy多线程=======
pool = ThreadPool(20)
time3 = time.time()
hasViewed = []
results = pool.map(getsource, urls)
pool.close()
pool.join()
print('并行耗时：{}'.format(time.time() - time3))

# ======Python threading 多线程=======================
time5 = time.time()
hasViewed = []
[threadGetSource(url) for url in urls]
while not len(hasViewed) == 20:
    pass
print('thread并行耗时: {}'.format(time.time() - time5))
