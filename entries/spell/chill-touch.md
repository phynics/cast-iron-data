+++
id = "ref/spell/chill-touch"
kind = "spell"
title = "Chill Touch"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chill_touch", path = "json/spells2.json" },
]
[[sources]]
publication = "core-rulebook"
page = "255"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Targets", value = "creature or creatures touched (up to one/level)" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial or Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Arcanist, Bloodrager, Magus, Shaman, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Fortitude partial or Will negates; see text
Spell resistance: yes
Targets: creature or creatures touched (up to one/level)
:::

A touch from your hand, which glows with blue energy, disrupts the life force of living creatures.
Each touch channels negative energy that deals 1d6 points of damage. The touched creature also takes
1 point of Strength damage unless it makes a successful Fortitude saving throw. You can use this
melee touch attack up to one time per level.

An undead creature you touch takes no damage of either sort, but it must make a successful Will
saving throw or flee as if panicked for 1d4 rounds + 1 round per caster level.
