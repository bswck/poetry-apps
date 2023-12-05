"""App installer for Poetry."""

from __future__ import annotations

from poetry.installation.installer import Installer


class AppInstaller(Installer):
    """App installer for Poetry."""

    def _do_install(self) -> int:
        """Install packages."""
        return super()._do_install()
