
# import os

# from talon import Context, Module, actions, app, clip, fs, imgui, ui
# cwd = os.path.dirname(os.path.realpath(__file__))
# homophones_file = os.path.join(cwd, "homophones.csv")

# mod, ctx = Module(), Context()

# phones = {}
# canonical_list = []
# with open(homophones_file) as f:
#   for line in f:
#     words = line.rstrip().split(",")
#     canonical_list.append(words[0])
#     merged_words = set(words)
#     for word in words:
#       old_words = phones.get(word.lower(), [])
#       merged_words.update(old_words)
#       merged_words = sorted(merged_words)
#       for word in merged_words:
#         phones[word.lower()] = merged_words
# global all_homophones
# all_homophones = phones
# ctx.lists["self.homophones_canonicals"] = canonical_list

# @imgui.open(y=ui.main_screen().y)
# def gui(gui: imgui.GUI):
#     global active_word_list
#     gui.text("Select a homophone")
#     gui.line()
#     index = 1
#     for word in active_word_list:
#       if gui.button(f"choose {index}: {word}"):
#             actions.insert(actions.user.homophones_select(index))
#             actions.user.homophones_hide()
#         index = index + 1

#     if gui.button("Phones hide"):
#         actions.user.homophones_hide()

