from app.ai.provider import AIProvider


class Translator:
    """
    Converts natural language into Linux commands using the AI provider.
    """

    def __init__(self):
        self.provider = AIProvider()

    def translate(self, query: str, context):
        """
        Translate an English query into a Linux command.

        Args:
            query: User's natural language request.
            context: Current system context collected by ContextService.

        Returns:
            LinuxCommand
        """

        return self.provider.translate(
            query=query,
            context=context,
        )