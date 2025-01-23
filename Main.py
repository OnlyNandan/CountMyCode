import subprocess
import os

home_dir = os.path.expanduser("~")
os.chdir(home_dir)
working_dir = home_dir
directories = []
files = []
No_of_lines = {
    "PYTHON": 0,
    "HTML": 0,
    "CSS": 0,
    "JAVASCRIPT": 0,
    "TYPESCRIPT": 0,
    "JAVASCRIPT XML": 0,
    "JAVA": 0,
    "C++": 0,
    "C": 0,
    "C#": 0,
    "SWIFT": 0,
    "KOTLIN": 0,
    "RUBY": 0,
    "PHP": 0,
    "GO": 0,
    "RUST": 0,
    "DART": 0,
    "SHELL SCRIPT": 0,
    "SQL": 0,
    "R": 0,
    "LUA": 0,
    "ASSEMBLY": 0,
    "SCALA": 0,
    "PERL": 0,
    "JSON": 0,
    "MATLAB / OBJECTIVE-C": 0,
    "BATCH FILE (WINDOWS)": 0,
    "YAML": 0,
    "XML": 0,
    "LATEX": 0,
    "VISUAL BASIC": 0,
    "VBSCRIPT": 0,
    "CLOJURE": 0,
    "CLOJURE EDN": 0,
    "COFFEESCRIPT": 0,
    "ERLANG": 0,
    "ELIXIR": 0,
    "ELIXIR SCRIPT": 0,
    "FORTRAN 90": 0,
    "FORTRAN": 0,
    "GROOVY": 0,
    "C HEADER FILES": 0,
    "C++ HEADER FILES": 0,
    "JUPYTER NOTEBOOK": 0,
    "JULIA": 0,
    "COMMON LISP": 0,
    "OPENCL": 0,
    "OCAML": 0,
    "F#": 0,
    "SAS": 0,
    "ADA": 0,
    "ADA SPECIFICATION": 0,
    "POWERSHELL": 0,
    "TCL": 0,
    "AWK": 0,
    "GAMEMAKER LANGUAGE": 0,
    "Q (KDB+)": 0,
    "SMALI (ANDROID)": 0,
    "CRYSTAL": 0,
    "HAXE": 0,
    "VERILOG": 0,
    "SYSTEMVERILOG": 0,
    "SASS (SCSS SYNTAX)": 0,
    "SASS": 0,
    "LESS (CSS PREPROCESSOR)": 0,
    "MARKDOWN": 0,
    "R MARKDOWN": 0,
    "RACKET": 0,
    "HASKELL": 0,
    "TERRAFORM": 0,
    "NIX": 0,
    "AUTOHOTKEY": 0,
    "ARDUINO SKETCH": 0,
    "BASIC": 0,
    "T-SQL (TRANSACT-SQL)": 0,
    "VUE.JS": 0,
    "PASCAL": 0,
    "ASSEMBLY (GENERIC)": 0,
    "ECMASCRIPT MODULES": 0,
    "REN'PY": 0,
    "XML TEMPLATE": 0,
    "YACC": 0,
    "LLVM INTERMEDIATE REPRESENTATION": 0,
    "ZIG": 0,
    "EIFFEL": 0,
    "D": 0,
    "PROCESSING": 0,
    "TYPESCRIPT JSX (REACT)": 0,
}
languages = [
    ".py",    # Python
    ".html",  # HTML
    ".css",   # CSS
    ".js",    # JavaScript
    ".ts",    # TypeScript
    ".jsx",   # JavaScript XML (React)
    ".java",  # Java
    ".cpp",   # C++
    ".c",     # C
    ".cs",    # C#
    ".swift", # Swift
    ".kt",    # Kotlin
    ".rb",    # Ruby
    ".php",   # PHP
    ".go",    # Go (Golang)
    ".rs",    # Rust
    ".dart",  # Dart
    ".sh",    # Shell Script
    ".sql",   # SQL
    ".R",     # R
    ".lua",   # Lua
    ".asm",   # Assembly
    ".scala", # Scala
    ".pl",    # Perl
    ".json",  # JSON
    ".m",     # MATLAB / Objective-C
    ".bat",   # Batch File (Windows)
    ".yaml",  # YAML
    ".xml",   # XML
    ".tex",   # LaTeX
    ".vb",    # Visual Basic
    ".vbs",   # VBScript
    ".clj",   # Clojure
    ".edn",   # Clojure EDN
    ".coffee",# CoffeeScript
    ".erl",   # Erlang
    ".ex",    # Elixir
    ".exs",   # Elixir Script
    ".f90",   # Fortran 90
    ".f",     # Fortran
    ".groovy",# Groovy
    ".h",     # C Header Files
    ".hpp",   # C++ Header Files
    ".ipynb", # Jupyter Notebook
    ".jl",    # Julia
    ".lisp",  # Common Lisp
    ".cl",    # OpenCL
    ".ml",    # OCaml
    ".fs",    # F#
    ".sas",   # SAS
    ".adb",   # Ada
    ".ads",   # Ada Specification
    ".ps1",   # PowerShell
    ".tcl",   # Tcl
    ".awk",   # AWK
    ".gml",   # GameMaker Language
    ".q",     # Q (KDB+)
    ".smali", # Smali (Android)
    ".cr",    # Crystal
    ".hx",    # Haxe
    ".v",     # Verilog
    ".sv",    # SystemVerilog
    ".scss",  # Sass (SCSS Syntax)
    ".sass",  # Sass
    ".less",  # Less (CSS Preprocessor)
    ".md",    # Markdown
    ".rmd",   # R Markdown
    ".rkt",   # Racket
    ".hs",    # Haskell
    ".tf",    # Terraform
    ".nix",   # Nix
    ".ahk",   # AutoHotkey
    ".ino",   # Arduino Sketch
    ".bas",   # BASIC
    ".tsql",  # T-SQL (Transact-SQL)
    ".vue",   # Vue.js
    ".pas",   # Pascal
    ".s",     # Assembly (generic)
    ".mjs",   # ECMAScript Modules
    ".rpy",   # Ren'Py
    ".xtml",  # XML Template
    ".y",     # Yacc
    ".ll",    # LLVM Intermediate Representation
    ".zig",   # Zig
    ".e",     # Eiffel
    ".d",     # D
    ".pde",   # Processing
    ".tsx",   # TypeScript JSX (React)
]

extensions_mapping = {
    ".py": "PYTHON",
    ".html": "HTML",
    ".css": "CSS",
    ".js": "JAVASCRIPT",
    ".ts": "TYPESCRIPT",
    ".jsx": "JAVASCRIPT XML",
    ".java": "JAVA",
    ".cpp": "C++",
    ".c": "C",
    ".cs": "C#",
    ".swift": "SWIFT",
    ".kt": "KOTLIN",
    ".rb": "RUBY",
    ".php": "PHP",
    ".go": "GO",
    ".rs": "RUST",
    ".dart": "DART",
    ".sh": "SHELL SCRIPT",
    ".sql": "SQL",
    ".r": "R",
    ".lua": "LUA",
    ".asm": "ASSEMBLY",
    ".scala": "SCALA",
    ".pl": "PERL",
    ".json": "JSON",
    ".m": "MATLAB / OBJECTIVE-C",
    ".bat": "BATCH FILE (WINDOWS)",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".xml": "XML",
    ".tex": "LATEX",
    ".vbs": "VBSCRIPT",
    ".fs": "F#",
    ".jl": "JULIA",
    ".ps1": "POWERSHELL",
    ".pas": "PASCAL",
    ".scss": "SASS (SCSS SYNTAX)",
    ".less": "LESS (CSS PREPROCESSOR)",
    ".md": "MARKDOWN",
    ".rmd": "R MARKDOWN",
    ".rkt": "RACKET",
    ".hs": "HASKELL",
    ".tf": "TERRAFORM",
    ".nix": "NIX",
    ".ahk": "AUTOHOTKEY",
    ".ino": "ARDUINO SKETCH",
    ".bas": "BASIC",
    ".sql": "T-SQL (TRANSACT-SQL)",
    ".vue": "VUE.JS",
    ".h": "C HEADER FILES",
    ".hpp": "C++ HEADER FILES",
    ".ipynb": "JUPYTER NOTEBOOK",
    ".erl": "ERLANG",
    ".ex": "ELIXIR",
    ".fsx": "F#",
    ".asmx": "ASSEMBLY (GENERIC)",
    ".zig": "ZIG",
    ".d": "D",
    ".pde": "PROCESSING",
    ".tsx": "TYPESCRIPT JSX (REACT)",
}

def scan_folder():
    global working_dir
    os.chdir(working_dir)
    result = os.listdir(working_dir)
    return result

def lister(direct):
    global directories
    

    ctr = 4
    directories.append("1. Select This Directory")
    directories.append("2. Home")
    directories.append("3. Back")

    for i in direct:
        if i!="":
            if i.find(".") == -1:
                i=str(ctr)+"."+" "+i
                directories.append(i)
                ctr+=1


def printer():
    global directories
    print("\n"*100)
    print("="*100) 
    print(f"{working_dir:^100}")
    print("="*100)
    for i in range(0,len(directories)-1,2):
        try:
            print(f"{directories[i].ljust(50, ' ')}{directories[i+1].ljust(50, ' ')}".center(100, ' '))        
        except IndexError:
            print(f"{directories[i]:^50}")
    print("="*100) 
        

def change_dir():
    global working_dir
    n=int(input("Enter the number of the directory you want to change to: "))
    print("\n"*20)
    global directories
    if n > 3:
        newdir = directories[n-1]
        if n<10:
            newdir = newdir[3:]
            os.chdir(newdir)

        elif n>9:
            newdir = newdir[4:]
            os.chdir(newdir)


    if n==2:
        os.chdir(home_dir)
    if n==3:
        os.chdir("..")
    if n==1:
        scan(working_dir)
        print("Selected Directory",working_dir)
        return 1
    if n!=1:
        print("Changing Directory...")
        print("\n")
        print("present working directory: ",os.getcwd())
        working_dir = os.getcwd()
        print("\n")
    elif n==1:
        print("Selected Directory",working_dir)

def scan(directory):
    global files
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item) 
            for i in languages:

                if os.path.isfile(item_path) and item_path.endswith(i):
                    files.append(item_path) 
            if os.path.isdir(item_path): 
                scan(item_path)
    except Exception as e:
        print(f"Error accessing {directory}: {e}")

def countfiles():
    global files, No_of_lines
    for i in files:
        try:
            with open(i, "r") as file:
                data = file.readlines()
                for ext, lang in extensions_mapping.items():
                    if i.endswith(ext):
                        No_of_lines[lang] += len(data)
                        break  
        except Exception as e:
            print(f"Error accessing {i}: {e}")
            

def output():
    global No_of_lines
    print("="*50) 
    print(f"{'Programming Language':^30} {'Lines of Code':^20}")  
    print("="*50) 
    for lang, lines in No_of_lines.items():
        if lines > 0:
            print(f"{lang:^30} {lines:^20}")  
    print("="*50) 

def main():
    global directories
    tempval = 0
    bool= True
    while bool:
        direct=scan_folder()
        lister(direct)
        printer()
        tempval=change_dir()
        countfiles()
        if tempval == 1:
            bool = False
            break
        if tempval != 1:
            directories = []
    output()
main()