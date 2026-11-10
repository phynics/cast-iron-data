+++
id = "ref/spell/death-candle"
kind = "spell"
title = "Death Candle"
aon = "SpellDisplay.aspx?ItemName=Death%20Candle"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "death_candle", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/death-knell" },
]
[[sources]]
publication = "advanced-race-guide"
page = "131"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death", "evil", "fire"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 round"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous/1 round per hd of subject; see text"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Antipaladin\
2: Cleric, Inquisitor, Oracle, Warpriest, Witch
Casting time: 1 round
Components: V, S
Range: touch
Duration: instantaneous/1 round per hd of subject; see text
Saving throw: Fortitude negates
Spell resistance: yes
Target: living creature touched
Descriptors: death, evil, fire
:::

> _[Ifrits](ref/race/ifrit) have access to the following spell._

This spell functions like [death knell](ref/spell/death-knell), except instead of using the slain
target's life energy to enhance yourself, you use it to summon a Small fire elemental resembling a
burning, howling version of the slain creature. The elemental acts immediately on your turn and
otherwise behaves as if you had summoned it with [summon monster II](ref/spell/summon-monster-2).
The elemental remains for a number of rounds equal to the Hit Dice of the slain creature.
