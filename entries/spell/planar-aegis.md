+++
id = "ref/spell/planar-aegis"
kind = "spell"
title = "Planar Aegis"
aon = "SpellDisplay.aspx?ItemName=Planar%20Aegis"
source_ids = ["plane-hoppers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planar_aegis", path = "json/spells7.json" },
]
[[sources]]
publication = "plane-hoppers-handbook"
page = "12"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 3 },
  { class = "Occultist", level = 4 },
  { class = "Ranger", level = 3 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a fistful of naturally occuring material from a plane)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Hunter, Ranger\
4: Occultist, Summoner, Unchained Summoner\
5: Arcanist, Druid, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a fistful of naturally occuring material from a plane)
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

You draw motes of essence from material native to a plane that has elemental or energy essence
traits, weaving the essence together into a shield of force. Choose an essence trait from the list
below; the material component for this spell must come from a plane that has the essence trait you
chose. Each essence trait has an associated damage type (see the table below). Any creature that
hits you with a non-reach melee weapon, natural weapon, or unarmed attack takes 3d6 points of damage
plus 1 point per caster level you have (maximum +20) of a type corresponding to the essence trait
you chose. In addition, you take only half damage from attacks or effects of the associated damage
type, and if such an attack or effect allows a saving throw for half damage, you take no damage on a
successful saving throw.

|Essence Trait|Damage Type|
| --- | --- |
|Air-Dominant|Electricity|
|Earth-Dominant|Acid|
|Fire-Dominant|Fire|
|Positive-Dominant|Positive|
|Negative-Dominant|Negative|
|Water-Dominant|Cold|
