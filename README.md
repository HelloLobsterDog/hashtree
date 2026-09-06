# hashtree
A CLI utility to calculate hashes for everything in a directory tree and provide a single composite hash of everything, including subdirectories and their contents.

It works on all major OSes where Python is installed.

```
$ hashtree testing/happy_path
happy_path
┣━big.jpg: 062b949aaf95f87ee123183ddca6deb8
┣━empty.txt: d41d8cd98f00b204e9800998ecf8427e
┣━same contents different name: f11ea1768ecd409899c9402804f7a192
┣━上篇: f11ea1768ecd409899c9402804f7a192
┣━chain
┃ ┣━binary
┃ ┃ ┣━katie.jpg: ff1af431750190e13f6b63b1a1a4b17f
┃ ┃ ┗━Opal.jpg: 2eda526319e7facd6b941aeec80e5749
┃ ┗━text
┃   ┣━lorem_ipsum.txt: db89bb5ceab87f9c0fcc2ab36c189c2c
┃   ┗━this one has newlines: 1701734cd6b90895d166ce1dda4f4489
┣━empty
┗━humor
  ┗━bee movie.txt: 5c18b58b2e7194a7f78bb55671d43e10

Final hash: c2b54c4674e73d81b84ba643cb607e8d
```

### Use cases
- determine whether two directories are the same without needing to buy or install tools like beyondcompare
- automated backup deduplication
- determine whether two directories on different machines are the same without needing to send them over the network to compare them
- track changes to a file tree through time without needing to store every modification made to every file

# Installation
- **Install from source**: `git clone https://github.com/HelloLobsterDog/hashtree.git && cd hashtree && pip install .`
- **Run from source** (hashtree.py is the entire program): `git clone https://github.com/HelloLobsterDog/hashtree.git && python hashtree/hashtree.py .`

Installation through pip is planned when the project is in a more complete state.

# Usage
```
usage: hashtree [-h] [-q] [-v] path

Calculate hashes for everything in a directory tree and provide a single
composite hash of everything, including subdirectories and their contents.

positional arguments:
  path           Path to calculate hashes for

options:
  -h, --help     show this help message and exit
  -q, --quiet    Output will be limited only to the final hash
  -v, --version  show program's version number and exit
```

## Credits
- The file Opal.jpg used in the testing data was acquired from [Wikipedia](https://commons.wikimedia.org/wiki/File:Opal_Welo_-_Welo,_Afar_Province,_Etiopia,_Afryka..jpg), was attributed to Lech Darski, and is licensed under the [Creative Commons Attribution-Share Alike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/deed.en) license.
- The files big.jpg and cat.jpg used in the testing data were taken by Daniel Westbrook, and are provided under the [Creative Commons Attribution-Share Alike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/deed.en) license. 
