"""Plugins provided by the package."""

from cleo.events.console_command_event import ConsoleCommandEvent
from cleo.events.console_events import COMMAND
from cleo.events.event_dispatcher import EventDispatcher
from cleo.io.io import IO
from poetry.console.application import Application
from poetry.console.commands.installer_command import InstallerCommand
from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_apps.installer import AppInstaller

PRIORITY = 1


class AppsPlugin(ApplicationPlugin):
    """Allow pipx to take precedence when installing CLI apps as dependencies."""

    def activate(self, application: Application) -> None:
        """Activate the plugin."""
        if application.event_dispatcher:
            application.event_dispatcher.add_listener(
                COMMAND,
                self.on_command,  # type: ignore[arg-type]
                priority=PRIORITY,
            )

    def on_command(
        self,
        event: ConsoleCommandEvent,
        event_name: str,  # noqa: ARG002
        dispatcher: EventDispatcher,  # noqa: ARG002
    ) -> None:
        """
        Capture any installer command (update, install).

        Configure the pipx-precedence installer.
        """
        command = event.command
        if isinstance(command, InstallerCommand):
            self.configure_installer_for_command(command, event.io)

    @staticmethod
    def configure_installer_for_command(command: InstallerCommand, io: IO) -> None:
        """Configure the pipx-precedence installer for the command."""
        poetry = command.poetry
        installer = AppInstaller(
            io,
            command.env,
            poetry.package,
            poetry.locker,
            poetry.pool,
            poetry.config,
            disable_cache=poetry.disable_cache,
        )
        command.set_installer(installer)
