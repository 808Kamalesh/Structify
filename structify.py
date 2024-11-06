import os
import argparse
import sys
from structer import ProjectStructureGenerator
from structure_parser import parse_structure_file, convert_to_dict
from utils import display_banner
from time import sleep
from rich.console import Console
from rich.prompt import Confirm

console = Console()

def main():

    parser = argparse.ArgumentParser(description="Generate project structure from a text file")
    parser.add_argument('structure_file', type=str, help='Text file containing project structure')
    parser.add_argument('--output', '-o', type=str, default=os.getcwd(),
                       help='Output directory for the project structure (default: current directory)')
    args = parser.parse_args()

    try:
        if not os.path.exists(args.structure_file):
            raise FileNotFoundError(f"Structure file '{args.structure_file}' not found")

        with open(args.structure_file, 'r') as f:
            root_dir = f.readline().strip()

        output_dir = os.path.abspath(args.output)
        if not root_dir:
            raise ValueError("Structure file must start with a root directory name")

        if os.path.basename(output_dir) != root_dir:
            output_dir = os.path.join(output_dir, root_dir)

        if os.path.exists(output_dir):
            if not Confirm.ask(f"\n[warning]Directory '{output_dir}' already exists. Do you want to continue?[/]"):
                console.print("[info]Operation cancelled by user.[/]")
                return

        os.makedirs(output_dir, exist_ok=True)

        console.print(f"\n[info]Output directory:[/] {output_dir}")

        with console.status("[bold cyan]Parsing structure file...[/]") as status:
            structure_list = parse_structure_file(args.structure_file)
            sleep(1)  

        with console.status("[bold cyan]Processing structure...[/]") as status:
            structure_dict = convert_to_dict(structure_list)
            sleep(1)  

        generator = ProjectStructureGenerator()
        generator.base_path = output_dir
        generator.create_structure(structure_dict, output_dir)

        console.print("\n[success]✨ Project structure created successfully![/]")

        console.print("\n[bold cyan]Created Project Structure:[/]")
        generator.display_tree(output_dir)

        stats_table = generator.get_stats_table()
        console.print("\n")
        console.print(stats_table)

    except Exception as e:
        console.print(f"\n[error]Error: {str(e)}[/]")
        sys.exit(1)

if __name__ == "__main__":
    main()
