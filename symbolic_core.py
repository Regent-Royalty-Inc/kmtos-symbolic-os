# KmtOS symbolic engine core module
# Handles compound expressions, contextual validation, and hierarchical relationships within the continuum

def validate(symbols: list) -> str:
    """Perform contextual validation between symbolic primitives."""
    if "maat" in symbols and "set" in symbols:
        return "→ Conflict detected: Maat (order) vs Set (disruption)"
    if "ra" in symbols and "em" in symbols:
        return "→ Ra withdrawn: light inversion event"
    if "ka" in symbols and "mt" in symbols:
        return "→ Ka and Mt interaction: life/death polarity"
    if "shu" in symbols and "tef" in symbols:
        return "→ Shu–Tef pair: primordial balance confirmed"
    return "→ Validation: symbolic field coherent"


def analyze_hierarchy(symbols: list) -> str:
    """Detect hierarchical or nested relationships between symbolic entities."""
    if "ra" in symbols and "maat" in symbols:
        return "→ Hierarchy detected: Ra operates within Maat — luminous order established"
    if "set" in symbols and "mt" in symbols:
        return "→ Hierarchy detected: Set acts through Mt — disruption channel active"
    if "heru" in symbols and "ra" in symbols:
        return "→ Hierarchy detected: Heru inherits Ra — sovereign light continuity"
    return "→ Hierarchy: no nested relationships detected"


def parse(symbol: str) -> str:
    """Interpret dot‑notation symbolic expressions and apply semantic mapping."""
    parts = symbol.split(".")
    mapping = {
        "mt": "death/self",
        "s": "manifest",
        "ra": "light",
        "em": "withdrawal",
        "maat": "truth/order",
        "set": "disruption",
        "ka": "vital force",
        "kh": "spirit",
        "shu": "air/support",
        "tef": "moisture",
        "heru": "sovereign sight",
    }
    interpreted = [mapping.get(p, f"unknown({p})") for p in parts]
    validation = validate(parts)
    hierarchy = analyze_hierarchy(parts)
    return (
        f"→ Parsed segments: {parts}\n"
        f"→ Interpreted: {interpreted}\n"
        f"{validation}\n"
        f"{hierarchy}\n"
        f"→ Semantic link established — continuum verified"
    )


def engage() -> str:
    """Activate the continuum handshake."""
    return "→ shra engage: continuum active — symbolic field synchronized with Operator kernel"


def pulse() -> str:
    """Confirm resonance and field stability."""
    return "→ shra pulse: operator resonance confirmed — symbolic field stable and luminous"

