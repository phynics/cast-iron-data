+++
id = "ref/spell/elemental-touch"
kind = "spell"
title = "Elemental Touch"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elemental_touch", path = "json/spells4.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "218"

[fields]
kind = "spell"
school = "evocation [acid, cold, electricity, or fire]"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a bit of the chosen element: earth, water, air, or fire)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation \[acid, cold, electricity, or fire\]
Level: 2: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a bit of the chosen element: earth, water, air, or fire)
Range: personal
Duration: 1 round/level (D)
Saving throw: see text
Spell resistance: no
Target: you
:::

Upon completing the casting of this spell, elemental energy infuses your hands. Choose an energy
type: acid, cold, electricity, or fire. You gain a melee touch attack causing 1d6 points of damage
of that energy type, along with a special effect described below. You also deal energy damage and
the related special effect when you attack with your hands using an unarmed strike, a single claw,
or a single slam attack. This bonus damage can never apply to multiple weapons.

_Acid:_ Your touch attack causes 1 point of ongoing acid damage per round for 1 round per three
caster levels. The target must make a Fortitude save or be sickened for the duration of the ongoing
acid damage.

_Cold:_ The target must make a Fortitude save or be fatigued. A creature that is already fatigued
suffers no additional effect.

_Electricity:_ The target must make a Fortitude save or be staggered for 1 round.

_Fire:_ Your hands ignite and shed light as a torch. Your touch may cause targets to catch on fire.

Subsequent attacks inflict the normal damage, but the additional effects do not stack. This spell
grants no special protection to anything held in or worn on your hands. When you cast this spell to
deal acid, cold, electricity, or fire damage, it is a spell of that type.
