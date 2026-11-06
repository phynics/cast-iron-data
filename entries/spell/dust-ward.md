+++
id = "ref/spell/dust-ward"
kind = "spell"
title = "Dust Ward"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dust_ward", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "10 minutes"
components = "V, S, M (a pinch of pumice)"
range = "touch"
effects = [
  { label = "Target", value = "one magic item" },
]
duration = "permanent"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 6: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (a pinch of pumice)
Range: touch
Duration: permanent
Saving throw: none
Spell resistance: no
Target: one magic item
:::

**Sources:** Monster Codex pg 45

You ward a magic item against other creatures who try to learn to use or copy it. When you cast the
spell, you designate one creature type, subtype, or a specific individual. If the item is worn or
carried for 1 continuous hour or more by a creature that doesn't match the designation, the dust
ward disintegrates the item into worthless gray dust. This destruction also occurs if the creature
attempts to study the item in order to learn its properties or how to magically craft it (a miracle
or wish spell used on the gray dust can still reveal this information). The destruction of the item
doesn't harm the creature wearing or carrying the item (although the item's destruction may put the
creature in harm's way, such as if a magical rope were being used to cross a chasm at the time). If
the offending creature wears or carries the item for less than 1 hour and passes it to a different
creature, the countdown to the item's destruction starts over.

The spell cannot affect a magic item with a caster level greater than half your caster level.
