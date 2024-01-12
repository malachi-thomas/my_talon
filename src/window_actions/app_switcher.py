from talon import Module, Context, ui
from ...util import csv_to_object

mod, ctx = Module(), Context()
mod.list("application_name")
ctx.lists["self.application_name"] = {
  "slack": "/Applications/Slack.app",
  "chrome": "/Applications/Google Chrome.app",
  "code": "/Applications/Visual Studio Code.app",
  "safari": "/Applications/Safari.app",
  "terminal": "/Applications/Alacritty.app",
  "finder": "/System/Library/CoreServices/Finder.app",
}

@mod.capture(rule="{self.application_name}")
def application_name(m) -> str:
  return str(m)

@mod.action_class
class Actions:
  def focus_or_launch(s: str):
    ""
    ui.launch(path=s)

