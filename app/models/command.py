from enum import Enum

from pydantic import BaseModel


class RiskLevel(str, Enum):

    SAFE = "safe"

    MEDIUM = "medium"

    HIGH = "high"


class LinuxCommand(BaseModel):

    command: str

    description: str

    risk: RiskLevel

    requires_confirmation: bool