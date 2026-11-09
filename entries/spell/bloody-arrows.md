+++
id = "ref/spell/bloody-arrows"
kind = "spell"
title = "Bloody Arrows"
source_ids = ["ranged-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bloody_arrows", path = "json/spells2.json" },
]
[[sources]]
publication = "ranged-tactics-toolbox"
page = "30"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one willing creature" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no (harmless)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Antipaladin, Hunter, Inquisitor, Magus, Ranger\
4: Arcanist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: none
Spell resistance: no (harmless)
Target: one willing creature
:::

Whenever this spell's target hits a creature with a ranged weapon that successfully deals piercing
or slashing damage, the struck creature takes 1 point of bleed damage. Unlike most bleed damage, the
bleed damage dealt by the subject of this spell is cumulative up to an amount equal to 1/2 your
caster level (to a maximum of 5 points of bleed damage at 10th level).
