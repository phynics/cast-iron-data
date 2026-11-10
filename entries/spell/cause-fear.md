+++
id = "ref/spell/cause-fear"
kind = "spell"
title = "Cause Fear"
aon = "SpellDisplay.aspx?ItemName=Cause%20Fear"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cause_fear", path = "json/spells2.json" },
]
[[sources]]
publication = "core-rulebook"
page = "252"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["emotion", "fear", "mind-affecting"]
levels = [
  { class = "Adept", level = 1 },
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature with 5 or fewer HD" },
]
duration = "1d4 rounds or 1 round; see text"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Adept, Antipaladin, Arcanist, Bloodrager, Bard, Cleric, Inquisitor, Medium, Mesmerist, Occultist, Oracle, Psychic, Shaman, Skald, Sorcerer, Spiritualist, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1d4 rounds or 1 round; see text
Saving throw: Will partial
Spell resistance: yes
Target: one living creature with 5 or fewer HD
Descriptors: emotion, fear, mind-affecting
:::

The affected creature becomes frightened. If the subject succeeds on a Will save, it is shaken for 1
round. Creatures with 6 or more HD are immune to this effect. Cause fear counters and dispels
[remove fear](ref/spell/remove-fear).
