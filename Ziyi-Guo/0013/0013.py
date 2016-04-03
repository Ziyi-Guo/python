import urllib2,re
from urlparse import urlsplit
from os.path import basename
"""
Assignment: download pics from bbs
Method: using urllib to read content, re to find img urls,
		and urlsplit + basename to get name 
"""
class Image_Downloader():
	def __init__(self,url):
		url = url+'?see_lz=1'
		content = urllib2.urlopen(url).read()
		page_ct = re.findall('<span class="red">(.*?)</span>',content)
		self.url = url+'?see_lz=1'+'?pn='
		self.page_vol = int(page_ct[0])

	def download_img(self):
		for i in range(self.page_vol):
			content = urllib2.urlopen(self.url+str(i)).read()
			ss = re.findall('<cc>(.*?)</cc>',content)
			ss = ','.join(ss)
			img_urls = re.findall('img .*? src="(.*?)"',ss)
			for im_url in img_urls:
				im = urllib2.urlopen(im_url).read()
				f_name = basename(urlsplit(im_url)[2])
				f = open(f_name,'w')
				f.write(im)
				f.close()
				print 'Done download %s' %f_name


imd = Image_Downloader('http://tieba.baidu.com/p/4403109806')
imd.download_img()