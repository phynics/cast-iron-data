+++
id = "ref/spell/life-pact"
kind = "spell"
title = "Life Pact"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "life_pact", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a drop of blood from each target)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one willing living creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Arcanist, Cleric, Oracle, Psychic, Shaman, Sorcerer, Spiritualist, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a drop of blood from each target)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes
Targets: one willing living creature/level, no two of which can be more than 30 ft. apart
:::

**Sources:** Advanced Class Guide pg 186

You bind the life forces of the targets into a mystical pact. If any target is reduced to fewer than
0 hit points, that target automatically triggers the power of the pact. The triggering target drains
1 hit point from all other targets who have at least 1 hit point and are within 30 feet of the
triggering target; these hit points are applied to the triggering target as magical healing. This
healing can prevent the triggering creature from dying, if the attack would cause the target's to
have an amount of negative hit points equal to its Constitution score. This healing cannot raise the
triggering creature above 1 hit point; any excess hit points drained from other targets are wasted.

The pact can be triggered once per round. It's not triggered by death effects or effects that do not
deal hit point damage.
