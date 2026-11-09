+++
id = "ref/spell/haunting-reminder"
kind = "spell"
title = "Haunting Reminder"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "haunting_reminder", path = "json/spells5.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "37"

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["fear", "mind-affecting"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "12 hours + 2 hours/level or until triggered, then 1 day/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Antipaladin\
2: Arcanist, Bard, Inquisitor, Mesmerist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 12 hours + 2 hours/level or until triggered, then 1 day/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: fear, mind-affecting
:::

As part of casting this spell, you can attempt a single Intimidate check to make the target act
friendly to you. If you succeed, the target assists you normally, but it remains fearful of your
retribution even after its attitude shifts to unfriendly. If the creature reports your coercion to
authorities, attacks you, or otherwise acts in a purposeful way that threatens you or your
objectives (at the GM's discretion), the spell triggers, inflicting the creature with the unshakable
certainty that you will find and punish it. This imposes the shaken condition on the creature for 1
day per caster level; during this time, the creature takes a -2 penalty on saving throws against
spells you cast with the fear descriptor.
