
def type_of_img(filename):
    import imghdr 
    print(imghdr.what(filename))
#for websites
import urllib
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import re
import validators
from tqdm import tqdm
import requests
import  validators
import mimetypes
url="https://en.wikipedia.org/wiki/JPEG"

# downloads the images by taking url as input
def dl_jpg(url,full_path):
    urllib.request.urlretrieve(url, full_path)

def get_image_type(url):
    try:
      response = requests.get(url)
      content_type = response.headers['content-type']
      print(content_type)
      extension = mimetypes.guess_extension(content_type)
      if(extension!=None):
        return extension
    except:
        print("passed")
        return None


def dl_from_website(url,file_path):
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    html=urlopen(req).read()
    bs =BeautifulSoup(html,'html.parser')
    images=bs.find_all('img',{'src':re.compile(r'(jpe?g)|(png)$')})
    for i,image in tqdm(enumerate(images)):
        print(image['src'])
        extensions=get_image_type("https:"+image['src'])
        
       # print("===================="+extensions+"=================")
        if(extensions=='.png'):
            extension='.png'
        if(extensions=='.jpe'):
            extension='.jpg'
        try:
         name="webpage{}".format(i)
         full_path=file_path+name+extension
         dl_jpg("https:"+image['src'],full_path)
        except:
         #dl_jpg("http:"+image['src'],full_path)
         print(validators.url("https:"+image['src']))
         print("---------------------"+str(extension)+"----------------------------")

        
dl_from_website(url,'folder/')



#url="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg"
#url="https://www.zerochan.net/Garou+%28One+Punch+Man%29"
file_path="folder/"

            

# if extension!=None:
#     if(extension=='.png'):
#         print("png")
#         dl_from_website(url,file_path,extension)
#     if(extension=='.jpe'):
#         print("jpg")
#         dl_from_website(url,file_path,'.jpg')
#     else:
#         print(extension)

    
    
 # response = requests.get(url)
#content_type = response.headers['content-type']
#extension = mimetypes.guess_extension(content_type)

#google images
# import requests
# l=[]
# def download_google(word):
#     url = 'https://www.google.com/search?q=' + word + '&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'
#     page = requests.get(url).text
#     soup = BeautifulSoup(page, 'html.parser')

#     for raw_img in soup.find_all('img'):
#            link = raw_img.get('src')
#            type_of_img(link)

#download_google("dog")

# req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
# html=urlopen(req).read()
# bs =BeautifulSoup(html,'html.parser')
# #get_image_type()
# images=bs.find_all('img',{'src':re.compile(r'(jpe?g)|(png)$')})
# for img in images:
#     print(str(img['src'])+'\n')