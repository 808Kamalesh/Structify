import os
import sys
from typing import Dict, Union, List, Tuple
from rich.console import Console
from rich.syntax import Syntax
from rich.panel import Panel

console = Console()

def parse_structure_file(file_path: str) -> List[Tuple[int, str]]:
    structure = []
    try:
        with open(file_path, 'r') as f:
            content = f.read()

        console.print("\n[bold cyan]Structure File Content:[/]")
        syntax = Syntax(content, "txt", theme="monokai")
        console.print(Panel(syntax))

        if not content.strip():
            raise ValueError("Structure file is empty")

        for line in content.splitlines():
            stripped_line = line.rstrip()
            if stripped_line:
                indent_level = len(stripped_line) - len(stripped_line.lstrip())
                name = stripped_line.lstrip()
                if not name:
                    continue
                structure.append((indent_level, name))

        if not structure:
            raise ValueError("No valid structure found in file")

    except Exception as e:
        console.print(f"[error]Error reading structure file: {str(e)}[/]")
        sys.exit(1)

    return structure

def convert_to_dict(structure: List[Tuple[int, str]]) -> Dict:
    if not structure:
        return {}

    result = {}
    stack = [(0, result)]

    try:
        for indent, name in structure:
            name = name.strip()
            if not name:
                continue

            while stack and indent <= stack[-1][0]:
                stack.pop()

            if not stack:
                stack = [(0, result)]

            current_dict = stack[-1][1]

            if name.endswith('/') or '.' not in name:
                name = name.rstrip('/')
                current_dict[name] = {}
                stack.append((indent, current_dict[name]))
            else:
                current_dict[name] = None

    except Exception as e:
        console.print(f"[error]Error processing structure: Invalid indentation or format[/]")
        sys.exit(1)

    return result