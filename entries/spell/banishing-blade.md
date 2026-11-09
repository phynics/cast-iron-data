+++
id = "ref/spell/banishing-blade"
kind = "spell"
title = "Banishing Blade"
aon = "SpellDisplay.aspx?ItemName=Banishing%20Blade"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "banishing_blade", path = "json/spells12.json" },
]
[[sources]]
publication = "arcane-anthology"
page = "7"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 5 },
  { class = "Bloodrager", level = 4 },
  { class = "Inquisitor", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Medium", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one melee weapon" },
]
duration = "1 round/level or until discharged"
saving_throw = "none and Will partial (see text)"
spell_resistance = "yes (see text)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Antipaladin, Bloodrager, Medium, Paladin\
5: Arcanist, Inquisitor, Magus, Shaman, Sorcerer, Spiritualist, Summoner, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level or until discharged
Saving throw: none and Will partial (see text)
Spell resistance: yes (see text)
Effect: one melee weapon
:::

You imbue a weapon with the power to drive foes back. The first time each round the weapon strikes a
creature, the weapon attempts a free bull rush combat maneuver check against that creature. This
does not provoke attacks of opportunity. The combat maneuver for the bull rush is equal to 1d20 +
your caster level. You do not have to move to push creatures more than 5 feet with this bull rush.
If a creature you strike has [spell resistance](ref/rule/spell-resistance), you must attempt a
caster level check to overcome its spell resistance the first time you strike it. If you fail, that
creature is immune to the effects of this casting of banishing blade.

The first time each extraplanar creature whose Hit Dice don't exceed your caster level is driven
back at least 10 feet by this spell, it must attempt a Will save. If it fails, it is sent back to
its home plane. Whether it succeeds or fails, that creature is staggered for 1 round and banishing
blade's duration ends.
