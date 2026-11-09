+++
id = "ref/spell/ghoul-touch"
kind = "spell"
title = "Ghoul Touch"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ghoul_touch", path = "json/spells13.json" },
]
[[sources]]
publication = "core-rulebook"
page = "289"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["poison"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (cloth from a ghoul or earth from a ghoul's lair)"
range = "touch"
effects = [
  { label = "Target", value = "living humanoid touched" },
]
duration = "1d6+2 rounds"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Arcanist, Bloodrager, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S, M (cloth from a ghoul or earth from a ghoul's lair)
Range: touch
Duration: 1d6+2 rounds
Saving throw: Fortitude negates
Spell resistance: yes
Target: living humanoid touched
Descriptors: poison
:::

Imbuing you with negative energy, this spell allows you to paralyze a single living humanoid for the
duration of the spell with a successful melee touch attack.

A paralyzed subject exudes a carrion stench that causes all living creatures (except you) in a
10-foot-radius spread to become sickened (Fortitude negates). A neutralize poison spell removes the
effect from a sickened creature, and creatures immune to poison are unaffected by the stench. This
is a poison effect.
