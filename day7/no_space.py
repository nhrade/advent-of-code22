from ast import List
import pathlib
import re
from dataclasses import dataclass
from typing import Any, Union


@dataclass
class File:
    name: str
    size: int
    parent: Any

    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def __repr__(self):
        return f"{self.name} (file, size={self.size})"

    def __str__(self):
        return f"{self.name} (file, size={self.size})"


@dataclass
class Dir:
    children: dict
    parent: Any
    name: str

    def __init__(self, name):
        self.name = name
        self.children = {}

    def add(self, file):
        file.parent = self
        self.children[file.name] = file

    def get(self, name):
        return self.children.get(name, None)

    def __repr__(self):
        return f"{self.name} (dir)"

    def __str__(self):
        return f"{self.name} (dir)"

    def print_filesystem(self, indent=0):
        indent_str = indent * " "
        print(f"{indent_str}- {str(self)}")
        for child in self.children:
            if isinstance(child, Dir):
                child.print_filesystem(indent + 1)
            else:
                indent_str += "\t"
                print(f"{indent_str}- {str(child)}")


class Filesystem:
    def __init__(self):
        self.root = Dir("/")
        self.pointer = self.root

    def goto_root(self):
        self.pointer = self.root

    def goto_parent(self):
        self.pointer = self.pointer.parent

    def cd(self, name):
        self.pointer = self.pointer.get(name)

    def ls(self):
        for child in self.pointer.children:
            print(child)

    # create a new file
    def touch(self, name, size):
        file = File(name, size)
        self.pointer.add(file)

    # create a new dir
    def mkdir(self, name):
        d = Dir(name)
        self.pointer.add(d)

    def print_filesystem(self):
        self.root.print_filesystem()


cd_regex = r"\$ cd (\w+|..|\/)"
ls_regex = r"\$ ls"
dir_regex = r"dir (\w+)"
file_regex = r"(\d+) (\w+(?:\.\w+)?)"


def parse_line(filesystem, line, ln):
    if match := re.match(cd_regex, line):
        name = match[1]
        if name == "/":
            filesystem.goto_root()
        elif name == "..":
            filesystem.goto_parent()
        else:
            filesystem.cd(name)
    elif _ := re.match(ls_regex, line):
        filesystem.ls()
    elif match := re.match(dir_regex, line):
        filesystem.mkdir(match[1])
    elif match := re.match(file_regex, line):
        filesystem.touch(match[2], match[1])
    else:
        raise ValueError(f"No match for line {ln}.")


def parse_lines(filesystem, lines):
    for ln, line in enumerate(lines):
        parse_line(filesystem, line, ln + 1)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()
        filesystem = Filesystem()
        parse_lines(filesystem, lines)
        filesystem.print_filesystem()
