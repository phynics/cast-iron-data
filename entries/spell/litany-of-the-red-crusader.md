+++
id = "ref/spell/litany-of-the-red-crusader"
kind = "spell"
title = "Litany of the Red Crusader"
aon = "SpellDisplay.aspx?ItemName=Litany%20of%20the%20Red%20Crusader"
source_ids = ["pathfinder-140-eulogy-for-roslars-coffer"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "litany_of_the_red_crusader", path = "json/spells6.json" },
]
[[sources]]
publication = "pathfinder-140-eulogy-for-roslars-coffer"
page = "72"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Inquisitor", level = 2 },
  { class = "Paladin", level = 1 },
]
casting_time = "1 swift action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Antipaladin, Paladin\
2: Inquisitor
Casting time: 1 swift action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round
Saving throw: Fortitude negates
Spell resistance: yes
Target: one creature
:::

Followers of [Arazni](ref/faith/arazni) have made use of this litany since her days as a crusader
and herald. Each time the target creature takes piercing or slashing damage, it takes 1 point of
bleed damage; this bleed damage stacks with itself. While subject to this spell, the target cannot
be the target of another spell that has the word "litany" in the title.
