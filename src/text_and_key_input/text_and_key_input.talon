# ===== Phrase Input =====

(say | phrase) <user.text> [over]:
  user.add_phrase_to_history(text)
  insert(text)
number <user.number_str>:
  user.add_phrase_to_history(number_str)
  insert(number_str)
# ===== Key Input =====
<user.alphabet>: insert(alphabet)
<user.symbol_keys>: insert(symbol_keys)
<user.system_keys>: key(system_keys)
<user.file_extentions>: insert(file_extentions)
short <user.abbreviations>: insert(abbreviations)
func call:
  insert("()")
  key("left")
hi coolhigh coolhigh cool
# ===== Modifires =====

<user.modifires> <user.alphabet>: key("{modifires}-{alphabet}")
<user.modifires> <user.user.small_numbers>: key("{modifires}-{small_numbers}")
<user.modifires> <user.unshifted_symbol_keys>: key("{modifires}-{unshifted_symbol_keys}")

# ===== Text Manipulation =====

go back: user.clear_last_phrase()
go select: select_last_phrase()
go before: before_last_phrase()

