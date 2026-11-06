+++
id = "ref/spell/sure-casting"
kind = "spell"
title = "Sure Casting"
source_ids = ["pathfinder-society-primer"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sure_casting", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, F (a square of cloth and a needle)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round (see text)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Arcanist, Bard, Cleric, Inquisitor, Oracle, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, F (a square of cloth and a needle)
Range: personal
Duration: 1 round (see text)
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Pathfinder Society Primer pg 13

You gain temporary insight into your enemies' magical defenses. When you next cast a spell before
the end of the next round, treat your caster level as 5 higher than normal for the purpose of
overcoming [spell resistance](ref/rule/spell-resistance). This bonus doesn't increase any other
effects that depend on caster level, such as the spell's damage or range, and affects only the first
spell cast after sure casting.
