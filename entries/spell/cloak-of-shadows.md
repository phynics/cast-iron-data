+++
id = "ref/spell/cloak-of-shadows"
kind = "spell"
title = "Cloak of Shadows"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cloak_of_shadows", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["evil", "shadow"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Antipaladin\
5: Arcanist, Bard, Mesmerist, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Shadow
Descriptors: evil, shadow
:::

**Sources:** Villain Codex pg 80

You wrap yourself in a protective mantle of semi-real shadow. This grants a number of advantages:
you gain concealment (20% miss chance), a +5 competence bonus on Stealth checks, and DR 5/good. This
shroud of shadows also protects you from direct sunlight, negating sunlight vulnerability, sunlight
powerlessness, and similar effects.

When you are in dim light or darkness, the first two benefits increase against foes that don't have
[darkvision](ref/rule/darkvision) or the see in darkness ability. Such creatures suffer a 50% miss
chance (though you don't gain total concealment) and your competence bonus on Stealth checks
increases to +10 with respect to such creatures.
