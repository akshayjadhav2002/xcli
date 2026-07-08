from rich.prompt import Confirm


def ask_confirmation():

    return Confirm.ask(
        "Execute this command?",
        default=False
    )