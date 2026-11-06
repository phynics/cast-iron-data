+++
id = "ref/spell/irregular-size"
kind = "spell"
title = "Irregular Size"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "irregular_size", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Medium\
3: Antipaladin, Cleric, Mesmerist, Occultist, Oracle, Shaman, Warpriest, Witch\
4: Arcanist, Bloodrager, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: permanent
Saving throw: Fortitude negates
Spell resistance: yes
Target: creature touched
Descriptors: curse
:::

**Sources:** Magic Tactics Toolbox pg 21

You curse a creature so one set of its limbs (typically its arms, legs, or wings) shrivels in size.

_Arms:_ The creature counts as one size category smaller for the purpose of determining the size of
weapon it can wield. If the creature is capable of making natural attacks with its arms, the damage
dealt by those attacks decreases as though the target were one size category smaller than its actual
size.

_Legs:_ The creature's base speed decreases by 10 feet (to a minimum of 5 feet) and its Strength
score counts as 4 lower for the purpose of determining its carrying capacity.

_Wings:_ The creature's Fly speed decreases by 10 feet (to a minimum of 5 feet), the damage dealt by
any wing attacks decreases as though the target were one size category smaller than its actual size,
and its fly maneuverability decreases by a step (to a minimum of clumsy).
