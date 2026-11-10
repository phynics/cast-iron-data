+++
id = "ref/spell/insect-spies-greater"
kind = "spell"
title = "Greater Insect Spies"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "insect_spies_greater", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/insect-spies" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "217"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 6 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 round"
components = "V, S, M (a drop of honey)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "up to one insect spy/4 levels" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 6: Druid, Hunter, Summoner, Unchained Summoner\
7: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S, M (a drop of honey)
Range: close (25 ft. + 5 ft./2 levels)
Effect: up to one insect spy/4 levels
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
:::

### Greater Insect Spies

As [insect spies](ref/spell/insect-spies), but you can also borrow the senses of the summoned
insects. As a move action, you can choose to receive sensory input from one of the insects, seeing
what it sees and hearing what it hears. While doing so, you are treated as being blind and deaf. You
can change to another insect, or return to your own senses, with another move action.
