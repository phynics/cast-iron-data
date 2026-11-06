+++
id = "ref/spell/shadow-dragon-aspect"
kind = "spell"
title = "Shadow Dragon Aspect"
source_ids = ["kobolds-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_dragon_aspect", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "Will disbelief (if interacted with), see text"
spell_resistance = "yes, see text"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Arcanist, Bard, Red Mantis Assassin, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level
Saving throw: Will disbelief (if interacted with), see text
Spell resistance: yes, see text
Target: you
Subschool: Shadow
Descriptors: shadow
:::

**Sources:** Kobolds of Golarion pg 27

You wreathe yourself in the quasi-real form of a dragon. You gain two claw attacks (1d6 plus caster
level slashing damage) and a bite attack (1d8 plus caster level piercing damage). These are primary
attacks. In addition, you gain shadowy wings, granting you a fly speed equal to your base speed
(good maneuverability). Your shadowy natural weapons are only half as strong as the real things,
though creatures that believe them to be real are affected at full strength. A creature is permitted
one Will save the first time you strike it. If it succeeds, the creature takes half damage from such
attacks for the duration of the spell. If you overcome a creature's
[spell resistance](ref/rule/spell-resistance) on your first attack, that creature remains vulnerable
for the spell's duration; otherwise, it's immune.
