+++
id = "ref/spell/ablative-sphere"
kind = "spell"
title = "Ablative Sphere"
source_ids = ["humans-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ablative_sphere", path = "json/spells.json" },
]
[[sources]]
publication = "humans-of-golarion"
page = "28"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a crystalline sphere worth 10 gp)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a crystalline sphere worth 10 gp)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

The Garundi tenaciously protect their homes, and through the years they have perfected magic to aid
them in their defense. An immobile, crystalline, web-like globe surrounds you.

When the ablative sphere winks into existence, it provides you with improved cover. The barrier does
not impede a spell's line of sight or effect.

The sphere is 1 inch thick per caster level, has [hardness](ref/umr/hardness) 5, and 3 hit points
per inch of thickness. When an ablative sphere loses hit points, the level of cover it provides is
reduced. When the ablative sphere has lost one-third of its hit points, it provides cover instead of
improved cover. Once it has lost two-thirds of its hit points, it provides only partial cover.
Finally, when the ablative sphere's hit points reach 0, the globe is destroyed. When an attack
reduces an ablative sphere's hit points to 0, you take any remaining damage.
