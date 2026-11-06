+++
id = "ref/spell/phantom-blood"
kind = "spell"
title = "Phantom Blood"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phantom_blood", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Advanced Class Guide pg 190

You bolster your life energy. If the loss of hit points at the end of a temporary effect that
modifies your Constitution (such as barbarian's rage or bloodrager's bloodrage) would cause you to
become unconscious or kill you, you gain temporary hit points equal to your caster level (maximum
10). Each casting of this spell grants you temporary hit points only once.
