import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    wd_abs = os.path.abspath(working_directory)
    joined = os.path.join(wd_abs, directory)
    dir_abs = os.path.abspath(joined)
    if not dir_abs.startswith(wd_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(dir_abs):
        return f'Error: "{directory}" is not a directory'
    try:
        contents = os.listdir(dir_abs)
        files = []
        for file in contents:
            path_to = dir_abs + f"/{file}"
            files.append(f"- {file}: file_size={os.path.getsize(path_to)} bytes, is_dir={os.path.isdir(path_to)}")
        string = "\n".join(files)
        return string
    except Exception as e:
        return f"Error listing files {e}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)