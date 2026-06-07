import argparse
import hashlib
from pathlib import Path

__version__ = '0.0.1'


def setup_argparse() -> argparse.ArgumentParser:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(prog="hashtree", description='calculate hashes for everything in a directory tree')

    parser.add_argument("paths", nargs='+', help="paths to calculate hashes for")

    return parser


def run() -> None:
    args: argparse.Namespace = setup_argparse().parse_args()
    for path in args.paths:
        hash_tree(Path(path))


def hash_tree(path: Path) -> str:
    stack: list[Path] = []
    todo_list: list[Path] = [path]
    while todo_list:
        directory: Path = todo_list.pop()
        print("┃"*(len(stack)-1) + "┣" + str(directory.stem))
        while stack and directory.parent != stack[-1]:
            stack.pop()
        stack.append(directory)

        subdirectories: list[Path] = []
        files: list[Path] = []
        for item in directory.iterdir():
            if item.is_symlink():
                raise NotImplementedError("symlinks not implemented")
            elif item.is_dir():
                subdirectories.append(item)
            elif item.is_file():
                files.append(item)
            else:
                raise NotImplementedError("Huh???")

        subdirectories.sort()
        files.sort()

        for f in files:
            print("┃"*(len(stack)-1) + "┣" + str(f.stem) + ": " + hash_file(f))
        for subdirectory in subdirectories:
            todo_list.append(subdirectory)


def hash_file(path: Path) -> str:
    with open(path, 'rb') as f:
        return hashlib.file_digest(f, "md5").hexdigest()
