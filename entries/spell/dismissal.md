+++
id = "ref/spell/dismissal"
kind = "spell"
title = "Dismissal"
source_ids = ["core-rulebook", "planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dismissal", path = "json/spells13.json" },
]
[[sources]]
publication = "core-rulebook"
page = "271"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one extraplanar creature" },
]
duration = "instantaneous"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Cleric, Inquisitor, Medium, Occultist, Oracle, Shaman, Summoner, Warpriest\
5: Arcanist, Psychic, Sorcerer, Spiritualist, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates; see text
Spell resistance: yes
Target: one extraplanar creature
:::

This spell forces an extraplanar creature back to its proper plane if it fails a Will save. If the
spell is successful, the creature is instantly whisked away, but there is a 20% chance of actually
sending the subject to a plane other than its own.
