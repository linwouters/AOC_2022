# AOC 2022-12-07
# Lin Wouters

def count_directory_sizes(file, i, dirs_sizes=[], max_size=100000):

    size = 0
    # While there are still lines to read in the file
    while i < len(file):
        # Go out of the directory and save the size of the current directory
        if file[i].startswith('$ cd ..'):
            dirs_sizes.append(size)
            return size, i, dirs_sizes
        # Go into a directory and count its size
        elif file[i].startswith('$ cd '):
            dir_size, i, dirs_sizes = count_directory_sizes(file, i+1, dirs_sizes, max_size)
            size = size + dir_size
        # Add file size to this current directory
        elif not file[i].startswith('$ ') and not file[i].startswith('dir'):
            size += int(file[i].split(' ')[0])
        i += 1
    # Append the size of the root folder
    dirs_sizes.append(size)

    return size, i, dirs_sizes


def folder_sizes(filepath, max_size=100000, total_disk=70000000, needed_disk=30000000):

    with open(filepath) as f:
        file = f.read().strip().split('\n')
        # Count the sizes of the directories
        size, i, dirs_sizes = count_directory_sizes(file, i=0, dirs_sizes=[], max_size=max_size)

    # Calculate the sum 
    total_size = sum([size for size in dirs_sizes if size <= max_size])

    # Smallest directory to remove
    to_remove = needed_disk - (total_disk - dirs_sizes[-1])
    remove_size = min([size for size in dirs_sizes if size >= to_remove])

    return total_size, remove_size


if __name__ == "__main__":
    filepath="../data/day7.txt"
    # filepath="../data/test_day7.txt"
    total_size, remove_size = folder_sizes(filepath, max_size=100000)
    print(f"The total size of the folders with max 100000 size is: {total_size}")
    print(f"The size of the smallest folder that can be removed to clear enough space is: {remove_size}")