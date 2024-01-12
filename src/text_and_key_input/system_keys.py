from talon import Context, Module
mod, ctx = Module(), Context()
mod.list("system_keys")
ctx.lists["self.system_keys"] = {
  "go north": "up",
  "go east": "right",
  "go south": "down",
  "go west": "left",
  "void": "space",
  "slap": "enter",
  "wipe": "backspace",
  "escape": "escape",
}

@mod.capture(rule="{self.system_keys}")
def system_keys(m) -> str:
  return m.system_keys
