from talon import Context, Module
from ...util import csv_to_object

mod, ctx = Module(), Context()
mod.list("website_names")

ctx.lists["user.website_names"] = {
  "google": "google.com",
  "talon": "docs,talon.wiki/unofficial_talon_docs",
  "youtube": "youtube.com",
  "github": "github.com",
  "rust crates": "crates.io",
}

@mod.capture(rule="{self.website_names}")
def website_names(m) -> str:
  return str(m)


