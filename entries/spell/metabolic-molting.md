+++
id = "ref/spell/metabolic-molting"
kind = "spell"
title = "Metabolic Molting"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "metabolic_molting", path = "json/spells14.json" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "19"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
]
casting_time = "10 minutes"
components = "V, S, M (a valuable gemstone worth at least 250 gp)"
range = "touch"
effects = [
  { label = "Target", value = "willing creature or dead body touched" },
]
duration = "see text"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Cleric, Druid, Hunter, Oracle, Shaman, Warpriest, Witch
Casting time: 10 minutes
Components: V, S, M (a valuable gemstone worth at least 250 gp)
Range: touch
Duration: see text
Saving throw: Will negates (harmless)
Spell resistance: no
Target: willing creature or dead body touched
:::

> _The following spell is the result of generations of [nagaji](ref/race/nagaji) tradition, but
> spellcasters from elsewhere in Tian Xia have begun to learn these techniques and spread them
> further._

You encase the willing subject in a jeweled shell that has the same [hardness](ref/umr/hardness) and
hit points as 5 inches of iron (hardness 10, hp 150). For 7 days, the subject enters a state of
suspended animation (as per temporal stasis), during which it heals from even the most grievous
wounds. Each day, the subject regains 5 hit points per Hit Die it has as well as recovering from 2
points of ability damage or ability drain from any ability score of its choice. After 7 days, the
shell crumbles away and the subject emerges, its body's severed limbs, broken bones, and ruined
organs regrown (as per regenerate).

If the gemstone you use for the component is worth at least 5,000 gp, metabolic molting can bring a
target back to life, as long as it has been dead for no more than 1 hour when the spell is cast.
When the spell is used on such a creature, the creature comes back to life after 7 days and
stabilizes at 0 hit points. A creature brought back to life through metabolic molting gains 1
permanent negative level, or 2 points of Constitution drain if it is 1st level. Like
[raise dead](ref/spell/raise-dead), this spell can't save creatures slain by death effects.
