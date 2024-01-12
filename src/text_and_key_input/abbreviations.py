from talon import Context, Module
from ...util import csv_to_object
mod, ctx = Module(), Context()
mod.list("abbreviations")
ctx.lists["self.abbreviations"] = {
  "string": "str",
  "interger": "int",
  "email": "malachithomas110@gmail.com",
}

@mod.capture(rule="{self.abbreviations}")
def abbreviations(m) -> str:
  return str(m)
