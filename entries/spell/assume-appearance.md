+++
id = "ref/spell/assume-appearance"
kind = "spell"
title = "Assume Appearance"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "assume_appearance", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/alter-self" },
]
[[sources]]
publication = "horror-adventures"
page = "108"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 minute"
components = "V, S, F (corpse of the deceased creature whose form you plan to assume)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 day/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Arcanist, Bard, Investigator, Medium, Mesmerist, Occultist, Psychic, Shaman, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 minute
Components: V, S, F (corpse of the deceased creature whose form you plan to assume)
Range: personal
Duration: 1 day/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

This spell functions similarly to [alter self](ref/spell/alter-self), except for the following
differences. You assume the exact form of a deceased Small or Medium creature of the humanoid type.
Your voice changes to match that of the form you assume. The creature whose form you assume must be
dead and you must have access to its fresh corpse (either dead less than 24 hours, or preserved via
[gentle repose](ref/spell/gentle-repose) or similar effect). Any attempt to copy the form of a
living creature causes the spell to fail. You do not have access to the assumed form's abilities,
memories, mannerisms, or speech patterns. The spell grants a +10 bonus on Disguise checks to appear
as the imitated creature.

If the assumed creature is returned to life while this spell is active, assume appearance
immediately ends.
