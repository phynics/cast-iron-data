+++
id = "ref/spell/crime-wave"
kind = "spell"
title = "Crime Wave"
aon = "SpellDisplay.aspx?ItemName=Crime%20Wave"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "crime_wave", path = "json/spells3.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "208"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a tarnished coin)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Antipaladin\
5: Bard, Mesmerist\
7: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a tarnished coin)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature/level, no two of which can be more than 30 ft. apart
Subschool: Compulsion
Descriptors: mind-affecting
:::

You instill overwhelming avarice in the targets and impel them toward a wild spree of larceny.
Creatures affected by a crime wave must roll percentile dice each round to determine what action
they take.

|d%|Behavior|
| --- | --- |
|01-25|Act normally, but with suspicion toward others. The target doesn't benefit from or provide benefits with teamwork feats and the aid another action. If a creature attempts to use a harmless spell or effect on the target, there is a 50% chance the target tries to avoid that effect as best as possible (taking an attack of opportunity against a spellcaster, requiring a successful attack roll on a touch spell, or attempting a saving throw).|
|26-50|Attempt a steal combat maneuver or Sleight of Hand check to steal a random valuable object from the nearest creature (or a nearby unattended object, if obviously of great value), moving adjacent to that creature or object as needed. Once an affected creature has stolen an item, further results of 26-50 cause the affected creature to flee, focusing all of its efforts on escaping with its loot and fighting to prevent the stolen object from being taken.|
|51-75|Attempt to break, destroy, or deface the nearest unattended manufactured object or structure. If the object or structure is too difficult to damage, the affected creature instead vandalizes or otherwise defaces its appearance.|
|76-100|Attack the nearest creature (for this purpose, a familiar counts as part of the affected creature's self).|

A character affected by a crime wave who is unable to carry out the indicated action moves toward
the nearest source of cover or concealment and attempts a Stealth check to hide. Affected creatures
with the ability to turn invisible (including through the use of magic items or spells) do so
instead of attempting a Stealth check.
