# coding=utf-8
import unittest
from kana_to_romaji.kana_to_romaji import kana_to_romaji


class TestHiraganaRomajiTranslation(unittest.TestCase):
    def setUp(self):
        print "\nStarting " + self.__module__ + ": " + self._testMethodName

    def test_brackets(self):
        d = {
            "！": "!",
            "＂": "\"",
            "＃": "#",
            "＄": "$",
            "％": "%",
            "＆": "&",
            "＇": "'",
            "（": "(",
            "）": ")",
            "＊": "*",
            "＋": "+",
            "，": ",",
            "－": "-",
            "．": ".",
            "／": "/",
            "０": "0",
            "１": "1",
            "２": "2",
            "３": "3",
            "４": "4",
            "５": "5",
            "６": "6",
            "７": "7",
            "８": "8",
            "９": "9",
            "：": ":",
            "；": ";",
            "＜": "<",
            "＝": "=",
            "＞": ">",
            "？": "?",
            "＠": "@",
            "Ａ": "A",
            "Ｂ": "B",
            "Ｃ": "C",
            "Ｄ": "D",
            "Ｅ": "E",
            "Ｆ": "F",
            "Ｇ": "G",
            "Ｈ": "H",
            "Ｉ": "I",
            "Ｊ": "J",
            "Ｋ": "K",
            "Ｌ": "L",
            "Ｍ": "M",
            "Ｎ": "N",
            "Ｏ": "O",
            "Ｐ": "P",
            "Ｑ": "Q",
            "Ｒ": "R",
            "Ｓ": "S",
            "Ｔ": "T",
            "Ｕ": "U",
            "Ｖ": "V",
            "Ｗ": "W",
            "Ｘ": "X",
            "Ｙ": "Y",
            "Ｚ": "Z",
            "［": "[",
            "＼": "\\",
            "］": "]",
            "＾": "^",
            "＿": "_",
            "｀": "'",
            "ａ": "a",
            "ｂ": "b",
            "ｃ": "c",
            "ｄ": "d",
            "ｅ": "e",
            "ｆ": "f",
            "ｇ": "g",
            "ｈ": "h",
            "ｉ": "i",
            "ｊ": "j",
            "ｋ": "k",
            "ｌ": "l",
            "ｍ": "m",
            "ｎ": "n",
            "ｏ": "o",
            "ｐ": "p",
            "ｑ": "q",
            "ｒ": "r",
            "ｓ": "s",
            "ｔ": "t",
            "ｕ": "u",
            "ｖ": "v",
            "ｗ": "w",
            "ｘ": "x",
            "ｙ": "y",
            "ｚ": "z",
            "｛": "{",
            "｜": "|",
            "｝": "}",
            "～": "~"
        }
        for k in d.keys():
            self.assertEqual(kana_to_romaji(k), d[k])
            self.assertTrue(ord(kana_to_romaji(k)) < 127)


if __name__ == "__main__":
    unittest.main()
