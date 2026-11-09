+++
id = "ref/spell/delay-pain"
kind = "spell"
title = "Delay Pain"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "delay_pain", path = "json/spells3.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "216"

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["emotion"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 hour/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Arcanist, Bloodrager, Bard, Cleric, Inquisitor, Mesmerist, Oracle, Psychic, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: emotion
:::

You override the target's ability to feel pain. Pain effects (such as pain strike and symbol of
pain) do not affect the target until this spell's duration has expired. This does not negate any
physical damage, ability damage, or ability drain that a pain effect has already done, but it does
negate ongoing penalties from pain while the spell lasts.
