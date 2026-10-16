"""Zorgt dat de starter-modules (opgave/starter) importeerbaar zijn in pytest."""

import sys
from pathlib import Path

STARTER = Path(__file__).resolve().parent.parent / "opgave" / "starter"
sys.path.insert(0, str(STARTER))
