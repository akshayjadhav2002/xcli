from rich.prompt import Confirm


def ask_confirmation() -> bool:
    """
    Ask the user whether they want to execute the command.
    """
    return Confirm.ask(
        "[yellow]Execute this command?[/yellow]",
        default=False,
    )