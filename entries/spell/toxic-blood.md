+++
id = "ref/spell/toxic-blood"
kind = "spell"
title = "Toxic Blood"
source_ids = ["potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "toxic_blood", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["poison"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (vial of black adder venom)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Arcanist, Bloodrager, Cleric, Druid, Hunter, Investigator, Magus, Oracle, Ranger, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (vial of black adder venom)
Range: touch
Duration: 1 minute/level
Saving throw: Fortitude negates; see text
Spell resistance: no
Target: creature touched
Descriptors: poison
:::

**Sources:** Potions and Poisons pg 11

The target creature's blood becomes poisonous. Anytime the target takes piercing or slashing damage,
a spray of acidic blood spurts from its body in the direction of the opponent who inflicted the
wound. This blood travels in a 10-foot line, striking the first creature or object it touches. A
creature struck by the blood is exposed to black adder venom and must save against the poison as
normal, with a DC equal to the spell's DC.

Toxic blood can be made permanent with a [permanency](ref/spell/permanency) spell cast by a caster
of 11th level or higher, at a cost of 7,500 gp.
