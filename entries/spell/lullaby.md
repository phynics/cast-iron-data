+++
id = "ref/spell/lullaby"
kind = "spell"
title = "Lullaby"
aon = "SpellDisplay.aspx?ItemName=Lullaby"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lullaby", path = "json/spells6.json" },
]
[[sources]]
publication = "core-rulebook"
page = "305"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 0 },
  { class = "Mesmerist", level = 0 },
  { class = "Psychic", level = 0 },
  { class = "Skald", level = 0 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "living creatures within a 10-ft.-radius burst" },
]
duration = "concentration+ 1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 0: Bard, Mesmerist, Psychic, Skald
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: concentration+ 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Area: living creatures within a 10-ft.-radius burst
Subschool: Compulsion
Descriptors: mind-affecting
:::

Any creature within the area that fails a Will save becomes drowsy and inattentive, taking a -5
penalty on Perception checks and a -2 penalty on Will saves against sleep effects while the lullaby
is in effect. Lullaby lasts for as long as the caster concentrates, plus up to 1 round per caster
level thereafter.
