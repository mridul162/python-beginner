# README.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a Python beginner learning repository containing standalone educational scripts that demonstrate fundamental Python concepts. Each file is an independent tutorial example meant to be run individually.

## Running Code

### Execute Individual Scripts
```powershell
python <script_name>.py
```

Examples:
```powershell
python 08_if_statement.py
python 16_class_objects.py
python lambda_function.py
```

### Using Virtual Environment
A `.venv` directory exists in the project. To activate it:
```powershell
.\.venv\Scripts\Activate.ps1
```

## Code Architecture

### Project Structure
- **Root-level scripts**: Numbered tutorial files (08-16) follow a learning progression
- **Unnumbered files**: Supplementary examples for specific topics (sets, files, lambda functions, while loops)
- **modules/**: Directory for custom modules (currently empty except for __pycache__)

### Key Patterns

**Module Import Examples**
- `12_modules.py`: Demonstrates custom path imports using `sys.path.append()`
- `14_caller.py` + `14__name__.py`: Shows module import patterns and `__name__ == "__main__"` usage

**File I/O Patterns**
- Scripts use absolute Windows paths (e.g., `C:\\data\\fun.txt`)
- File operations demonstrated with both manual `open()/close()` and `with` statements

**Interactive Scripts**
Many scripts use `input()` for user interaction:
- `08_if_statement.py`: Number/dish input validation
- `09_for_loop.py`: Collecting fruit list
- `15_exception_handling.py`: Division with error handling

### Concepts Covered by File
- **08_if_statement.py**: Conditionals, membership testing with lists
- **09_for_loop.py**: Iteration, range(), list operations, break/continue
- **10_functions.py**: Function definitions, parameters, default arguments, docstrings, scope
- **12_modules.py**: Module imports and custom paths
- **13_working_with_json.py**: JSON serialization with dictionaries
- **14__name__.py / 14_caller.py**: Module execution context
- **15_exception_handling.py**: Try/except blocks, specific exception types
- **16_class_objects.py**: Class definitions, `__init__`, methods
- **files.py**: File operations, read/write modes, `with` statements
- **lambda_function.py**: Lambda expressions, higher-order functions
- **sets.py**: Set operations (union, intersection, symmetric difference)
- **while.py**: While loops

## Development Notes

### Environment
- Project uses PyCharm IDE (`.idea` directory present)
- Windows environment with PowerShell
- Python virtual environment configured in `.venv/`

### Code Characteristics
- Most tutorial code sections are commented out (using `#`)
- Scripts often contain multiple examples for the same concept
- Many hardcoded file paths point to `C:\\data\\` directory
- Mix of teaching styles: some files have active code, others have commented examples to uncomment

### Working with This Codebase
When modifying or adding examples:
1. Follow the numbered naming convention for sequential tutorials (e.g., `17_next_topic.py`)
2. Include comments explaining concepts for beginners
3. Use standalone, runnable examples that don't require external dependencies
4. For file I/O examples, be aware of hardcoded paths to `C:\\data\\`
