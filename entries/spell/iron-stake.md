+++
id = "ref/spell/iron-stake"
kind = "spell"
title = "Iron Stake"
source_ids = ["ultimate-wilderness", "the-first-world-realm-of-the-fey"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "iron_stake", path = "json/spells6.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "231"
[[sources]]
publication = "the-first-world-realm-of-the-fey"
page = "12"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Ranger", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of iron filings)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "see text" },
]
duration = "instantaneous or 1 round/level; see text"
saving_throw = "Fortitude partial"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Hunter, Inquisitor, Ranger\
3: Arcanist, Cleric, Druid, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a pinch of iron filings)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous or 1 round/level; see text
Saving throw: Fortitude partial
Spell resistance: no
Effect: see text
Subschool: Creation
:::

This spell creates a 1-foot-long spike of cold iron that you fling at your target as a ranged touch
attack. The stake is treated as a magic and cold iron weapon for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction), and deals 1d6 points of piercing damage for every 2
caster levels you have (maximum 10d6 at 20th level).

Additionally, if a creature with DR/cold iron takes damage from this spell, it is sickened for 1
round and must attempt a Fortitude save. If it fails, for a number of rounds equal to your caster
level, it must succeed at a [concentration](ref/rule/concentration) check (in addition to any
normally required concentration checks) to use any spells or
[spell-like abilities](ref/umr/spell-like-abilities) it has - the DC of this check is equal to 15 +
twice the spell's level. If the creature fails this concentration check, its spell is wasted.
