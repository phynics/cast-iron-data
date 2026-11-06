+++
id = "ref/spell/feeblemind"
kind = "spell"
title = "Feeblemind"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "feeblemind", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a handful of clay, crystal, or glass spheres)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Medium\
5: Arcanist, Mesmerist, Psychic, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a handful of clay, crystal, or glass spheres)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Will negates; see text
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 281

Target creature's Intelligence and Charisma scores each drop to 1. The affected creature is unable
to use Intelligence- or Charisma-based skills, cast spells, understand language, or communicate
coherently. Still, it knows who its friends are and can follow them and even protect them. The
subject remains in this state until a [heal](ref/spell/heal),
[limited wish](ref/spell/limited-wish), [miracle](ref/spell/miracle), or [wish](ref/spell/wish)
spell is used to cancel the effect of the feeblemind. A creature that can cast arcane spells, such
as a sorcerer or a wizard, takes a -4 penalty on its saving throw.
