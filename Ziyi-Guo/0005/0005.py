import Image
import os
"""
Aim: deal with all the pics in a floder
	 make them eqaul or less than iphone5's size
Method: using Image module
"""

class Pic_Resizer():
	"""docstring for Pic_Resizer"""
	def __init__(self, folder_name='.'):
		format = ['jpg','png','jpeg']
		file_list = [x for x in os.listdir(folder_name) if x.split('.')[-1] in format]
		if file_list==[]: # no pic file in the dir
			print "No pic file at all!"
			return
		self.file_list = file_list
		self.size_restrict = [640,1136]
	
	def get_pic_file(self):
		for f_name in self.file_list:
			im = Image.open(f_name)
			[width,height] = im.size
			w_ratio = width/float(self.size_restrict[0]);h_ratio = height/float(self.size_restrict[1]);
			if w_ratio>1 or h_ratio>1:
				im = self.pic_resize(im,[width,height],[w_ratio,h_ratio])
				im.save('tmp_'+f_name,'JPEG')
			

	def pic_resize(self,im,size,ratio):
		x = max(ratio)
		im = im.resize([int(size[0]/x),int(size[1]/x)])
		return im



pr = Pic_Resizer()
pr.get_pic_file()