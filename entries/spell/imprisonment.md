+++
id = "ref/spell/imprisonment"
kind = "spell"
title = "Imprisonment"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "imprisonment", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "300"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 9: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will negates; see text
Spell resistance: yes
Target: creature touched
:::

When you cast imprisonment and touch a creature, it is entombed in a state of suspended animation
(see the [temporal stasis](ref/spell/temporal-stasis) spell) in a small sphere far beneath the
surface of the ground. The subject remains there unless a freedom spell is cast at the locale where
the imprisonment took place. Magical search by a crystal ball, a locate object spell, or some other
similar divination does not reveal the fact that a creature is imprisoned, but discern location
does. A wish or miracle spell will not free the recipient, but will reveal where it is entombed. If
you know the target's name and some facts about its life, the target takes a -4 penalty on its save.
