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
    for current_directory, dirs, files in path.walk(top_down=True):
        dirs.sort()
        files.sort()

        for file_name in files:
            file = Path(current_directory/file_name)
            if file.is_symlink():
                raise NotImplementedError("symlink handling is not implemented")
            else:
                print(file_name + ": " + hash_file(file))
    return ''


def hash_file(path: Path) -> str:
    with open(path, 'rb') as f:
        return hashlib.file_digest(f, "md5").hexdigest()
