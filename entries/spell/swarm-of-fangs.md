+++
id = "ref/spell/swarm-of-fangs"
kind = "spell"
title = "Swarm of Fangs"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "swarm_of_fangs", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 round"
components = "V, S, M (a lizard's tooth)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one swarm of animate teeth" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Druid, Hunter, Psychic, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 round
Components: V, S, M (a lizard's tooth)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Effect: one swarm of animate teeth
Subschool: Summoning
:::

**Sources:** Monster Codex pg 213

You summon a swarm consisting of thousands of animate, flying teeth in a 10-foot-by-10-foot cube.
These fangs attack all creatures within the swarm's area. You can summon the swarm so that it shares
an area with other creatures, and you can move the swarm up to 40 feet each round as a move action.
If you choose not to move the swarm, it automatically moves up to 40 feet to envelop the nearest
creature (including you) if it has not already done so.

Creatures caught inside the swarm's area of effect take 2d6 points of damage. The fangs deal damage
to all creatures sharing their area when they first appear, and at the end of their movement each
round.
