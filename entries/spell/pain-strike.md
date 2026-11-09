+++
id = "ref/spell/pain-strike"
kind = "spell"
title = "Pain Strike"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pain_strike", path = "json/spells7.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "234"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["evil", "pain"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Psychic\
3: Arcanist, Bloodrager, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
Target: one living creature
Descriptors: evil, pain
:::

Pain strike racks the targeted creature with agony, inflicting 1d6 points of nonlethal damage per
round for 1 round per level (maximum 10 rounds). Additionally, the affected creature is sickened for
the spell's duration, and the caster gains a +4 circumstance bonus on Intimidate checks against the
target.
