+++
id = "ref/spell/particulate-form"
kind = "spell"
title = "Particulate Form"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "particulate_form", path = "json/spells7.json" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "6"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Occultist", level = 5 },
  { class = "Oracle", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of fine sand)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "1 creature/level, no two of which can be more than 30 feet apart" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Occultist\
7: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a pinch of fine sand)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Targets: 1 creature/level, no two of which can be more than 30 feet apart
:::

The targets' physical forms undergo a bizarre transformation. They look and function normally, but
are composed of countless particles that separate and reconnect to remain whole. Each target gains
[fast healing](ref/umr/fast-healing) 1 and is immune to bleed damage, critical hits, sneak attacks,
and other forms of precision damage. The value of this fast healing increases by 1 at caster levels
10th, 15th, and 20th. Any target can end the spell effect on itself as a swift action; the target
then regains 5d6 hit points and can attempt an additional saving throw against any one disease or
poison affecting it (at the original save DC), ending that disease or poison with a successful
saving throw.
