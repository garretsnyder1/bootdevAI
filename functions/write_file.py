import os

def write_file(working_directory, file_path, content):
    wd_abs = os.path.abspath(working_directory)
    joined = os.path.join(wd_abs, file_path)
    file_abs = os.path.abspath(joined)
    if not file_abs.startswith(wd_abs):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        os.makedirs(os.path.dirname(file_abs), exist_ok=True)
        with open(file_abs, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"