from typing import Any
import ipaddress


class FilterModule:
    @staticmethod
    def ensure_domain(name: str, domain: str) -> str:
        """
        Ensure that `name` ends with the given `domain`.

        - If already a FQDN under `domain`, return unchanged.
        - If no dot in name, append domain.
        - If `name` is an IP address, return unchanged.
        """
        if not domain:
            return name

        try:
            ipaddress.ip_address(name)
            return name
        except ValueError:
            pass

        domain = domain.lstrip(".")

        if name.endswith("." + domain) or name == domain:
            return name
        return f"{name}.{domain}"

    def filters(self) -> dict[str, Any]:
        return {
            "ensure_domain": self.ensure_domain,
        }
