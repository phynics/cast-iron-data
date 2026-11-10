+++
id = "ref/spell/impossible-angles"
kind = "spell"
title = "Impossible Angles"
aon = "SpellDisplay.aspx?ItemName=Impossible%20Angles"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "impossible_angles", path = "json/spells14.json" },
]
[[sources]]
publication = "horror-adventures"
page = "121"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a melted prism)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "contiguous area up to one 5-foot cube/caster level (S)" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Medium\
4: Mesmerist, Occultist\
5: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a melted prism)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Area: contiguous area up to one 5-foot cube/caster level (S)
Subschool: Figment
:::

You cause the surrounding area to appear to distort. The angles and corners of the area subtly twist
and contort, creating unnatural and impossible shapes. Any creature entering the area must succeed
at a Will save or become disoriented. Disoriented characters treat the area as difficult terrain and
are sickened. In addition, whenever a disoriented creature uses an action to move (including taking
a 5-foot step if it can do so in difficult terrain), roll 1d8 to see which direction it moves, in a
similar manner to determining where a splash weapon lands on a miss. On a 1, the creature moves in
its intended direction, with 2 through 8 rotating around the creature's starting square in a
clockwise direction. Only the creature's first 5 feet of movement each round are affected in this
way - it can move normally for any remaining movement, either from the same action or from later
actions, as the creature acclimatizes to the distortion. An affected creature can attempt a new Will
save each round to end the disoriented effect. A creature that leaves the area and re-enters must
attempt the saving throw again, even if it succeeded at its initial save.
