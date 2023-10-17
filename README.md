# Gofile Python Wrapper

This Python wrapper provides a convenient interface for interacting with the Gofile.io API (back-end), allowing you to upload files, and read file content.

## Installation

```bash
git clone https://github.com/lutherantz/gofile
```

## Usage

```python
from gofile import Gofile

# Initialize Gofile
gof = Gofile()

# Upload a file to Gofile.io
file_code = gof.uploadFile("path_to_your_file.ext")

# Read the content of a file
file_content = gof.readFile(file_code)
# Or
print(gof.readFile(file_code))
```

Make sure to replace ```"path_to_your_file.ext"``` with the actual file path you want to upload.

# Licence

This project is licensed under the MIT License. Feel free to use and modify the code as needed. For more information, see the LICENSE file.

# Author

By @sekateur
