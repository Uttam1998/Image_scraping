# import required modules
import requests # for get requests
import re
from bs4 import BeautifulSoup as bs # for scraping
import os # for creating dirs & writing files,

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}



Image = 'women+dress' # the required image
url = 'https://www.bewakoof.com/search/' + Image # the Bewakoof api for searching a required image
x = 1 # set the var x to 0
filePath = 'images/' + Image # file path for the directory

# download page for parsing
page = requests.get(url=url, headers = headers) # get the url 
soup = bs(page.text, 'html.parser') # parse it with beautifulSoup, imported as bs, store it in soup var

# locate all elements with image tag
image_tags = soup.findAll('img') #for all format images
getStuff = soup.findAll('img', {'src' : re.compile(r'(jpe?g)$')}) #only for jpg format
# create directory for required images
if not os.path.exists(filePath): # if the dir doesn't exist
    os.makedirs(filePath) # create the dir

# move to new directory
os.chdir(filePath)

# writing images in the created folder
for image in getStuff: # for each image in the image_tags array,
	try: # go thru this loop
		url = image['src'] # set the url variable to the src of the image tags
		response = requests.get(url) # go to the url and store it in the response var
		if response.status_code == 200: # if the status code === 200
			with open(Image + '-' + str(x) + '.jpg', 'wb') as f: # open the image as the mentioned file format, (w for writing, and b for binary)
				# as the format is jpg, it needs to be saved as a binary file
				# here "f" is just a variable assignment
				f.write(requests.get(url).content) # get the content of the url and write/save in the created dir
				f.close() # stop writing/saving the image
				x += 1 # increment x by 1
	except: # on excpetion (i.e, status code !== 200, or other errors)
		pass # repeat the loop again
