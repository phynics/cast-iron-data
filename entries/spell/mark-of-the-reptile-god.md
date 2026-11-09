+++
id = "ref/spell/mark-of-the-reptile-god"
kind = "spell"
title = "Mark of the Reptile God"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mark_of_the_reptile_god", path = "json/spells6.json" },
]
[[sources]]
publication = "monster-codex"
page = "213"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Antipaladin, Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent
Saving throw: Fortitude negates
Spell resistance: yes
Target: one creature
Descriptors: curse
:::

If you succeed at a ranged touch attack, you burn your handprint onto the flesh of a creature,
dealing 1d6 points of acid damage. The mark can be placed on any exposed portion of the creature,
typically the head or forearm. The flesh around the handprint becomes rough and scaly, like the hide
of a lizard. It also glows with a green radiance (shedding light as a torch) when brought within 60
feet of you. While the handprint glows, the target takes a -2 penalty to AC against your attacks and
on saving throws to resist any spell you cast or [spell-like ability](ref/umr/spell-like-abilities)
you use.

Additionally, each day the target remains cursed, more and more of its flesh becomes covered in
reptilian scales. The target must succeed at a Fortitude save each day or take 1d4 points of
Charisma damage, 1 point of which is Charisma drain instead. A creature reduced to 0 Charisma by
this effect is immediately transformed into a small, harmless cave lizard, as the
[baleful polymorph](ref/spell/baleful-polymorph) spell.

As with the effects of bestow curse, the curse inflicted by this spell cannot be dispelled, but it
can be removed with a [break enchantment](ref/spell/break-enchantment),
[limited wish](ref/spell/limited-wish), [miracle](ref/spell/miracle),
[remove curse](ref/spell/remove-curse), or [wish](ref/spell/wish) spell.
