# -*- coding: UTF-8 -*
import wave
import numpy as np
from pyaudio import PyAudio,paInt16
import speech_recognition as sr
from subprocess import call

'''
Assignment: record voice and open default page of web browser
Methods: Ugly one, using wave and PyAudio to record audio
		and 3rd party speech_recognition to recognize, and 
		subprocess.call to deal with the words using 'firefox'
'''

def save_wave_file(file_name,data):
	wf = wave.open(file_name,'wb')
	wf.setnchannels(1)
	wf.setsampwidth(2)
	wf.setframerate(SAMPLING_RATE)
	wf.writeframes(''.join(data))
	wf.close()

f_name = 'data.wav'
NUM_SAMPLES = 2000		#
SAMPLING_RATE = 8000	#
LEVEL = 1500			#
COUNT_NUM = 20 			#
SAVE_LENGTH = 4 		#

pa = PyAudio()
stream = pa.open(format=paInt16,channels=1,rate=SAMPLING_RATE,input=True,
				 frames_per_buffer = NUM_SAMPLES)
save_count = 0
save_buffer = []

while True:
	string_audio_data = stream.read(NUM_SAMPLES)
	audio_data = np.fromstring(string_audio_data, dtype = np.short)
	large_sample_count = np.sum( audio_data > LEVEL)
	print np.max(audio_data),large_sample_count
	if large_sample_count > COUNT_NUM:
		save_count = SAVE_LENGTH
	else:
		save_count -= 1

	if save_count < 0:
		save_count = 0

	if save_count > 0 :
		save_buffer.append( string_audio_data )
	else:
		if len(save_buffer) > 0:
			save_wave_file(f_name,save_buffer)
			save_buffer = []
			print f_name,'saved'
			break

r = sr.Recognizer()
with sr.AudioFile(f_name) as source:
	audio = r.record(source)

try:
	text = r.recognize_google(audio)
	print "Google thinks you're saying ",text
	call(['firefox',text.lower()+'.com'])
except sr.UnknownValueError:
	print "Google does'nt know what you're talking"