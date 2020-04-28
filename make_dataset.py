from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
import urllib
file_path="folder/"
url="https://safebooru.org/index.php?page=post&s=list"

def dl_jpg(url,full_path):
    urllib.request.urlretrieve(url, full_path)

html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
for i,image in tqdm(enumerate(images)): 
    name="webpage{}".format(i)
    full_path=file_path+name+'.jpg'
    dl_jpg(image['src'],full_path)
