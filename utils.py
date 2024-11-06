from rich.console import Console

console = Console()

def display_banner():
    banner = """
[bold orange3]
░█▀▀░▀█▀░█▀▄░█░█░█▀▀░▀█▀░▀█▀░█▀▀░█░█
░▀▀█░░█░░█▀▄░█░█░█░░░░█░░░█░░█▀▀░░█░
░▀▀▀░░▀░░▀░▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░░░░▀░
[/]
    """
    console.print(banner)

display_banner()
