+++
id = "ref/spell/fleshwarping-swarm"
kind = "spell"
title = "Fleshwarping Swarm"
source_ids = ["inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fleshwarping_swarm", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-swarm" },
]
[[sources]]
publication = "inner-sea-races"
page = "220"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 round"
components = "V, S, M/DF (a square of red cloth)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one swarm of bats, rats, or spiders" },
]
duration = "concentration+ 2 rounds and 1 hour/level (see text)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Sorcerer, Summoner, Witch, Wizard
Casting time: 1 round
Components: V, S, M/DF (a square of red cloth)
Range: close (25 ft. + 5 ft./2 levels)
Duration: concentration+ 2 rounds and 1 hour/level (see text)
Saving throw: none
Spell resistance: no
Effect: one swarm of bats, rats, or spiders
Subschool: Summoning
:::

> _The following spell is available to the indicated race or ethnicity: [Drow](ref/race/drow)_

This spell functions as [summon swarm](ref/spell/summon-swarm), except that living and undead
creatures that fail their saving throw against the swarm's distraction find that their limbs twist
and spasm, as their bodies become susceptible to transmutations. Such creatures take a -4 penalty to
Dexterity and on saving throws against transmutation effects for 1 hour per caster level.
