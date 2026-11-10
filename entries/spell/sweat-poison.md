+++
id = "ref/spell/sweat-poison"
kind = "spell"
title = "Sweat Poison"
aon = "SpellDisplay.aspx?ItemName=Sweat%20Poison"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sweat_poison", path = "json/spells10.json" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "11"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["poison"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 2 },
  { class = "Ranger", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Alchemist, Hunter, Investigator, Ranger\
3: Druid, Inquisitor
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: poison
:::

> _Drawing on aspects of their amphibious animal counterparts, the following spell is more common
> among [grippli](ref/race/grippli) spellcasters than among those of other races._

Glands along your neck, back, or wrists swell and exude a viscous injury poison (see below). You are
not immune to this poison, and unless you have the poison use class feature or a similar ability,
you are at risk of poisoning yourself. You can apply this poison to a weapon as a move action, and
each dose you apply reduces the remaining duration of this spell by 1 minute. If doing so would
reduce the remaining duration to 0 minutes or less, the spell ends, and any applied poisons retain
their potency only until the end of your turn. When you apply the poison, you can choose to reduce
the spell's remaining duration by 2 or more additional minutes (maximum = your caster level) in
order to enhance that dose of poison. For every 2 minutes of duration expended, the poison's save DC
increases by 1, the number of rounds it lasts increases by 1/2 (round down), and the number of saves
required to cure it increases by 1/4 (round down). If you have the toxic skin alternate racial
trait, you can expend one daily use as a free action to enhance this spell's poison's damage to 1d3
Strength and its starting save DC to 15.

**Type:** Poison (Injury)

**Save:** Fortitude DC 14

**Frequency:** 1/round for 4 rounds

**Effect:** Strength damage 1d2

**Cure:** 1 save
