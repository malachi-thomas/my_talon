open <user.application_name>: user.focus_or_launch(application_name)
# desk <user.small_number_str>: key("ctrl-{small_number_str}")
snap <user.window_snap_position>: user.snap_window(window_snap_position)

win new | new win: key("cmd-n")
win close | close win: key("cmd-w")
win hide | hide win: key("cmd-h")
win quit | quit win: key("cmd-q")

# Needs Better Touch Tool Needed
# move <user.small_number_str>: key("ctrl-shift-{user.small_number_str}")
