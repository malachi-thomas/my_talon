from talon import Context, Module
mod, ctx = Module(), Context()
mod.list("modifiers")

ctx.lists["self.modifiers"] = {
  "command": "cmd",
  "controll": "ctrl",
  "shift": "shift",
  "alt": "alt",
  "cord": "cmd-shift",
  "troll": "ctrl-shift",
}

@mod.capture(rule="{self.modifires}+")
def modifires(m) -> str: return str(m).replace(" ", "-")
