

# from talon import Context, Module, actions, app, clip, fs, imgui, ui




homophones = [
  ["key", "ki", "che"],
  ["cat", "kat"],
  ["call", "coal", "cool"],
  ["eye", "i"],
  ["gym", "jim"],
  ["by", "buy", "bye"],
]

def homophones_to_list(homophone_list):
  phones = {}
  for homophone_words in homophone_list:
    for word in homophone_words:
      phones.update(word)


homophones_to_list(homophones)