from app.models.command import RiskLevel
from app.security.policy_loader import PolicyLoader


class RuleEngine:

    def __init__(self):

        self.policy = PolicyLoader().load()

    def get_rule(self, executable):

        return self.policy["commands"].get(executable)

    def blocked_commands(self):

        return self.policy["blocked_commands"]

    def parse_risk(self, risk):

        return RiskLevel(risk)