# CountMyCode

This Python script recursively scans directories and counts the lines of code (LOC) in files of various programming languages. It categorizes the files by their extensions and tallies the LOC for each language.

## Features

- **Directory Navigation**: Allows the user to navigate through directories.
- **File Filtering**: Filters files by programming language extensions.
- **Recursive Scanning**: Recursively scans subdirectories for files.
- **LOC Counting**: Counts the number of lines in each file, categorized by programming language.
- **Interactive Interface**: Provides an interactive terminal interface for directory selection.

## How it Works

1. **Directory Selection**: The script starts by listing all directories and files in the current working directory. The user can select the directory to navigate into.
   
2. **File Scanning**: Once the directory is selected, the script scans all files inside the directory and its subdirectories. It looks for files with known programming language extensions.

3. **Line Counting**: For each file, the script opens it, reads the lines, and counts how many lines of code belong to each programming language based on the file extension.

4. **Results**: The script outputs a list of programming languages with the corresponding lines of code in the terminal.

## Supported Languages

The script currently supports the following programming languages based on their file extensions:

- Python (.py)
- HTML (.html)
- CSS (.css)
- JavaScript (.js)
- TypeScript (.ts)
- Java (.java)
- C (.c)
- C++ (.cpp)
- C# (.cs)
- Swift (.swift)
- Kotlin (.kt)
- Ruby (.rb)
- PHP (.php)
- Go (.go)
- Rust (.rs)
- Dart (.dart)
- Shell Script (.sh)
- SQL (.sql)
- R (.R)
- Lua (.lua)
- Assembly (.asm)
- And many more...

## Usage

1. Clone this repository or download the script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:

```bash
python3 count_lines.py