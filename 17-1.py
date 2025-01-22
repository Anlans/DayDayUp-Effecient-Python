import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __getitem__(self, index):
        return self.words[index]
    
    def __len__(self):
        return len(self.words)
    
    def __repr__(self):
        return f"Sentence({reprlib.repr(self.text)})"


s = Sentence('"The time has come," the Walrus said,')
print(iter(s))
# print(f"s: {s}")
# for word in s:
#     print(word)
