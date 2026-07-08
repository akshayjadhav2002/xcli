from google import genai
from google.genai import types

from app.config import Config
from app.models.command import LinuxCommand


class AIProvider:
    """
    Handles all communication with Gemini.
    """

    def __init__(self):

        self.client = genai.Client(
            api_key=Config.GEMINI_API_KEY
        )

    def _build_prompt(self, query: str, context) -> str:

        files = ", ".join(context.files[:30]) if context.files else "No files"

        processes = (
            ", ".join(context.running_processes[:10])
            if context.running_processes
            else "None"
        )

        interfaces = (
            ", ".join(context.network_interfaces)
            if context.network_interfaces
            else "None"
        )

        return f"""
    You are xcli, an AI-powered Linux terminal assistant.

    Your job is to convert the user's English request into exactly ONE safe Linux command.

    =========================
    CURRENT SYSTEM CONTEXT
    =========================

    User:
    {context.user}

    Operating System:
    {context.os}

    Hostname:
    {context.hostname}

    Shell:
    {context.shell}

    Current Directory:
    {context.cwd}

    Home Directory:
    {context.home}

    Files in Current Directory:
    {files}

    Git Repository:
    {context.git_repo}

    Git Branch:
    {context.git_branch}

    Python Version:
    {context.python_version}

    Virtual Environment:
    {context.virtualenv}

    CPU Usage:
    {context.cpu_usage:.1f}%

    Memory Usage:
    {context.memory_usage:.1f}%

    Disk Usage:
    {context.disk_usage:.1f}%

    Running Processes:
    {processes}

    Network Interfaces:
    {interfaces}

    =========================
    USER REQUEST
    =========================

    {query}

    =========================
    RULES
    =========================

    1. Return ONLY valid JSON.

    2. Never explain your reasoning.

    3. Never return Markdown.

    4. Never return multiple commands.

    5. Never use:

    &&
    ||
    ;
    |
    >
    >>

    6. Never generate dangerous commands.

    7. Assume Ubuntu Linux.

    8. Use the current system context whenever it helps generate a better command.

    9. If the requested file exists in the current directory, use it.

    10. If the command cannot be generated safely, return the safest possible alternative.

    """

    def translate(
        self,
        query: str,
        context,
    ) -> LinuxCommand:

        prompt = self._build_prompt(
            query=query,
            context=context,
        )

        response = self.client.models.generate_content(

            model=Config.MODEL,

            contents=prompt,

            config=types.GenerateContentConfig(

                response_mime_type="application/json",

                response_schema=LinuxCommand,

                temperature=0,

            ),
        )

        return response.parsed