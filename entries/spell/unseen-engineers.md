+++
id = "ref/spell/unseen-engineers"
kind = "spell"
title = "Unseen Engineers"
aon = "SpellDisplay.aspx?ItemName=Unseen%20Engineers"
source_ids = ["kobolds-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unseen_engineers", path = "json/spells11.json" },
]
[[sources]]
publication = "kobolds-of-golarion"
page = "27"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (materials required to construct the trap)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Effect", value = "a team of tiny, invisible engineers" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Summoner, Unchained Summoner\
3: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (materials required to construct the trap)
Range: long (400 ft. + 40 ft./level)
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Effect: a team of tiny, invisible engineers
Subschool: Creation
:::

You conjure an invisible team of tiny engineers to construct a trap at alarming speed. Originating
at your location, the team must remain within range of you or the spell ends. The engineers
construct a mechanical trap of your choice. Construction takes a number of rounds equal to the
trap's challenge rating. The engineers must have the materials available. At the end of the
construction time, use your Craft (traps) skill with a +5 bonus to determine the success of their
work. If the engineers succeed, the trap is complete and the spell ends. If they fail, the materials
are deposited at that location and the spell ends. If the spell's duration ends before the trap is
complete, the engineers automatically fail.

The engineers move at your base speed and can carry only materials required in the construction of
the desired trap. They can't attack in any way or be killed, and dissipate if they take 12 points of
damage from area attacks (they get no saves against attacks).
