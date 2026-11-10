+++
id = "ref/spell/hide-bruises"
kind = "spell"
title = "Hide Bruises"
aon = "SpellDisplay.aspx?ItemName=Hide%20Bruises"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hide_bruises", path = "json/spells5.json" },
]
[[sources]]
publication = "villain-codex"
page = "20"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (drop of blood)"
range = "touch"
effects = [
  { label = "Target", value = "one creature touched" },
]
duration = "10 minutes/level (D)"
saving_throw = "none and Will disbelief (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Antipaladin, Arcanist, Bard, Inquisitor, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (drop of blood)
Range: touch
Duration: 10 minutes/level (D)
Saving throw: none and Will disbelief (see text)
Spell resistance: yes
Target: one creature touched
Subschool: Glamer
Descriptors: glamer
:::

The target's wounds to seem to disappear. A creature attempting a Heal check to tell the severity of
the target's injuries takes a -10 penalty on that check. A creature that physically touches the
glamered areas can attempt a Will save to recognize it as an illusion.
