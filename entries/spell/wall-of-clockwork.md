+++
id = "ref/spell/wall-of-clockwork"
kind = "spell"
title = "Wall of Clockwork"
aon = "SpellDisplay.aspx?ItemName=Wall%20of%20Clockwork"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wall_of_clockwork", path = "json/spells11.json" },
]
[[sources]]
publication = "heroes-of-the-streets"
page = "23"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "wall of bronze clockworks whose area is up to one 5-ft.-square/level (S)" },
]
duration = "1 minute/level"
saving_throw = "Reflex half or Reflex negates, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level
Saving throw: Reflex half or Reflex negates, see text
Spell resistance: yes
Effect: wall of bronze clockworks whose area is up to one 5-ft.-square/level (S)
Subschool: Creation
:::

An immobile, vertical wall of spinning cogs and gears springs into existence. Any creature passing
through the wall takes 1d6 points of piercing and slashing damage per 2 caster levels (maximum
10d6); a successful Reflex save halves the damage.

The wall cannot be conjured so that it occupies the same space as a creature or another object. It
must always be a flat plane, though you can shape its edges to fit the available space.

A wall of clockwork provides cover (+4 bonus to AC, +2 bonus on Reflex saves) against attacks made
through it.

A wall of clockwork is 1 inch thick per 4 caster levels. You can double the wall's area by halving
its thickness. Each 5-foot square of the wall has 30 hit points per inch of thickness and
[hardness](ref/umr/hardness) 9. A section of wall whose hit points drop to 0 is breached. If a
creature tries to break through the wall with a single attack, the DC for the Strength check is 25 +
2 per inch of thickness. If an attacker an attack roll of a natural 20 (and only a natural 20,
regardless of the weapon's threat range) and confirms the critical hit (even though the wall is
otherwise immune to critical hits), that section of wall gains the broken condition. If already
broken, that section of wall is destroyed instead.

Bronze created by this spell is not suitable for use in the creation of other objects (even for the
limited duration of the spell) and cannot be sold.
