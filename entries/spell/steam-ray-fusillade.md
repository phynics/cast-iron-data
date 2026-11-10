+++
id = "ref/spell/steam-ray-fusillade"
kind = "spell"
title = "Steam Ray Fusillade"
aon = "SpellDisplay.aspx?ItemName=Steam%20Ray%20Fusillade"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "steam_ray_fusillade", path = "json/spells9.json" },
]
[[sources]]
publication = "aquatic-adventures"
page = "61"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire", "water"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a scraping from a hydrothermal vent)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a scraping from a hydrothermal vent)
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
Descriptors: fire, water
:::

For the duration of the spell, you can fire three rays of steam once per round as a standard action
(and you also fire three such rays as part of casting the spell). These rays function similarly to
the rays from [scorching ray](ref/spell/scorching-ray) (you can fire them at close range, they're
ranged touch attacks, they deal 4d6 points of fire damage each, and
[spell resistance](ref/rule/spell-resistance) negates them) except that they work both underwater
and above water without a caster level check for being a fire spell.
