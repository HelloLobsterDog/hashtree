from pathlib import Path

from hashtree import hash_file


def test_md5():
    testing_directory = Path(__file__).parent.parent/'testing'

    assert hash_file(testing_directory / 'happy_path' / '上篇') == 'f11ea1768ecd409899c9402804f7a192'
    assert hash_file(testing_directory / 'happy_path' / 'same contents different name') == hash_file(testing_directory / 'happy_path' / '上篇')
    assert hash_file(testing_directory / 'happy_path' / 'empty.txt') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert hash_file(testing_directory / 'happy_path' / 'big.jpg') == '062b949aaf95f87ee123183ddca6deb8'
    assert hash_file(testing_directory / 'happy_path' / 'humor' / 'bee movie.txt') == '5c18b58b2e7194a7f78bb55671d43e10'
    assert hash_file(testing_directory / 'happy_path' / 'chain' / 'binary' / 'katie.jpg') == 'ff1af431750190e13f6b63b1a1a4b17f'
    assert hash_file(testing_directory / 'happy_path' / 'chain' / 'binary' / 'Opal.jpg') == '2eda526319e7facd6b941aeec80e5749'
    assert hash_file(testing_directory / 'happy_path' / 'chain' / 'text' / 'lorem_ipsum.txt') == 'db89bb5ceab87f9c0fcc2ab36c189c2c'
    assert hash_file(testing_directory / 'happy_path' / 'chain' / 'text' / 'this one has newlines') == '1701734cd6b90895d166ce1dda4f4489'
