from talon import Context, Module
mod, ctx = Module(), Context()
mod.list("terminal_commands")
ctx.lists["self.terminal_commands"] = {
  "change": "cd ",
  "go back": "../",
  "copy ": "cp ",

}

@mod.capture(rule="{self.terminal_commands}")
def terminal_commands(m) -> str:
  return str(m)
