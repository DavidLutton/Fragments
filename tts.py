import subprocess
import shlex


class Mimic():
    def voice(self, voice):
        self.voice = '-voice ' + voice + ' '

    def binary(self, binary):
        self.binary = binary + ' '

    def say(self, sentence):
        cmd = self.binary + self.voice + '-t ' + shlex.quote(sentence)
        # print(cmd)
        subprocess.run(cmd, shell=True, check=True)
        # TODO not ideal, should be cleaner/safer
