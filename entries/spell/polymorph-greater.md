+++
id = "ref/spell/polymorph-greater"
kind = "spell"
title = "Greater Polymorph"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "polymorph_greater", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/polymorph" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of the creature whose form you choose)"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you choose)
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: living creature touched
Subschool: Polymorph
:::

**Sources:** PRPG Core Rulebook pg 324

This spell functions as [polymorph](ref/spell/polymorph) except that it allows the creature to take
on the form of a dragon or plant creature. If you use this spell to cause the target to take on the
form of an animal or magical beast, it functions as beast shape IV. If the form is that of an
elemental, the spell functions as elemental body III. If the form is that of a humanoid, the spell
functions as alter self. If the form is that of a plant, the spell functions as plant shape II. If
the form is that of a dragon, the spell functions as form of the dragon I. The subject may choose to
resume its normal form as a full-round action; doing so ends the spell.
