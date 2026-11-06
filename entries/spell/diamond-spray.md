+++
id = "ref/spell/diamond-spray"
kind = "spell"
title = "Diamond Spray"
source_ids = ["pathfinder-24-the-final-wish"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "diamond_spray", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["earth"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a lump of coal)"
range = "20 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a lump of coal)
Range: 20 ft.
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: cone-shaped burst
Descriptors: earth
:::

**Sources:** Pathfinder \#24: The Final Wish pg 60

A cone of tiny, sparkling slivers as hard and sharp as filed diamonds springs from your outstretched
fingers at tremendous speed. Any creature in the area of the torrent takes 1d6 points of slashing
damage per caster level (maximum 10d6). These magical slivers are treated as adamantine and cold
iron for the purpose of overcoming [damage reduction](ref/rule/damage-reduction). In addition, this
spell bypasses up to 1 point of an object's [hardness](ref/umr/hardness) per 2 caster levels
(maximum 10).
