import os
import sys
import glob

from tinytag import TinyTag
from hurry.filesize import size


def second_to_time(seconds):
    seconds = int(seconds)
    minutes = int(seconds/60)
    r_seconds = seconds % 60
    return '{}:{}'.format(str(minutes), str(r_seconds))


def bytes_to_mb(bytes):
    return size(bytes)


arguments = sys.argv[1:]

if not arguments:
    print('Please provide directory path')
    exit()

"""
Scan provided directory paths and check if path exists and create list of absolute paths
"""
paths = []
for arg in arguments:
    if arg[0] == '/':
        path = arg
    else:
        path = os.path.join(os.getcwd(), arg)

    if not os.path.isdir(path):
        print(arg + ' is not a valid directory')
        exit()

    paths.append(path)

"""
Loop over paths to get list of all files
"""
media_files = []
for path in paths:
    glob_files = glob.glob(path+'/*.mp3')
    media_files = media_files + glob_files

"""
Loop over media files to get tags
"""
total_duration = 0
total_files = 0
total_size = 0
files_data = []
for media in media_files:
    tag = TinyTag.get(media)
    # Prepare media dictionary
    media_dictionary = {
        'file': media.split('/')[-1],
        'duration': tag.duration,
        'filesize': tag.filesize
    }
    files_data.append(media_dictionary)
    total_duration = total_duration + tag.duration
    total_size = total_size + tag.filesize
    total_files = total_files + 1

"""
Print data in tabular form
"""
# Find longest column
longest_col = 10
for data in files_data:
    if len(data['file']) > longest_col:
        longest_col = len(data['file'])

raw_str = '{:<'+str(longest_col)+'} {:<15} {:<10}'

print(raw_str.format('File', 'Filesize', 'Duration (mm:ss)'))
for data in files_data:
    print(raw_str.format(data['file'], bytes_to_mb(data['filesize']), second_to_time(data['duration'])))

print('-'*(longest_col+15+10))

print(raw_str.format('Total: ' + str(total_files), bytes_to_mb(total_size), second_to_time(total_duration)))

print()
print()
