+++
id = "ref/spell/stone-shape"
kind = "spell"
title = "Stone Shape"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stone_shape", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["earth"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (soft clay)"
range = "touch"
effects = [
  { label = "Target", value = "stone or stone object touched, up to 10 cu. ft. + 1 cu. ft./level" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Cleric, Druid, Hunter, Occultist, Oracle, Shaman, Warpriest\
4: Arcanist, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (soft clay)
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: stone or stone object touched, up to 10 cu. ft. + 1 cu. ft./level
Descriptors: earth
:::

**Sources:** PRPG Core Rulebook pg 349

You can form an existing piece of stone into any shape that suits your purpose. While it's possible
to make crude coffers, doors, and so forth with stone shape, fine detail isn't possible. There is a
30% chance that any shape including moving parts simply doesn't work.

### Mythic Stone Shape

**Sources:** Mythic Adventures pg 109\
The duration changes to 1 round/level and instantaneous (see text). Each round after the round you
cast the spell, you can spend a standard action to shape up to 5 additional cubic feet of stone you
touch. Shaped stone has an instantaneous duration (meaning it does not revert to its previous form
when the spell ends).
