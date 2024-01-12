from talon import Context, Module

mod, ctx = Module(), Context()

mod.list("symbol_keys")
mod.list("extra_symbol_keys")

ctx.lists["self.symbol_keys"] = {
  "slash": "/",
  "quote": "",
  "tick": "`",
  "quote": "'",
  "grave": "~",
  "drip": ",",
  "span": ",",
  # "dot": ".",
  "point": ".",
  "semicolon": ";",
  "backslash": "\\",
  "dash": "-",
  "square": "[",
  "right square": "]",
}

ctx.lists["self.extra_symbol_keys"] = {
  "question": "?",
  "dollar": "$",
  "star": "*",
  "hash": "#",
  "percent": "%",
  "at sign": "@",
  "quad": '"',
  "plus": "+",
  "downscore": "_",
  "floor": "_",
  "stack": ":",
  "ampersand": "&",
  "pound sign": "£",
  "peren": "(",
  "right peren": ")",
  "perens": "()",
  "brack": "{",
  "right brack": "}",
  "bracks": "{",
  "arrow": "->",
  "dub arrow": "=>",
  "angle": "<",
  "rangle": ">",
  "minus": "-",
}

@mod.capture(rule="{user.symbol_keys} | {user.extra_symbol_keys}")
def symbol_keys(m) -> str:
  return str(m)

@mod.capture(rule="{user.symbol_keys}")
def unshifted_symbol_keys(m) -> str:
  return str(m)
