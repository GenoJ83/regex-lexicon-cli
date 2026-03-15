from typing import Dict, List, Optional
from src.core.models import PatternEntry

PREBUILT_PATTERNS: Dict[str, PatternEntry] = {
    "email": PatternEntry(
        slug="email",
        title="RFC 5322 Email Address",
        pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        category="network",
        description="Standard email format validation",
        examples_match=["alice@example.com", "user+tag@domain.co.uk"],
        examples_fail=["missing-at.com", "@domain.com"]
    ),
    "ipv4": PatternEntry(
        slug="ipv4",
        title="IPv4 Address",
        pattern=r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
        category="network",
        description="Valid IPv4 dotted decimal address",
        examples_match=["192.168.1.1", "10.0.0.1", "255.255.255.255"],
        examples_fail=["256.0.0.1", "1.2.3"]
    ),
    "uuid": PatternEntry(
        slug="uuid",
        title="UUID v4",
        pattern=r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
        category="identifiers",
        description="Canonical 36-char hexadecimal UUID string",
        examples_match=["123e4567-e89b-12d3-a456-426614174000"],
        examples_fail=["not-a-uuid"]
    ),
    "semver": PatternEntry(
        slug="semver",
        title="Semantic Versioning 2.0",
        pattern=r"^v?(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$",
        category="software",
        description="Semantic version string with optional prerelease and build metadata",
        examples_match=["1.0.0", "v2.1.3-beta.1", "0.3.4+exp.sha.5114f85"],
        examples_fail=["1.0", "v1.2.a"]
    )
}

def get_pattern(slug: str) -> Optional[PatternEntry]:
    return PREBUILT_PATTERNS.get(slug)

def list_categories() -> List[str]:
    return sorted(list(set(p.category for p in PREBUILT_PATTERNS.values())))
