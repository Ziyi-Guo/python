import os,hashlib,hmac
'''
Assignment: generate /unbreakable/ password 
Methods: salt and hash 
'''
class PasswordManager():
	"""docstring for PasswordManager"""
	def __init__(self):
		pass

	def encrypt_password(self,raw_password,salt=None):
		if salt is None:
			salt = os.urandom(8)

		assert len(salt) == 8
		assert isinstance(salt,str)

		if isinstance(raw_password,unicode):
			raw_password = raw_password.encode('utf-8')

		assert isinstance(raw_password,str)

		result = raw_password
		for i in range(10):
			result = hmac.HMAC(result,salt,hashlib.sha256).digest()
		return salt+result

	def validata_password(self,first,pwd):
		return first == self.encrypt_password(pwd,first[:8])

pm = PasswordManager()
f_pwd = pm.encrypt_password(raw_input('your_pwd>'))
print pm.validata_password(f_pwd,raw_input('again>'))