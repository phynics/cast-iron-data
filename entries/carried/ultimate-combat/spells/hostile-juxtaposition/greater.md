+++
id = "ref/carried/ultimate-combat/spells/hostile-juxtaposition/greater"
kind = "spell"
title = "Hostile Juxtaposition, Greater"
source_ids = ["ultimate-combat"]
section = ["Spells", "Hostile Juxtaposition"]
tags = ["conjuration", "teleportation"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Hostile Juxtaposition/Greater", path = "ultimate_combat/spell/hostile_juxtaposition_greater.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["teleportation"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a coin)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/4 levels" },
]
duration = "1 round/level or until discharged"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
School: conjuration (teleportation)
Level: 6: Summoner\
7: Arcanist, Sorcerer, Witch, Wizard
Casting Time: 1 standard action
Components: V, S, M (a coin)
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/4 levels
Duration: 1 round/level or until discharged
Saving Throw: Will negates
Spell Resistance: yes
:::

_You may target one creature for every four of your caster levels._

This spell functions like _[hostile juxtaposition](ref/spell/hostile-juxtaposition)_, except you can
target one creature for every four caster levels you have or you can target a single creature that
is larger than you are. You can switch places with each target only once while the effect lasts.
Once you have used it to teleport and switch places with each affected target, the spell is
discharged.
