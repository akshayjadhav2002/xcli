import shlex

from app.models.command import RiskLevel
from app.security.rule_engine import RuleEngine
from app.security.scanner import DANGEROUS_PATTERNS
from app.security.validation_result import ValidationResult


class SecurityValidator:
    """
    Validates Linux commands before execution.

    This class is the final security layer before a command
    is executed.
    """

    def __init__(self):
        self.engine = RuleEngine()

    def validate(self, command: str) -> ValidationResult:
        """
        Validate a Linux command.

        Returns:
            ValidationResult
        """

        command = command.strip()

        # ----------------------------------------
        # Empty command
        # ----------------------------------------

        if not command:
            return ValidationResult(
                allowed=False,
                risk=RiskLevel.HIGH,
                requires_confirmation=False,
                reason="Empty command.",
            )

        # ----------------------------------------
        # Block shell injection operators
        # ----------------------------------------

        for pattern in DANGEROUS_PATTERNS:

            if pattern in command:

                return ValidationResult(
                    allowed=False,
                    risk=RiskLevel.HIGH,
                    requires_confirmation=False,
                    reason=f"Shell operator '{pattern}' is not allowed.",
                )

        # ----------------------------------------
        # Tokenize command safely
        # ----------------------------------------

        try:
            tokens = shlex.split(command)

        except ValueError:

            return ValidationResult(
                allowed=False,
                risk=RiskLevel.HIGH,
                requires_confirmation=False,
                reason="Unable to parse command.",
            )

        if not tokens:

            return ValidationResult(
                allowed=False,
                risk=RiskLevel.HIGH,
                requires_confirmation=False,
                reason="No executable found.",
            )

        executable = tokens[0]

        # ----------------------------------------
        # Completely blocked commands
        # ----------------------------------------

        if executable in self.engine.blocked_commands():

            return ValidationResult(
                allowed=False,
                risk=RiskLevel.HIGH,
                requires_confirmation=False,
                reason=f"'{executable}' is blocked.",
            )

        # ----------------------------------------
        # Get command policy
        # ----------------------------------------

        rule = self.engine.get_rule(executable)

        if rule is None:

            return ValidationResult(
                allowed=False,
                risk=RiskLevel.HIGH,
                requires_confirmation=False,
                reason=f"'{executable}' is not supported yet.",
            )

        # ----------------------------------------
        # Validate arguments
        # ----------------------------------------

        blocked_arguments = rule.get("blocked_arguments", [])
        warning_arguments = rule.get("warning_arguments", [])

        for argument in tokens[1:]:

            if argument in blocked_arguments:

                return ValidationResult(
                    allowed=False,
                    risk=RiskLevel.HIGH,
                    requires_confirmation=False,
                    reason=f"Argument '{argument}' is blocked.",
                )

            if argument in warning_arguments:

                return ValidationResult(
                    allowed=True,
                    risk=RiskLevel.HIGH,
                    requires_confirmation=True,
                    reason=f"Argument '{argument}' requires confirmation.",
                )

        # ----------------------------------------
        # Validation successful
        # ----------------------------------------

        return ValidationResult(
            allowed=True,
            risk=self.engine.parse_risk(rule["risk"]),
            requires_confirmation=rule["confirm"],
            reason="Validation successful.",
        )