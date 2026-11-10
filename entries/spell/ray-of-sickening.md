+++
id = "ref/spell/ray-of-sickening"
kind = "spell"
title = "Ray of Sickening"
aon = "SpellDisplay.aspx?ItemName=Ray%20of%20Sickening"
source_ids = ["core-rulebook", "ultimate-magic", "dark-markets-a-guide-to-katapesh"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ray_of_sickening", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/ray-of-exhaustion" },
]
[[sources]]
publication = "ultimate-magic"
page = "234"
[[sources]]
publication = "dark-markets-a-guide-to-katapesh"
page = "57"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of sweat)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "ray" },
]
duration = "1 minute/level"
saving_throw = "Fortitude partial; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Arcanist, Bloodrager, Magus, Mesmerist, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of sweat)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Fortitude partial; see text
Spell resistance: yes
Effect: ray
:::

### Ray of Sickening

This spell functions as [ray of exhaustion](ref/spell/ray-of-exhaustion), except the target is
sickened if it fails its save and unaffected if it makes its save.
