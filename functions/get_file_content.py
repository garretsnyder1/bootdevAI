import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    wd_abs = os.path.abspath(working_directory)
    joined = os.path.join(wd_abs, file_path)
    file_abs = os.path.abspath(joined)
    if not file_abs.startswith(wd_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:

        with open(file_abs, "r") as f:
            truncation_msg = None
            if os.path.getsize(file_abs) > MAX_CHARS:
                truncation_msg = f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return f.read(MAX_CHARS) + truncation_msg
    except Exception as e:
        return f"Error listing files {e}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read contents of a file in the specified directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to read file from, relative to the working directory.",
            ),
        },
    ),
)