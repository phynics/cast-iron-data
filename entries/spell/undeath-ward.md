+++
id = "ref/spell/undeath-ward"
kind = "spell"
title = "Undeath Ward"
source_ids = ["dungeons-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "undeath_ward", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (powdered silver)"
range = "10 ft."
effects = [
  { label = "Area", value = "10-ft.-radius emanantion, centered on you" },
]
duration = "1 minute/level (D)"
saving_throw = "none or Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Inquisitor\
5: Cleric, Oracle, Warpriest\
6: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (powdered silver)
Range: 10 ft.
Duration: 1 minute/level (D)
Saving throw: none or Will negates (see text)
Spell resistance: yes
Area: 10-ft.-radius emanantion, centered on you
:::

**Sources:** Dungeons of Golarion pg 63

You create a pale silver barrier that repels undead. Mindless undead and intelligent undead with
fewer Hit Dice than your caster level cannot enter the area or penetrate the barrier. Undead of Hit
Dice equal to or greater than your caster level can pass through this barrier by making a successful
Will save against the spell, but as they do so, they take 3d6 points of damage. Once an undead
creature makes its save against this spell and takes this damage, it can come and go without further
penalty. This spell may only be used defensively, not aggressively. Forcing an undeath ward against
creatures that the spell keeps at bay collapses the barrier.
