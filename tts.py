import subprocess
import shlex
import logging


class Mimic():
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.info('Creating an instance of ' + __name__)

    def voice(self, voice):
        self.voice = '-voice ' + voice + ' '
        self.log.info('Setting voice to  :' + voice)

    def binary(self, binary):
        self.binary = binary + ' '
        self.log.info('Setting binary to :' + self.binary)

    def say(self, sentence):
        self.log.debug(sentence.strip())
        sentence = shlex.quote(sentence)
        cmd = self.binary + self.voice + '-t ' + sentence
        subprocess.run(cmd, shell=True, check=True)
        # TODO not ideal, should be cleaner/safer
