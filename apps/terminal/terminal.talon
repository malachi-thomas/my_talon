app: Alacritty
-

command <user.terminal_commands>: insert(terminal_commands)
# flag <user.terminal_flags>: insert(terminal_flags)


list all:
  insert("la")
  key("enter")

go back:
  insert("cd ../")
  key("enter")

move to:
  insert("cd ")

copy this: insert("cp ")
move this: "mv "
link this: "ln"
link force:"ln -f"
tab key: key(tab)

cancel: key(ctrl-c)