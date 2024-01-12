from talon import Context, Module, ui

mod, ctx = Module(), Context()

mod.list("window_snap_positions")

def window_snapper(window, pos):
  screen = window.screen.visible_rect
  x=screen.x + (screen.width * pos.left)
  y=screen.y + (screen.height * pos.top)
  width=screen.width * (pos.right - pos.left)
  height=screen.height * (pos.bottom - pos.top)
  window.rect = ui.Rect(round(x), round(y), round(width), round(height))

class Rect:
  def __init__(self, left, top, right, bottom):
    self.left = left
    self.top = top
    self.bottom = bottom
    self.right = right

window_positions = {
  "west": Rect(0, 0, 0.5, 1),
  "east": Rect(0.5, 0, 1, 1),
  "north": Rect(0, 0, 1, 0.5),
  "south": Rect(0, 0.5, 1, 1),
  "center": Rect(1 / 3, 0, 2 / 3, 1),
  "west small": Rect(0, 0, 1 / 3, 1),
  "east small": Rect(2 / 3, 0, 1, 1),
  "west large": Rect(0, 0, 2 / 3, 1),
  "east large": Rect(1 / 3, 0, 1, 1),
  "north west": Rect(0, 0, 0.5, 0.5),
  "north east": Rect(0.5, 0, 1, 0.5),
  "south west": Rect(0, 0.5, 0.5, 1),
  "south east": Rect(0.5, 0.5, 1, 1),
  "north west small": Rect(0, 0, 1 / 3, 0.5),
  "north east small": Rect(2 / 3, 0, 1, 0.5),
  "north west large": Rect(0, 0, 2 / 3, 0.5),
  "north east large": Rect(1 / 3, 0, 1, 0.5),
  "north center small": Rect(1 / 3, 0, 2 / 3, 0.5),
  "south west small": Rect(0, 0.5, 1 / 3, 1),
  "south east small": Rect(2 / 3, 0.5, 1, 1),
  "south west large": Rect(0, 0.5, 2 / 3, 1),
  "south east large": Rect(1 / 3, 0.5, 1, 1),
  "south center small": Rect(1 / 3, 0.5, 2 / 3, 1),
  "center": Rect(1 / 8, 1 / 6, 7 / 8, 5 / 6),
  "full": Rect(0, 0, 1, 1),
  "fullscreen": Rect(0, 0, 1, 1),
}

ctx.lists["user.window_snap_positions"] = window_positions.keys()

@mod.capture(rule="{user.window_snap_positions}")
def window_snap_position(m) -> Rect:
    return window_positions[m.window_snap_positions]

@mod.action_class
class Actions:
  def snap_window(position: Rect) -> None:
    ""
    window_snapper(ui.active_window(), position)