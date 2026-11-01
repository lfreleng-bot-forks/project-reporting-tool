# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 The Linux Foundation

"""Transitional alias for the moved CLI package.

The package now lives at ``lf_releng_project_reporting.cli``. This module
registers every one of its modules under the old top-level ``cli`` name,
so ``import cli.errors`` yields the very module the package uses rather
than a second copy. It exists only until the tests import the new path.
"""

import importlib
import pkgutil
import sys

import lf_releng_project_reporting.cli as _cli


for _info in pkgutil.walk_packages(_cli.__path__, f"{_cli.__name__}."):
    if _info.name.endswith(".__main__"):
        continue
    _alias = "cli" + _info.name.removeprefix(_cli.__name__)
    sys.modules[_alias] = importlib.import_module(_info.name)

sys.modules[__name__] = _cli
