+++
id = "ref/spell/false-life-greater"
kind = "spell"
title = "Greater False Life"
source_ids = ["core-rulebook", "mythic-adventures", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "false_life_greater", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/false-life" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of blood)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level or until discharged; see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Medium, Mesmerist\
4: Alchemist, Arcanist, Bloodrager, Investigator, Occultist, Psychic, Shaman, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of blood)
Range: personal
Target: you
Duration: 1 hour/level or until discharged; see text
Saving throw: none
Spell resistance: no
:::

### Mythic False Life

**Sources:** Mythic Adventures pg 93

The temporary hit points gained increase to 2d8 + 2 per caster level (maximum +20). As an immediate
action, you can dismiss the remaining duration of the spell to prevent 1 point of Strength,
Dexterity, or Constitution damage per 10 temporary hit points remaining from the spell. This takes
effect after the attack hits you and the damage is rolled, but before you take the damage. For
example, if you have 22 temporary hit points from mythic false life and a wyvern stings you for 3
points of Constitution damage, you can dismiss the spell to prevent 2 points of Constitution damage
from that attack.

### Greater False Life

**Sources:** Ultimate Magic pg 219

This spell functions as [false life](ref/spell/false-life), except you gain temporary hit points
equal to 2d10 + 1 point per caster level (maximum +20). The effects of this spell do not stack with
those of false life.
