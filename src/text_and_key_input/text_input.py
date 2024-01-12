from talon import Context, Module, actions
from ...format_phrase import format_phrase
mod, ctx = Module(), Context()
mod.list("text_replacements")
mod.list("phrase_punctuation")

ctx.lists["self.text_replacements"] = {
  "hat": "cow",
  "che": "key",
  "ki": "key",
  "nat west": "natwest",
}

ctx.lists["self.phrase_punctuation"] = {
  "space": " ",
  "slap": "\n",
}
@mod.capture(
  rule="({self.text_replacements} | {user.phrase_punctuation} | {user.symbol_keys} | {user.extra_symbol_keys} | <phrase>)+")
def text(m) -> str:
  return format_phrase(m).lower()
