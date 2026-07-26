#!/usr/bin/env python3
"""Compile the generator and validate every committed Draw.io example."""

from __future__ import annotations

import py_compile
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "drawio-mxgraph" / "scripts" / "drawio_tool.py"
EXAMPLES = (
    ROOT / "examples" / "agentbuilder-customer-service-architecture.drawio",
    ROOT / "examples" / "agentbuilder-customer-service-flow.drawio",
)


def main() -> int:
    py_compile.compile(str(TOOL), doraise=True)

    for example in EXAMPLES:
        subprocess.run(
            [sys.executable, str(TOOL), "validate", str(example)],
            check=True,
        )

    print(f"Validated {len(EXAMPLES)} example diagrams.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
