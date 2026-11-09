+++
id = "ref/spell/invisibility-bubble-mass"
kind = "spell"
title = "Mass Invisibility Bubble"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invisibility_bubble_mass", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/invisibility-bubble" },
]
[[sources]]
publication = "aquatic-adventures"
page = "60"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 6 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (needle from a sea urchin)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "any number of creatures, no two of which can be more than 180 ft. apart" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 6: Mesmerist, Summoner, Unchained Summoner\
7: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (needle from a sea urchin)
Range: long (400 ft. + 40 ft./level)
Target: any number of creatures, no two of which can be more than 180 ft. apart
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Subschool: Glamer
Descriptors: glamer
:::

### Mass Invisibility Bubble

This functions as per [invisibility bubble](ref/spell/invisibility-bubble), but the spell affects
the areas of each target creature, regardless of the creature's size. The effect moves with the
group and is broken when anyone in the group attacks. Individuals in separate bubbles can't see each
other. The spell is broken for any individual who moves more than 180 feet from the nearest member
of the group. If only two individuals are affected, the one moving away from the other one loses its
invisibility. If both are moving away from each other simultaneously, they both become visible when
the distance between them exceeds 180 feet.
