from io import StringIO
from pathlib import Path

from hashtree import hash_tree


def test_real_folder():
    tree_stream = StringIO()
    result = hash_tree(Path(__file__).parent.parent / 'testing' / 'happy_path', tree_stream)

    assert tree_stream.getvalue() == '''happy_path
┣big.jpg: 062b949aaf95f87ee123183ddca6deb8
┣empty.txt: d41d8cd98f00b204e9800998ecf8427e
┣same contents different name: f11ea1768ecd409899c9402804f7a192
┣上篇: f11ea1768ecd409899c9402804f7a192
┣chain
┃┣binary
┃┃┣katie.jpg: ff1af431750190e13f6b63b1a1a4b17f
┃┃┗Opal.jpg: 2eda526319e7facd6b941aeec80e5749
┃┗text
┃ ┣lorem_ipsum.txt: db89bb5ceab87f9c0fcc2ab36c189c2c
┃ ┗this one has newlines: 1701734cd6b90895d166ce1dda4f4489
┣empty
┗humor
 ┗bee movie.txt: 5c18b58b2e7194a7f78bb55671d43e10
'''
    assert result == '0'
