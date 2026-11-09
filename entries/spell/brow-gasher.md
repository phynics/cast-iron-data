+++
id = "ref/spell/brow-gasher"
kind = "spell"
title = "Brow Gasher"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "brow_gasher", path = "json/spells2.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "224"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Area", value = "one slashing melee weapon touched" },
]
duration = "1 round/level or until discharged"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Arcanist, Bloodrager, Hunter, Inquisitor, Magus, Occultist, Ranger, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level or until discharged
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Area: one slashing melee weapon touched
:::

You imbue a slashing melee weapon with the ability to deal a gruesome head wound. When the target
weapon hits a living creature, in addition to the normal effects of that hit, the wielder can
discharge this spell as a free action to open a gash on the target's forehead that deals bleed
damage equal to half your caster level. At the start of each of the target's turns, when it takes
bleed damage, it also takes a cumulative -1 penalty on all attack rolls. When that penalty reaches
-3, the target also treats all targets as having concealment (20% miss chance). When the penalty
reaches -5, the target is blinded. Stopping the bleed damage ends the effects this spell imposes on
the bleeding creature. A target that is immune to bleed damage is also immune to all this spell's
effects.
