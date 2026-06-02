import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Search for files by extension")
parser.add_argument("--path", required=True, help="Directory path to search")
parser.add_argument("--ext", required=True, help="The file extension you want to search, e.g. .txt, .py, .tmp")

args = parser.parse_args()
pattern = f"*{args.ext}"

for file in Path(args.path).rglob(pattern):
	print(f"Found file: {file}")