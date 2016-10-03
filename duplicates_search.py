import sys
import os
import hashlib
import collections


def md5sum(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()


hash_to_files = collections.defaultdict(list)


top_dir = sys.argv[1]
for root, _, files in os.walk(top_dir):
    for filename in files:
        if not filename.startswith('.') and not filename.startswith('~'):
            file_path = os.path.join(root, filename)
            if not (os.path.islink(file_path)):
                hsh = md5sum(file_path)
                hash_to_files[hsh].append(os.path.relpath(file_path, top_dir))

for duplicates in hash_to_files.values():
    if len(duplicates) > 1:
        print(':'.join(duplicates))
