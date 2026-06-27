import argparse
import hashlib
import sys
from dataclasses import dataclass
from pathlib import Path
from queue import Queue

from typing import Tuple, TextIO


__version__ = '0.0.2'


def setup_argparse() -> argparse.ArgumentParser:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(prog="hashtree", description='calculate hashes for everything in a directory tree')

    parser.add_argument("paths", nargs='+', help="paths to calculate hashes for")

    return parser


def run() -> None:
    args: argparse.Namespace = setup_argparse().parse_args()
    for path in args.paths:
        hash_tree(Path(path), sys.stdout)


@dataclass
class InProgressDirectory:
    path: Path
    in_progress: Path | None
    todo_list: Queue[Path]
    completed: list[Tuple[Path, str]]

    def get_hash(self, hash_name='md5') -> str:
        hasher = hashlib.new(hash_name)
        for hash_component in sorted(self.completed, key=lambda x: x[0].name):
            hasher.update(hash_component[0].name.encode('utf-8'))
            hasher.update(b"|")
            hasher.update(hash_component[1].encode('utf-8'))
            hasher.update(b'//')
        return hasher.hexdigest()


def make_wip(directory: Path) -> InProgressDirectory:
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
    todo_list = Queue()
    for item in files:
        todo_list.put(item)
    for subdir in subdirectories:
        todo_list.put(subdir)

    return InProgressDirectory(directory, None, todo_list, [])


def assemble_prefix(stack: list[InProgressDirectory]) -> str:
    prefix = ''
    for x in stack:
        if x.todo_list.empty():
            prefix += ' '
        else:
            prefix += '┃'
    last = stack[-1]
    if last.todo_list.empty():
        prefix = prefix[:-1] + '┗'
    else:
        prefix = prefix[:-1] + '┣'
    return prefix


def hash_tree(path: Path, stream: TextIO) -> str:
    root: InProgressDirectory = make_wip(path)
    stack: list[InProgressDirectory] = [root]
    stream.write(str(root.path.name))
    stream.write("\n")

    while stack:
        current = stack[-1]
        if not current.todo_list.empty():
            todo = current.todo_list.get_nowait()
            current.todo_list.task_done()

            if todo.is_file():
                stream.write(assemble_prefix(stack))
                stream.write(str(todo.name))
                file_hash = hash_file(todo)
                stream.write(": ")
                stream.write(file_hash)
                stream.write("\n")
                current.completed.append((todo, file_hash))

            elif todo.is_dir():
                stream.write(assemble_prefix(stack))
                stream.write(str(todo.name))
                stream.write("\n")
                current.in_progress = todo
                wip = make_wip(todo)
                stack.append(wip)

        else:
            # we're done with this directory, pop off the stack
            stack.pop()
            if stack:
                parent = stack[-1]
                parent.completed.append((current.path, current.get_hash()))
                parent.in_progress = None

    return root.get_hash()


def hash_file(path: Path) -> str:
    with open(path, 'rb') as f:
        return hashlib.file_digest(f, "md5").hexdigest()
