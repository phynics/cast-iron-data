+++
id = "ref/spell/touch-of-idiocy"
kind = "spell"
title = "Touch of Idiocy"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "touch_of_idiocy", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Arcanist, Bloodrager, Medium, Mesmerist, Psychic, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 10 minutes/level
Saving throw: none
Spell resistance: yes
Target: living creature touched
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 360

With a touch, you reduce the target's mental faculties. Your successful melee touch attack applies a
1d6 penalty to the target's Intelligence, Wisdom, and Charisma scores. This penalty can't reduce any
of these scores below 1.

This spell's effect may make it impossible for the target to cast some or all of its spells, if the
requisite ability score drops below the minimum required to cast spells of that level.
