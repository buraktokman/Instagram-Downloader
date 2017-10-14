#!/usr/bin/env python
# Instagram Avatar Downloader

import urllib.request
import sys,os
#from sys import argv
from bs4 import BeautifulSoup
from urllib.request import urlopen
from os.path import expanduser

desktop = expanduser("~") + '/Desktop'
image_url = None
username = None
directory = None

if len(sys.argv) < 2:
	username = 'instagram'
	print('default account: instagram')
elif len(sys.argv) < 3:
	username = sys.argv[1]
	print('default directory: desktop')
elif len(sys.argv) < 4:
	username = sys.argv[1]
	directory = sys.argv[2]

def download_file(url):
	filename = url[url.rfind("/")+1:]
	if directory != None:
		if check_file_exists(directory + '/' + filename) == False:
			urllib.request.urlretrieve(url, directory + '/' + filename)
	else:
		if check_file_exists(desktop + '/' + filename) == False:
			urllib.request.urlretrieve(url, desktop + '/' + filename)
	return

def check_file_exists(url):
	return os.path.exists(url)

def url_parser(url):
	set1 = {'s1080x1080/', 's640x640/', 's480x480/', 's320x320/', 's150x150/', 'p1080x1080/', 'p640x640/', 'p480x480/', 'p320x320/', 'sh0.08/', 'e35/', 'e15/'}
	# t51.2885-15/
	# t51.2885-19/
	for x in set1:
		if x in url:
			url = url.replace(x, '')
	return url

def avatar(url):
	global image_url
	print(url)
	page = urlopen(url)
	soup = BeautifulSoup(page, 'lxml')
	image = soup.find('meta', property='og:image')
	image_url = image['content']
	image_url = url_parser(image_url)
	print(image_url)
	download_file(image_url)
	return

def main():
	global username
	print(username)
	avatar('https://www.instagram.com/' + username)

if __name__ == "__main__":
	main()
