+++
id = "ref/spell/umbral-strike"
kind = "spell"
title = "Umbral Strike"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "umbral_strike", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "necromancy"
subschools = ["Shadow"]
descriptors = ["darkness"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Druid", level = 7 },
  { class = "Inquisitor", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Spiritualist", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a black crossbow bolt)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "1 creature" },
]
duration = "1 round/level"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Inquisitor, Magus, Occultist, Spiritualist\
7: Arcanist, Cleric, Druid, Oracle, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a black crossbow bolt)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Fortitude partial
Spell resistance: yes
Target: 1 creature
Subschool: Shadow
Descriptors: darkness
:::

**Sources:** Blood of Shadows pg 16

You create a bolt of dark energy and use it to make a ranged touch attack that ignores
[concealment](ref/rule/concealment) (but not total concealment). If you hit, the target takes 1d6
points of damage per caster level (maximum 20d6). Half of this damage is cold damage and half of it
is negative energy. The bolt's shadow expands and covers the target, rendering him blind for the
duration of the spell. A successful Fortitude save halves the damage and negates the blind
condition.

**Note:** Normally, only [illusion](ref/spelldef/illusion) spells can be of the shadow subschool. No
errata has been issued, but this spell may have been intended to have the
[shadow descriptor](ref/spelldef/shadow-descriptor), like the spell
[umbral infusion](ref/spell/umbral-infusion) that was introduced in the same sourcebook.
