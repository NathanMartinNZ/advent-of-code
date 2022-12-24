import re

with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.replace("\n", "") for line in lines]

##############
### Part 1 ###
##############
fs_data = {
    'root': {
        'size': 0,
        'total_size': 0,
        'files': []
    }
}

current_dir = ["root"]

for line in lines[1:]:
    if line == "$ ls" or re.findall("dir ", line):
        continue
    elif line == "$ cd ..":
        current_dir.pop()
    elif re.findall("\$ cd", line):
        current_dir.append(line.replace("$ cd ", ""))
        if '/'.join(current_dir) not in fs_data:
            fs_data['/'.join(current_dir)
                    ] = {'size': 0, 'total_size': 0, 'files': []}
    else:
        [size, file] = line.split(" ")
        fs_data['/'.join(current_dir)]['files'].append({
            "file": file,
            "size": int(size)
        })


for dir in fs_data:
    # Add size of files in current dir
    size = sum(f['size'] for f in fs_data[dir]['files'])
    fs_data[dir]['size'] = size

    # Add total sizes of dir and all children dirs
    dir_and_children_dirs = dict(((key, fs_data[key])
                                  for key in fs_data if key.startswith(dir)))

    for c_dir in dir_and_children_dirs:
        sum_size = sum(f['size'] for f in fs_data[c_dir]['files'])
        fs_data[dir]['total_size'] = fs_data[dir]['total_size'] + int(sum_size)


part_1_answer = sum(fs_data[key]['total_size']
                    for key in fs_data if fs_data[key]['total_size'] <= 100000)
print(part_1_answer)


##############
### Part 2 ###
##############
max_space = 70000000
unused_space_req = 30000000
current_space_used = fs_data['root']['total_size']
space_to_remove = unused_space_req - (max_space - current_space_used)

dirs_with_enough_space = [fs_data[key]['total_size']
                          for key in fs_data if fs_data[key]['total_size'] >= space_to_remove]

dirs_with_enough_space.sort()

part_2_answer = dirs_with_enough_space[0]

print(part_2_answer)
