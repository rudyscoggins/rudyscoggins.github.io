import os
import shutil
import argparse

parser = argparse.ArgumentParser(description='Transfer songs to staging folder.')
parser.add_argument('source', help='Path to directory containing songs')
parser.add_argument('staging', help='Path to staging directory')
args = parser.parse_args()

source_dir = args.source
staging_dir = args.staging

if not os.path.isdir(source_dir):
    raise SystemExit(f'Source directory {source_dir} does not exist.')
if not os.path.isdir(staging_dir):
    os.makedirs(staging_dir, exist_ok=True)

for filename in os.listdir(source_dir):
    src = os.path.join(source_dir, filename)
    dst = os.path.join(staging_dir, filename)
    if os.path.isfile(src):
        shutil.copy2(src, dst)

print('Songs transferred successfully to staging.')
