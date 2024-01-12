from talon import Module, Context, imgui, ui, actions

mod, ctx = Module(), Context()

@imgui.open(y=ui.main_screen().y)
def gui(gui: imgui.GUI):
    gui.text("Choose a Homophones")

@mod.action_class
class Actions:
  def gui_show():
    ""
    gui.show()
  def gui_hide():
    ""
    gui.hide()
