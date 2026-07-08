from dataclasses import dataclass
from app.models.command import RiskLevel


@dataclass
class CommandRule:
    """
    Represents a validation rule for a Linux command.
    """

    command: str

    risk: RiskLevel

    requires_confirmation: bool

    blocked_arguments: set[str]

    warning_arguments: set[str]