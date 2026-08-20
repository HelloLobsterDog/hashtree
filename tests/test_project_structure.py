"""
Tests in this file look for accidents in project structure, and are intended purely to prevent me from making mistakes.
"""
import tomllib
from pathlib import Path

import hashtree


def test_I_did_not_break_the_newline_file_accidentally():
    with open(Path(__file__).parent.parent / 'testing' / 'happy_path' / 'chain' / 'text' / 'this one has newlines', 'rb') as f:
        contents = f.read()
        assert contents.count(b'\n') == 5
        assert contents.count(b'\r') == 3 # not the same!


def test_version_matches():
    with open(Path(__file__).parent.parent / "pyproject.toml", "rb") as f:
        data = tomllib.load(f)
        assert data['project']['version'] == hashtree.__version__


def test_python_version_matches():
    with open(Path(__file__).parent.parent / "pyproject.toml", "rb") as toml_file:
        data = tomllib.load(toml_file)
        toml_version = data['project']['requires-python'].replace(">", '').replace('=', '')
    with open(Path(__file__).parent.parent / ".python-version", "r") as python_version:
        assert toml_version == python_version.read().replace("\n", '')


def test_usage_in_readme_matches_real():
    with open(Path(__file__).parent.parent / "README.MD", "r", encoding="utf-8") as readme:
        contents = readme.read().replace("\r\n", "\n")
        just_usage = contents[contents.find("# Usage\n```")+11:contents.find("```", contents.find("# Usage\n```")+11)].strip()
        assert just_usage+'\n' == hashtree.setup_argparse().format_help()
