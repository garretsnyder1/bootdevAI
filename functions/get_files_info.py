import os

def get_files_info(working_directory, directory="."):
    joined = os.path.join(working_directory, directory)
    abspath = os.path.abspath(joined)
    print(joined)
    print(abspath)
    if not abspath.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abspath):
        return f'Error: "{directory}" is not a directory'
    contents = os.listdir(abspath)
    files = []
    for file in contents:
        path_to = abspath + f"/{file}"
        files.append(f"- {file}: file_size={os.path.getsize(path_to)} bytes, is_dir={os.path.isdir(path_to)}")
    string = "\n".join(files)
    return string