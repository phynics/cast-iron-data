+++
id = "ref/spell/replenish-ki"
kind = "spell"
title = "Replenish Ki"
aon = "SpellDisplay.aspx?ItemName=Replenish%20Ki"
source_ids = ["inner-sea-gods", "pathfinder-53-tide-of-honor"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "replenish_ki", path = "json/spells8.json" },
]
[[sources]]
publication = "inner-sea-gods"
page = "238"
[[sources]]
publication = "pathfinder-53-tide-of-honor"
page = "73"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 minute"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Cleric, Oracle, Warpriest
Casting time: 1 minute
Components: V, S, DF
Range: touch
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Healing
:::

You attune the target's internal store of supernatural energy to the cosmos, replenishing its ki
pool. If you are the target, you regain 2 ki points. If another creature is the target, it regains 1
ki point. This does not allow the target to exceed its ki pool's maximum. This spell has no effect
if the target does not have a ki pool.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
