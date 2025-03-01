import os
import shutil
import tempfile

# 1. Write a Python program to list only directories, files and all directories, files in a specified path.
def list_directories_files(path):
    dirs = []
    files = []
    all_dirs = []
    all_files = []
    
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            dirs.append(item)
            all_dirs.append(item)
        elif os.path.isfile(os.path.join(path, item)):
            files.append(item)
            all_files.append(item)
    
    return dirs, files, all_dirs, all_files

# 2. Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
def check_access(path):
    
    # r - read, w - write, x - execute
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK) 
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    
    return exists, readable, writable, executable

# 3. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
def path_info(path):
    exists = os.path.exists(path)
    if exists:
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return filename, directory
    return

# 4. Write a Python program to count the number of lines in a text file.
def count_lines_in_file(path):
    with open(path, 'r') as file:
        return len(file.readlines())
    
# 5. Write a Python program to write a list to a file.
def write_list_to_file(path, lst):
    with open(path, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")

# 6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
def generate_files():
    a_ascii_letter = 65
    z_ascii_letter = 91
    for c in range(a_ascii_letter, z_ascii_letter):
        with open(f"{chr(c)}.txt", 'w') as file:
            # print('File created:', f"{chr(c)}.txt")
            pass
    
# 7. Write a Python program to copy the contents of a file to another file
def copy_file(src, dest):
    with open(src, 'r') as src_file:
        with open(dest, 'w') as dest_file:
            dest_file.write(src_file.read())

# 8. Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
def delete_file(path):
    exists = os.path.exists(path)
    if exists:
        os.remove(path)
        return True
    return False

def test_file_operations():
    # going full TDD mode :D
    # didn't knew assert is available without any libraries... python rocks!
     
    # vremennaya papka dlya testov operaciy nad files
    test_dir = tempfile.mkdtemp()
    test_subdir = os.path.join(test_dir, "subdir")
    os.makedirs(test_subdir)
    
    # test files
    test_file = os.path.join(test_dir, "test.txt")
    with open(test_file, "w") as f:
        f.write("Line 1\nLine 2\nLine 3")    
    
    try:
        # Test 1: List directories and files
        dirs, files, all_dirs, all_files = list_directories_files(test_dir)
        assert "subdir" in dirs
        assert "test.txt" in files
        
        # Test 2: Check access
        exists, readable, writable, executable = check_access(test_file)
        assert exists and readable and writable
        
        # Test 3: Path info
        filename, directory = path_info(test_file)
        assert filename == "test.txt"
        assert directory == test_dir
        
        # Test 4: Count lines
        assert count_lines_in_file(test_file) == 3
        
        # Test 5: zapisat list v file
        items = ["element 1", "element 2", "element 3", "etc"]
        write_list_to_file(test_file, items)
        with open(test_file, "r") as f:
            assert f.read().strip() == "element 1\nelement 2\nelement 3\netc"
        
        # Test 6: sgenerit files (in subdir)
        os.chdir(test_subdir)
        generate_files()
        assert os.path.exists(os.path.join(test_subdir, "A.txt"))
        os.chdir(test_dir)
        
        # Test 7: Copy file
        copy_dest = os.path.join(test_dir, "copy.txt")  
        copy_file(test_file, copy_dest)  
        assert os.path.exists(copy_dest)  # Checkaem esli copied file exists

        # Test 8: Delete file
        assert delete_file(copy_dest)  
        assert not os.path.exists(copy_dest) # Checkaem esli file deleted
        
        print("All tests passed. horosh")
    finally:
        # v konce udalit' vse
        shutil.rmtree(test_dir)

if __name__ == "__main__":
    with open("paste.py", "w") as f:
        with open("paste.txt", "r") as source:
            f.write(source.read())
    
    test_file_operations()