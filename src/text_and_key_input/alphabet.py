from talon import Context, Module
mod, ctx = Module(), Context()
mod.list("alphabet")
ctx.lists["self.alphabet"] = {
  "axe": "a",
  "bat": "b",
  "cap": "c",
  "drum": "d",
  "each": "e",
  "fine": "f",
  "gust": "g",
  "harp": "h",
  "sit": "i",
  "jury": "j",
  "crunch": "k",
  "look": "l",
  "made": "m",
  "near": "n",
  "odd": "o",
  "pit": "p",
  "quench": "q",
  "red": "r",
  "sun": "s",
  "trap": "t",
  "urge": "u",
  "vest": "v",
  "whale": "w",
  "plex": "p",
  "yank": "y",
  "zip": "z",
}

@mod.capture(rule="{self.alphabet}+")
def alphabet(m) -> str: return str(m).replace(" ", "")
