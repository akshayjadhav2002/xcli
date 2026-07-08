from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()


class Printer:

    def show_help(self):
        """Display help information."""

        help_text = """
[bold cyan]Linux AI Assistant[/bold cyan]

Examples:

• x list files
• x show current directory
• x current process
• x disk usage
• x create folder demo
• x remove folder demo

Write your request in plain English.
"""

        console.print(
            Panel.fit(
                help_text,
                title="Welcome",
                border_style="cyan",
            )
        )

    def review(self, query, command):
        """
        Display the AI-generated command before execution.
        """

        table = Table(show_header=False, box=None)

        table.add_row("🗣 Request", query)
        table.add_row("💻 Linux Command", f"[bold green]{command.command}[/bold green]")
        table.add_row("📖 Meaning", command.description)

        risk = command.risk.value.upper()

        if risk == "SAFE":
            risk_text = "[green]SAFE[/green]"
        elif risk == "MEDIUM":
            risk_text = "[yellow]MEDIUM[/yellow]"
        else:
            risk_text = "[red]HIGH[/red]"

        table.add_row("🛡 Risk", risk_text)

        console.print()
        console.print(
            Panel(
                table,
                title="[bold cyan]Linux AI Assistant[/bold cyan]",
                border_style="cyan",
            )
        )

    def thinking(self):
        console.print("[cyan]🤖 Understanding request...[/cyan]")

    def translating(self):
        console.print("[cyan]🧠 Translating to Linux command...[/cyan]")

    def validating(self):
        console.print("[cyan]🛡 Running security checks...[/cyan]")

    def executing(self):
        console.print("\n[yellow]⚡ Executing command...[/yellow]\n")

    def output(self, text):
        if text.strip():
            console.print(
                Panel(
                    text.strip(),
                    title="[green]Output[/green]",
                    border_style="green",
                )
            )

    def success(self):
        console.print("\n[bold green]✓ Command executed successfully[/bold green]\n")

    def blocked(self, reason):
        console.print(
            Panel(
                reason,
                title="[bold red]BLOCKED[/bold red]",
                border_style="red",
            )
        )

    def cancelled(self):
        console.print(
            "\n[yellow]Operation cancelled by user.[/yellow]\n"
        )

    def error(self, error):
        console.print(
            Panel(
                str(error),
                title="[bold red]Error[/bold red]",
                border_style="red",
            )
        )

    def separator(self):
        console.rule("[bold blue]Linux AI Assistant[/bold blue]")