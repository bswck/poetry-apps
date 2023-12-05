"""Pipx-aware installer for Poetry."""

from __future__ import annotations

from poetry.installation.installer import Installer


class PipxPrecedenceInstaller(Installer):
    """A pipx-aware installer for Poetry."""

    def _do_install(self) -> int:
        """Install packages."""
        return super()._do_install()
