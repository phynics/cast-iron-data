+++
id = "ref/spell/threefold-sight"
kind = "spell"
title = "Threefold Sight"
aon = "SpellDisplay.aspx?ItemName=Threefold%20Sight"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "threefold_sight", path = "json/spells10.json" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "25"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a three-pointed knot)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "3 minutes"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Arcanist, Bard, Medium, Occultist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a three-pointed knot)
Range: personal
Duration: 3 minutes
Saving throw: none
Spell resistance: no
Target: you
:::

You view several possible futures at once, allowing you to thread a needle around disasters by
taking a middle path. For the duration of this spell, whenever you roll for an attack, saving throw,
or skill check, roll three d20 and use the middle of the three rolls (or the highest, if more than
one die shows the same highest value, or the lowest, if more than one die shows the same lowest
value). If another ability would make you roll an attack roll, saving throw, or skill check twice
and take the higher result, roll twice and take the lower result, or reroll, that ability has no
effect and threefold sight ends immediately.
