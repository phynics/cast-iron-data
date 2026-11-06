+++
id = "ref/spell/diminished-detection"
kind = "spell"
title = "Diminished Detection"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "diminished_detection", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of wool)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Alchemist, Arcanist, Bard, Investigator, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of wool)
Range: personal
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Inner Sea Intrigue pg 59

You can avoid being detected when you are on the edges of some divination spells' ranges. Whenever
you would normally be within the area of effect of a detection spell (such as
[detect magic](ref/spell/detect-magic), [detect evil](ref/spell/detect-evil), or
[detect undead](ref/spell/detect-undead)), the area of effect is reduced by half for the purposes of
the spell's caster detecting you or your possessions. The caster of the detect spell is unaware of
this reduction in her spell's range; she simply does not detect you.
