"""Plugins provided by the package."""

from cleo.events.console_command_event import ConsoleCommandEvent
from cleo.events.console_events import COMMAND
from cleo.events.event_dispatcher import EventDispatcher
from poetry.console.application import Application
from poetry.console.commands.install import InstallCommand
from poetry.plugins.application_plugin import ApplicationPlugin


class PipxPlugin(ApplicationPlugin):
    """Allow pipx to take precedence when installing CLI apps as dependencies."""

    def activate(self, application: Application) -> None:
        """Activate the plugin."""
        application.event_dispatcher.add_listener(COMMAND, self.on_command)

    def on_command(
        self,
        event: ConsoleCommandEvent,
        event_name: str,  # noqa: ARG002
        dispatcher: EventDispatcher,  # noqa: ARG002
    ) -> None:
        """Capture the install command and modify it to use pipx."""
        if not isinstance(event.command, InstallCommand):
            return
