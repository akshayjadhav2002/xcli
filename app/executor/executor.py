import subprocess
import shlex

from app.executor.result import ExecutionResult


class CommandExecutor:

    def execute(self, command: str):

        result = subprocess.run(

            shlex.split(command),

            capture_output=True,

            text=True,

            shell=False

        )

        return ExecutionResult(

            success=result.returncode == 0,

            stdout=result.stdout,

            stderr=result.stderr,

            returncode=result.returncode

        )