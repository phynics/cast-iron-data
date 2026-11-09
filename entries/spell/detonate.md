+++
id = "ref/spell/detonate"
kind = "spell"
title = "Detonate"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detonate", path = "json/spells3.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "215"

[fields]
kind = "spell"
school = "evocation [acid, cold, electricity, or fire]"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (two vials; one containing acid and one containing an alkaline solution worth a total of 50 gp)"
range = "30 ft."
effects = [
  { label = "Area", value = "30-ft.-radius spread centered on you" },
]
duration = "1 round, then instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation \[acid, cold, electricity, or fire\]
Level: 4: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (two vials; one containing acid and one containing an alkaline solution worth a total of 50 gp)
Range: 30 ft.
Duration: 1 round, then instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: 30-ft.-radius spread centered on you
:::

You flood yourself with a potent surge of elemental energy. One round after completing the casting
of the spell, the energy explodes from your body.

When this spell creates the explosion of energy, choose one of the following four energy types:
acid, cold, electricity, or fire. The explosion inflicts 1d8 points of damage of that energy type
per caster level (maximum 10d8) to all creatures and unattended objects within 15 feet, and half
that amount to targets past 15 feet but within 30 feet. You automatically take half damage from the
explosion, without a saving throw, but any other energy resistance or energy immunity effects you
may have in place can prevent or lessen this overflow damage caused by the explosion.
