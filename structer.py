import os
import sys
from typing import Dict, Union, Tuple
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.tree import Tree
from rich.table import Table
from time import sleep

console = Console()

class ProjectStructureGenerator:
    def __init__(self):
        self.created_paths = []
        self.tree = None

    def create_structure(self, structure: Dict[str, Union[Dict, None]], base_path: str = ".") -> None:
        try:
            total_items = self._count_items(structure)
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
                console=console
            ) as progress:
                task = progress.add_task("[yellow]Creating project structure...", total=total_items)
                self._create_with_progress(structure, base_path, progress, task)

                progress.update(task, completed=total_items)

        except Exception as e:
            console.print(f"\n[error]Error creating structure: {str(e)}[/]")
            self.cleanup()
            sys.exit(1)

    def _count_items(self, structure: Dict) -> int:
        count = 0
        for name, content in structure.items():
            count += 1  
            if isinstance(content, dict):
                count += self._count_items(content)  
        return count

    def _create_with_progress(self, structure: Dict, base_path: str, progress, task) -> None:
        for name, content in structure.items():
            path = os.path.join(base_path, name)

            if content is None:  
                with open(path, 'w') as f:
                    pass
                self.created_paths.append(("file", path))
            else:  
                os.makedirs(path, exist_ok=True)
                self.created_paths.append(("dir", path))
                self._create_with_progress(content, path, progress, task)  

            progress.update(task, advance=1)
            sleep(0.05)  

    def cleanup(self) -> None:
        console.print("\n[warning]⚠️ Error occurred. Cleaning up...[/]")
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("[yellow]Cleaning up...", total=len(self.created_paths))

            for path_type, path in reversed(self.created_paths):
                try:
                    if path_type == "file" and os.path.isfile(path):
                        os.remove(path)
                    elif path_type == "dir" and os.path.isdir(path):
                        os.rmdir(path)
                    progress.update(task, advance=1)
                except Exception as e:
                    console.print(f"[warning]Error during cleanup of {path}: {str(e)}[/]")

    def display_tree(self, base_path: str) -> None:
        self.tree = Tree(
            f"[bold cyan]{os.path.basename(base_path)}[/]",
            guide_style="cyan"
        )
        self._build_tree(base_path, self.tree)
        console.print(self.tree)

    def _build_tree(self, directory: str, tree: Tree) -> None:
        try:
            for item in sorted(os.listdir(directory)):
                path = os.path.join(directory, item)
                if os.path.isfile(path):
                    tree.add(f"[green]{item}[/]")
                else:
                    branch = tree.add(f"[bold yellow]{item}[/]")
                    self._build_tree(path, branch)
        except Exception as e:
            console.print(f"[error]Error building tree: {str(e)}[/]")

    def get_stats_table(self) -> Table:
        files = sum(1 for t, _ in self.created_paths if t == "file")
        dirs = sum(1 for t, _ in self.created_paths if t == "dir")

        stats_table = Table(title="Project Statistics")
        stats_table.add_column("Type", style="cyan")
        stats_table.add_column("Count", style="green")

        stats_table.add_row("Files", str(files))
        stats_table.add_row("Directories", str(dirs))
        stats_table.add_row("Total Items", str(files + dirs))

        return stats_table