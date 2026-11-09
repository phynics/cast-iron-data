+++
id = "ref/spell/fleshworm-infestation"
kind = "spell"
title = "Fleshworm Infestation"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fleshworm_infestation", path = "json/spells4.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "220"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level (D)"
saving_throw = "Fortitude partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Arcanist, Cleric, Inquisitor, Oracle, Psychic, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level (D)
Saving throw: Fortitude partial (see text)
Spell resistance: yes
Target: creature touched
Subschool: Summoning
Descriptors: evil
:::

With a touch, you cause an infestation of ravenous worms to manifest in the target's flesh. The
target must make a Fortitude save every round. Failure means it takes 1d6 hit points of damage and 2
points of Dexterity damage, and is staggered for 1 round. If it makes the save, it takes no hit
point or Dexterity damage and is only sickened for 1 round rather than staggered. Fleshworm
infestation cannot be ended early by [remove disease](ref/spell/remove-disease) or
[heal](ref/spell/heal), as the infestation starts anew if the current worms are slain.
[Protection from evil](ref/spell/protection-from-evil) negates this spell's effects for as long as
the two durations overlap. [Dispel evil](ref/spell/dispel-evil) automatically ends a fleshworm
infestation.
