import Image,ImageDraw,ImageFont

class Image_CornerNum():
	def open_img(self,name):
		self.im = Image.open(name)
		self.font_size = min(self.im.size)/5

	def open_font(self,filename,fontsize=20):
		self.font = ImageFont.truetype(filename,self.font_size)

	def write_text(self,text):
		d = ImageDraw.Draw(self.im) 
		t_size = d.textsize(text,self.font)
		im_size = self.im.size
		d.text((im_size[0] * 8/9-t_size[0],0),text,font=self.font,fill=(255,0,0,200))
		self.im.save('with_num.jpg','JPEG')

pic = Image_CornerNum()
pic.open_img('photo.jpg')
pic.open_font('font.ttf',25)
pic.write_text("5")