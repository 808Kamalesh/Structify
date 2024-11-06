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

# Ensure it's only called once in your script
display_banner()
