+++
id = "ref/spell/pesh-vigor"
kind = "spell"
title = "Pesh Vigor"
aon = "SpellDisplay.aspx?ItemName=Pesh%20Vigor"
source_ids = ["black-markets", "dark-markets-a-guide-to-katapesh"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pesh_vigor", path = "json/spells7.json" },
]
[[sources]]
publication = "black-markets"
page = "19"
[[sources]]
publication = "dark-markets-a-guide-to-katapesh"
page = "57"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a dose of pesh worth 15 gp)"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 round/level; see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Alchemist, Antipaladin, Arcanist, Bloodrager, Cleric, Druid, Hunter, Investigator, Magus, Oracle, Shaman, Sorcerer, Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M (a dose of pesh worth 15 gp)
Range: touch
Duration: 1 round/level; see text
Saving throw: Will negates
Spell resistance: yes
Target: living creature touched
:::

The target gains a +2 enhancement bonus to its Strength. Once per round as a free action, the target
can choose to increase the enhancement bonus by 2 for 1 round; if it does so, it takes 1d6 points of
nonlethal damage and the spell's duration decreases by 1 additional round. For every 5 caster levels
you have, the target can choose to increase the enhancement bonus by an additional 2, taking an
additional 1d6 points of nonlethal damage and decreasing the duration by 1 additional round per
increase to the Strength bonus, to a maximum enhancement bonus of +10 and 4d6 points of nonlethal
damage at caster level 15th. The subject can't spend more rounds than remain in the duration. When
the spell ends, the subject becomes fatigued.
