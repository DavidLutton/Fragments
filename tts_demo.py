from tts import Mimic
import os
import logging

logging.basicConfig(level=logging.DEBUG)


tts = Mimic()
tts.binary(os.path.join('/mnt', 'ssd', 'Media', 'ReposEXT', 'mimic', 'bin', 'mimic'))
tts.voice(os.path.join('/mnt', 'ssd', 'Media', 'ReposEXT', 'mimic', 'voices', 'mycroft_voice_4.0.flitevox'))

tts.say("Greetings")

x = """Hello
World
Hello World
"""
for n in x.splitlines(True):
    tts.say(n)
