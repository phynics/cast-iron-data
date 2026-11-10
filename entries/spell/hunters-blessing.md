+++
id = "ref/spell/hunters-blessing"
kind = "spell"
title = "Hunter's Blessing"
aon = "SpellDisplay.aspx?ItemName=Hunter%27s%20Blessing"
source_ids = ["inner-sea-gods"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hunters_blessing", path = "json/spells5.json" },
]
[[sources]]
publication = "inner-sea-gods"
page = "235"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Cleric, Druid, Hunter, Inquisitor, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature/level, no two of which can be more than 30 ft. apart
:::

When casting this spell, you designate a type or type and subtype of creature (using the
[ranger's](ref/class/ranger) [favored enemy](ref/ability/favored-enemy) categories) and a type of
terrain (using the list of ranger's [favored terrain](ref/ability/favored-terrain) categories).
Targets of the spell gain a +2 sacred bonus on Bluff, Perception, Sense Motive, and Survival checks
attempted against creatures of the selected type, and a +2 sacred bonus on attack rolls and damage
rolls made against creatures of that type. Furthermore, they gain a +2 sacred bonus on initiative
checks, Perception, Stealth, and Survival checks while they are in the type of terrain you
designate. Lastly, when tracking the designated creature type in the chosen terrain, the targets can
follow the tracks of such creatures untrained, even if the DC for the task is 11 or higher.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
