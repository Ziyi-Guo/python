import string,random,Image,ImageDraw,ImageFont,ImageFilter
'''
Assignment: generate image with random letters on it, with filter
Method: generate strings with string and random, write into pic and filter with Image.
'''

class LetterImageGenerator():
	# Class for generate image with random string on it
	def __init__(self,s_len=4):
		self.str_len = s_len

	def rand_str(self):
		''' generate random strings with the length '''
		s = []
		s.extend(string.letters);s.extend(string.digits);
		len_s = len(s)
		tmp_indx = random.sample(range(0,len_s),self.str_len)
		self.str = ''.join(s[j] for j in tmp_indx)


	def write_pic_file(self):
		''' generate raw img first, then get font, and write text, save file '''
		self.im = Image.new("RGB",(300,100),"white")
		self.font_size = 300 / (self.str_len) # get font size
		self.font = ImageFont.truetype("font.ttf",self.font_size)
		self.write_text()
		self.im.save('%s.jpg' %self.str,'JPEG')

	def write_text(self):
		''' get drawer, for every letter, random color, write letters, blur it '''
		d = ImageDraw.Draw(self.im) 
		im_size = self.im.size
		for i in range(self.str_len):
			txt_cl = random.sample(range(0,255),4)
			d.text((10 + i*300/self.str_len,10),self.str[i],font=self.font,fill=(txt_cl[0],txt_cl[1],txt_cl[2],txt_cl[3]))
		self.im = self.im.filter(ImageFilter.BLUR)



lig = LetterImageGenerator(6)
lig.rand_str()
lig.write_pic_file()