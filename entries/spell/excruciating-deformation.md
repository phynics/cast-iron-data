+++
id = "ref/spell/excruciating-deformation"
kind = "spell"
title = "Excruciating Deformation"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "excruciating_deformation", path = "json/spells4.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "219"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
descriptors = ["evil", "pain"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Bloodrager, Psychic, Red Mantis Assassin, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level
Saving throw: Fortitude partial
Spell resistance: yes
Target: creature touched
Subschool: Polymorph
Descriptors: evil, pain
:::

Your touch attack causes your target to become painfully malformed. Its limbs twist and buckle,
while its body contorts uncontrollably, shifting and warping. Each round the target suffers
excruciating pain and takes 2d6 points of nonlethal damage, 1 point of Dexterity damage, and 1 point
of Constitution damage, and its speed is reduced by 10 feet. Once per round as a free action on its
turn, the target can attempt a new Fortitude saving throw to resist the spell for 1 round.
