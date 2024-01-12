# ===== Keyboard Shortcuts =====

# Deleting
delete word: key(alt-backspace)
delete line:
  key(home)
  key(cmd-delete)
  key(backspace)
clear line:
  key(home)
  key(cmd-delete)
delete home:
  key(shift-home)
  key(backspace)
delete end:
  key(shift-end)
  key(backspace)
remove space:
  key(alt-left)
  key(backspace)
  key(alt-right)

# Selecting
select word east: key(alt-shift-right)
select word [west]: key(alt-shift-left)
select home: key(shift-home)
select end: key(shift-end)
select line:
  key(home)
  key(shift-end)

# Cutting
cut this: key(cmd-x)
cut word [west]:
  key(shift-alt-left)
  key(cmd-x)
cut word east:
  key(shift-alt-right)
  keep()
cut line:
  key(home)
  key(shift-end)
  key(cmd-x)

# Movements
word west: key(alt-left)
word east: key(alt-right)
key home: key(home)
key  end: key(end)


# Globals
find: key(cmd-f)
undo: key(cmd-z)
redo: key(cmd-shift-z)
tab next: key(ctrl-tab)
tab last: key(ctrl-shift-tab)
save: key(cmd-s)
(spotlight | light) [<user.text>]:
  key(cmd-space)
  sleep(25ms)
  user.add_phrase_to_history(text)
  insert(text)

search: key(shift-cmd-ctrl-alt-s)




force quit: key(alt-cmd-escape)

# Keyboard Use
key(alt-m): user.macro_play("")
key(alt-b): user.clear_last_phrase()
key(alt-r): core.repeat_command(2)



