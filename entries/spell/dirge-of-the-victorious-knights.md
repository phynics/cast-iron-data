+++
id = "ref/spell/dirge-of-the-victorious-knights"
kind = "spell"
title = "Dirge of the Victorious Knights"
source_ids = ["adventurers-guide", "inner-sea-world-guide", "cheliax-empire-of-devils"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dirge_of_the_victorious_knights", path = "json/spells3.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "98"
[[sources]]
publication = "inner-sea-world-guide"
page = "294"
[[sources]]
publication = "cheliax-empire-of-devils"
page = "22"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
levels = [
  { class = "Bard", level = 6 },
  { class = "Skald", level = 6 },
]
casting_time = "1 round"
components = "V, S, F (a medal from a dead Hellknight or a copy a Chelish opera script, either worth at least 100 gp)"
range = "120 ft."
effects = [
  { label = "Area", value = "120-ft. line, 10 ft. wide" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 6: Bard, Skald
Casting time: 1 round
Components: V, S, F (a medal from a dead Hellknight or a copy a Chelish opera script, either worth at least 100 gp)
Range: 120 ft.
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: 120-ft. line, 10 ft. wide
Subschool: Shadow
:::

By performing part of the Chelish opera Victory of the [Hellknights](ref/rule/aff-lawknights), you
call forth spectral illusions of mounted Hellknights to trample your foes under the hooves of their
glorious steeds. The shadowy knights appear in an adjacent 10-foot square and ride forward in the
direction you indicate, dealing 1d6 points of damage per caster level (maximum 20d6) to all
creatures in their path. Half of this damage is cold damage, while half results directly from arcane
power and is not subject to cold resistance or immunity. The knights cannot pass through force
effects or barriers that block incorporeal creatures or undead.
