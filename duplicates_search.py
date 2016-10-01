import sys
import os
import hashlib


def md5sum(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()


dict_of_diff_files = dict()


def collect_duplicates(file_path):
    if md5sum(file_path) not in dict_of_diff_files.keys():
        dict_of_diff_files[md5sum(file_path)] = [os.path.relpath(
                                                 file_path, top_dir)]
    else:
        dict_of_diff_files[md5sum(file_path)].append(
                          os.path.relpath(file_path, top_dir))
    return dict_of_diff_files


top_dir = sys.argv[1]
for root, _, files in os.walk(top_dir):
    for filename in files:
        if not filename.startswith('.') and not filename.startswith('~'):
            collect_duplicates(os.path.join(root, filename))

for list_of_duplicates in dict_of_diff_files.values():
        print(':'.join(map(str, list_of_duplicates)))
