from dataclasses import dataclass

from app.models.command import RiskLevel


@dataclass
class ValidationResult:
    """
    Result returned by the SecurityValidator.
    """

    allowed: bool
    risk: RiskLevel
    requires_confirmation: bool
    reason: str