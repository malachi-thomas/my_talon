from talon import Context, Module
mod, ctx = Module(), Context()
mod.list("function_keys")
ctx.lists["self.function_keys"] = {
  "fun one": "f1",
  "fun two": "f2",
  "fun three": "f3",
  "fun four": "f4",
  "fun five": "f5",
  "fun six": "f6",
  "fun seven": "f7",
  "fun eight": "f8",
  "fun nine": "f9",
  "fun ten": "f10",
  "fun eleven": "f11",
  "fun twelve": "f12",
}

@mod.capture(rule="{self.function_keys}")
def function_keys(m) -> str: str(m.function_keys)
