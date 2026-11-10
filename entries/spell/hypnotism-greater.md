+++
id = "ref/spell/hypnotism-greater"
kind = "spell"
title = "Greater Hypnotism"
aon = "SpellDisplay.aspx?ItemName=Hypnotism%2C%20Greater"
source_ids = ["core-rulebook", "blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hypnotism_greater", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/hypnotism" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "19"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "1 round"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "several living creatures, no two of which may be more than 30 ft. apart" },
]
duration = "2d4 rounds (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Arcanist, Bard, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Witch
Casting time: 1 round
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Area: several living creatures, no two of which may be more than 30 ft. apart
Duration: 2d4 rounds (D)
Saving throw: Will negates
Spell resistance: yes
Subschool: Compulsion
Descriptors: mind-affecting
:::

### Greater Hypnotism

> _The following spell is the result of generations of [nagaji](ref/race/nagaji) tradition, but
> spellcasters from elsewhere in Tian Xia have begun to learn these techniques and spread them
> further._

This functions as [hypnotism](ref/spell/hypnotism), except it affects 2 Hit Die of creatures per
caster level you have. You can make up to five requests (instead of a single request) to each
creature affected by the spell, and the requests can be as long and as complicated as you desire
(though they still must be reasonable).
