import sys
import traceback

from app.ai.translator import Translator
from app.context.service import ContextService
from app.executor.executor import CommandExecutor
from app.security.validator import SecurityValidator
from app.ui.confirm import ask_confirmation
from app.ui.printer import Printer

translator = Translator()
context_service = ContextService()
validator = SecurityValidator()
executor = CommandExecutor()
printer = Printer()


def main():
    """
    Linux AI Assistant

    Examples:
        x list files
        x current process
        x show disk usage
        x who am i
    """

    if len(sys.argv) < 2:
        printer.show_help()
        return

    query = " ".join(sys.argv[1:])

    try:
        printer.separator()

        # -----------------------------
        # Collect Context
        # -----------------------------
        context = context_service.collect()

        # -----------------------------
        # AI Translation
        # -----------------------------
        printer.thinking()

        result = translator.translate(
            query=query,
            context=context,
        )

        # -----------------------------
        # Validation
        # -----------------------------
        printer.validating()

        validation = validator.validate(result.command)

        printer.review(query, result)

        if not validation.allowed:
            printer.blocked(validation.reason)
            return

        # -----------------------------
        # Confirmation
        # -----------------------------
        if validation.requires_confirmation:

            if not ask_confirmation():
                printer.cancelled()
                return

        # -----------------------------
        # Execute
        # -----------------------------
        printer.executing()

        execution = executor.execute(result.command)

        if execution.success:
            printer.output(execution.stdout)
            printer.success()
        else:
            printer.error(execution.stderr)

    except KeyboardInterrupt:
        printer.cancelled()

    except Exception:
        traceback.print_exc()
        printer.error("Unexpected error occurred.")