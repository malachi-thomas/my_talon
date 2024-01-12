from talon import Context, Module
from ...util import csv_to_object
mod, ctx = Module(), Context()
mod.list("file_extentions")
ctx.lists["self.file_extentions"] = {
  "dot pie": ".py",
  "dot com": ".com",
}

@mod.capture(rule="{self.file_extentions}")
def file_extentions(m) -> str:
  return str(m)
