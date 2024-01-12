from talon import Module, actions

mod= Module()
mod.list("text")

@mod.action_class
class Actions:
  def delete_line() -> None:
    ""
    actions.key("end")
    actions.key("cmd-backspace")
    actions.key("backspace")
  def clear_line() -> None:
    ""
    actions.key("end")
    actions.key("shift-home")
    actions.key("backspace")
  def delete_word() -> None:
    ""
    actions.key("alt-left")
    actions.key("alt-right")
    actions.key("alt-backspace")
  def delete_home() -> None:
    ""
    actions.key("cmd-delete")
  def delete_end() -> None:
    ""
    actions.key("cmd-backspace")
  def delete_num_words(num: int) -> None:
    ""
    for _ in range(num):
      actions.key("alt-backspace")
  def select_word() -> None:
    ""
    actions.key("shift-alt-left")

  def select_inside_word() -> None:
    ""
    actions.key("alt-left")
    actions.key("alt-shift-right")
  def select_home() -> None:
    ""
    actions.key("shift-home")
  def select_end() -> None:
    ""
    actions.key("shift-end")
  def select_line() -> None:
    ""
    actions.key("end")
    actions.key("shift-home")
  def word_west() -> None:
    ""
    actions.key("alt-left")
  def word_east() -> None:
    ""
    actions.key("alt-right")
  def home() -> None:
    ""
    actions.key("home")
  def end() -> None:
    ""
    actions.key("end")
  def cut_line() -> None:
    ""
    actions.key("home")
    actions.key("shift-end")
    actions.key("cmd-x")
  def cut_word() -> None:
    ""
    actions.key("alt-left")
    actions.key("shift-alt-right")
    actions.key("cmd-x")





  def add_surrounds_to_word(key: str) -> None:
    ""
    actions.key("alt-left")
    actions.key(key)
    actions.key("alt-right")
    actions.key(key)


