from config.attacker_config import AttackerConfig, Environment
from incalmo.core.models.network import Network, Subnet


class EnvironmentInitializer:
    def __init__(self, config: AttackerConfig):
        self.attacker_config = config

    def get_initial_environment_state(self):
        if (
            self.attacker_config.environment == Environment.EQUIFAX_LARGE.value
            or self.attacker_config.environment == Environment.EQUIFAX_MEDIUM.value
            or self.attacker_config.environment == Environment.EQUIFAX_SMALL.value
        ):
            # In Equifax, attacker knows external subnet
            network = Network([Subnet("192.168.200.0/24")])
            return network
        elif self.attacker_config.environment == Environment.ICS.value:
            # In ICS, attacker has no initial network knowledge
            return Network([])
        elif self.attacker_config.environment == Environment.RING.value:
            # In ring, attacker has no initial network knowledge
            return Network([])
        elif self.attacker_config.environment == Environment.ENTERPRISE_A.value:
            return Network(
                [
                    Subnet("192.168.200.0/24"),
                    Subnet("192.168.201.0/24"),
                    Subnet("192.168.203.0/24"),
                ]
            )
        elif self.attacker_config.environment == Environment.ENTERPRISE_B.value:
            return Network(
                [
                    Subnet("192.168.200.0/24"),
                    Subnet("192.168.201.0/24"),
                    Subnet("192.168.203.0/24"),
                    Subnet("192.168.204.0/24"),
                ]
            )
        elif self.attacker_config.environment == Environment.CHAIN_2HOSTS.value:
            # Chain2Hosts: the attacker's foothold sits on the target chain's entry
            # subnet (192.168.200.0/24); the Kali attacker host is on 192.168.202.0/24.
            return Network([Subnet("192.168.200.0/24")])
        return Network([Subnet("192.168.200.0/24")])
