+++
id = "ref/spell/shrink-item"
kind = "spell"
title = "Shrink Item"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shrink_item", path = "json/spells9.json" },
]
[[sources]]
publication = "core-rulebook"
page = "342"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one touched object of up to 2 cu. ft./level" },
]
duration = "1 day/level; see text"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Occultist, Psychic, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 day/level; see text
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: one touched object of up to 2 cu. ft./level
:::

You are able to shrink one nonmagical item (if it is within the size limit) to 1/16 of its normal
size in each dimension (to about 1/4,000 the original volume and mass). This change effectively
reduces the object's size by four categories. Optionally, you can also change its now shrunken
composition to a cloth-like one. Objects changed by a shrink item spell can be returned to normal
composition and size merely by tossing them onto any solid surface or by a word of command from the
original caster. Even a burning fire and its fuel can be shrunk by this spell. Restoring the
shrunken object to its normal size and composition ends the spell.

Shrink item can be made permanent with a [permanency](ref/spell/permanency) spell, in which case the
affected object can be shrunk and expanded an indefinite number of times, but only by the original
caster.
