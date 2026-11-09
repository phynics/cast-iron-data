+++
id = "ref/spell/phase-door"
kind = "spell"
title = "Phase Door"
aon = "SpellDisplay.aspx?ItemName=Phase%20Door"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phase_door", path = "json/spells7.json" },
]
[[sources]]
publication = "core-rulebook"
page = "320"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V"
range = "touch"
effects = [
  { label = "Effect", value = "ethereal 5-ft.-by-8-ft. opening, 10 ft. deep + 5 ft. deep per three levels" },
]
duration = "one usage per two levels"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 7: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: touch
Duration: one usage per two levels
Saving throw: none
Spell resistance: no
Effect: ethereal 5-ft.-by-8-ft. opening, 10 ft. deep + 5 ft. deep per three levels
Subschool: Creation
:::

This spell creates an ethereal passage through wooden, plaster, or stone walls, but not other
materials. The phase door is invisible and inaccessible to all creatures except you, and only you
can use the passage. You disappear when you enter the phase door and appear when you exit. If you
desire, you can take one other creature (Medium or smaller) through the door. This counts as two
uses of the door. The door does not allow light, sound, or spell effects through it, nor can you see
through it without using it. Thus, the spell can provide an escape route, though certain creatures,
such as phase spiders, can follow with ease. A [gem of seeing](ref/magic-wondrous/gem-of-seeing) or
similar magic reveals the presence of a phase door but does not allow its use.

A phase door is subject to [dispel magic](ref/spell/dispel-magic). If anyone is within the passage
when it is dispelled, he is harmlessly ejected just as if he were inside a passwall effect.

You can allow other creatures to use the phase door by setting some triggering condition for the
door. Such conditions can be as simple or elaborate as you desire. They can be based on a creature's
name, identity, or alignment, but otherwise must be based on observable actions or qualities.
Intangibles such as level, class, HD, and hit points don't qualify.

Phase door can be made permanent with a [permanency](ref/spell/permanency) spell.
