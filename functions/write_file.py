import os
from google.genai import types

def write_file(working_directory, file_path, content):
    wd_abs = os.path.abspath(working_directory)
    joined = os.path.join(wd_abs, file_path)
    file_abs = os.path.abspath(joined)
    if not file_abs.startswith(wd_abs):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file_abs):
        try:
            os.makedirs(os.path.dirname(file_abs), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    if os.path.exists(file_abs) and os.path.isdir(file_abs):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        with open(file_abs, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: writing to file: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite contents of a file in the specified directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to write or overwrite file from, relative to the working directory.",
            ),
        },
    ),
)