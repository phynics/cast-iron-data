+++
id = "ref/spell/unlock-flesh"
kind = "spell"
title = "Unlock Flesh"
source_ids = ["curse-of-the-crimson-throne"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unlock_flesh", path = "json/spells11.json" },
]
[[sources]]
publication = "curse-of-the-crimson-throne"
page = "453"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, F (any slashing weapon or cutting tool)"
range = "touch"
effects = [
  { label = "Area", value = "creature touched" },
]
duration = "1 round/level (living creature) or instantaneous (undead target); see below"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (any slashing weapon or cutting tool)
Range: touch
Duration: 1 round/level (living creature) or instantaneous (undead target); see below
Saving throw: Fortitude negates
Spell resistance: yes
Area: creature touched
:::

By touching a creature with a bladed instrument, you cause the creature's flesh to loosen and slide
against its skeletal moorings. A living creature touched becomes staggered by the disturbing and
uncomfortable sensation for 1 round per level. Each round on its turn, the subject can attempt a new
saving throw to end the effect. This is a standard action that does not provoke attacks of
opportunity. A corporeal undead creature targeted by this spell instead takes 1d6 points of damage
per caster level (maximum 5d6 at 5th level) as wet, oozing chunks of flesh slough off its desiccated
bones (a successful Fortitude save halves this damage). Incorporeal creatures, or creatures that do
not have flesh, are immune to this spell's effects.
