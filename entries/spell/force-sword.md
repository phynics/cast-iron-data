+++
id = "ref/spell/force-sword"
kind = "spell"
title = "Force Sword"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "force_sword", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "0 ft."
effects = [
  { label = "Effect", value = "one sword-shaped weapon of force" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Bloodrager, Magus, Occultist, Psychic, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 0 ft.
Duration: 1 minute/level
Saving throw: none
Spell resistance: yes
Effect: one sword-shaped weapon of force
Descriptors: force
:::

**Sources:** Arcane Anthology pg 8

You create a +1 longsword of pure force sized appropriately for you that you can wield or give to
another creature like any other longsword. At 8th level, the sword functions as a +2 longsword. At
13th level, it functions as a +3 longsword. A force sword cannot be attacked or harmed by physical
attacks, but [dispel magic](ref/spell/dispel-magic), [disintegrate](ref/spell/disintegrate), a
[sphere of annihilation](ref/magic-artifact/sphere-of-annihilation), or a
[rod of cancellation](ref/magic-rod/rod-of-cancellation) affects it.

If a creature you attack with the sword has [spell resistance](ref/rule/spell-resistance), you must
attempt a caster level check (1d20 + your caster level) against that spell resistance the first time
the force sword strikes it. If you fail the check, the spell is dispelled. If you succeed, the
weapon has its normal full effect on that creature for the duration of the spell.
