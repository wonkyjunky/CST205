import json
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
import cv2


r = requests.get('https://www.instagram.com/explore/tags/bs4testcoding/')
soup = BeautifulSoup(r.text, 'lxml')

script = soup.find('script', text=lambda t: t.startswith('window._sharedData'))
page_json = script.text.split(' = ', 1)[1].rstrip(';')
data = json.loads(page_json)

for post in data['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']:
    image_src = post['node']['display_url']


a = urlopen("https://scontent-lax3-1.cdninstagram.com/vp/7a6b73f765f781bdeb2896c968c36f40/5E2B52C0/t51.2885-15/e35/s1080x1080/74711756_418939425354973_6313057521815563604_n.jpg?_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=101")
image = np.asarray(bytearray(a.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)

img_remap = cv2.applyColorMap(image, cv2.COLORMAP_OCEAN)
cv2.imshow("Original", img_remap) 
cv2.waitKey(7000)