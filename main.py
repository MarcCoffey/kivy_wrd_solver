from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import itertools
from kivy.factory import Factory

class WordFinder(BoxLayout):
    def __init__(self, **kwargs):
        super(WordFinder, self).__init__(**kwargs)
        # Get list of words from shelve files
        with open('wordFile.txt', 'r') as wrdFile:
            self.words_raw = wrdFile.read()
            self.word_list = self.words_raw.split('\n\n')
        del wrdFile, self.words_raw
        self.length = self.ids.chkb6.value

    def word_maker(self, chars_in, word_len, word_lst):
        char_combos = list(itertools.permutations(chars_in, word_len))
        char_combos = [''.join(j) for j in char_combos]
        trash, self.ans = [], []
        trash = [self.ans.append(i) if i in word_lst else i for i in char_combos]
        if chars_in.isalpha() and len(chars_in) == 6:
            self.ids.rv.data = [{'text': str(x)} for x in set(self.ans)]
        else:
            Factory.WarningPopUp().open()
        return set(self.ans)

    def getChars(self):
        self.chars = self.ids.txtinpt.text

        print(f'chars are: {self.chars}')
        return self.chars

    def getLength(self, intVal):
        self.length = intVal
        print('length is: {}'.format(self.length))
        return self.length


class BuildApp(App):
    def build(self):
        return WordFinder()


if __name__ == '__main__':
    BuildApp().run()
