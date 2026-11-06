+++
id = "ref/spell/fallback-strategy"
kind = "spell"
title = "Fallback Strategy"
source_ids = ["inner-sea-gods", "gods-and-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fallback_strategy", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level or until discharged; see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Cleric, Inquisitor, Magus, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 1 minute/level or until discharged; see text
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Inner Sea Gods pg 233, Gods and Magic pg 39

While this spell is active, you may reroll one attack roll, combat maneuver check, or skill check
before the result of the roll or check is known. You must take the result of the reroll, even if
it's worse than the original roll. Once the reroll is used, the spell ends. You can have no more
than one fallback strategy active on you at the same time.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
