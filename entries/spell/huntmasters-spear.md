+++
id = "ref/spell/huntmasters-spear"
kind = "spell"
title = "Huntmaster's Spear"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "huntmasters_spear", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Bloodrager", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Paladin", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 2 },
]
casting_time = "10 minutes"
components = "V, S, M/DF (see text)"
range = "touch"
effects = [
  { label = "Target", value = "nonmagical spear touched" },
]
duration = "24 hours or until discharged"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Antipaladin, Hunter, Paladin, Ranger\
2: Bloodrager, Druid, Inquisitor, Magus, Occultist, Shaman
Casting time: 10 minutes
Components: V, S, M/DF (see text)
Range: touch
Duration: 24 hours or until discharged
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: nonmagical spear touched
:::

**Sources:** Monster Hunter's Handbook pg 30

Choose one creature type (and subtype, if applicable) from the ranger's
[favored enemy](ref/ability/favored-enemy) list. When you cast this spell, the targeted spear hums
with destructive energy and functions as a +1 spear against creatures of the selected type.

You can discharge this spell in order to make an especially powerful attack with the spear. The
spear's critical range becomes 18-20 and its critical multiplier becomes ×3. If you make this attack
as part of a charge action, you gain an enhancement bonus of +30 feet to your base speed while
performing the charge. If you throw the spear as part of this attack, its range increment increases
to 80 feet. If you cast this spell on a masterwork spear, it also gains the bane special ability
against the selected creature type and automatically bypasses any
[damage reduction](ref/rule/damage-reduction) (except DR/-) regardless of the creature's type. After
resolving the attack, the spear is completely destroyed in a burst of energy.

Any creature other than you treats the spear as a normal weapon of its type. You can have only one
huntmaster's spear in effect at a time. If you cast the spell again, any previous instance of the
spell immediately ends. If you expend a monster trophy of the type selected as an optional material
component for this spell, you reduce the casting time to 1 round.
