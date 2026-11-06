+++
id = "ref/spell/swallow-your-fear"
kind = "spell"
title = "Swallow Your Fear"
source_ids = ["pathfinder-35-war-of-the-river-kings", "inner-sea-gods"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "swallow_your_fear", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "enchantment"
levels = [
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature plus one additional creature per four levels, no two of which can be more than 30 ft. apart" },
]
duration = "10 minutes; see text"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Bard, Cleric, Oracle, Skald, Warpriest
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes; see text
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature plus one additional creature per four levels, no two of which can be more than 30 ft. apart
:::

**Sources:** Pathfinder \#35: War of the River Kings pg 73

You make the affected subjects ready for battle despite their fear. If a target is suffering from a
[fear effect](ref/rule/fear-conditions) of any kind, he gains a +2 morale bonus to Strength and
Constitution, a +1 morale bonus on Will saves, and a -2 penalty to AC. If the subject is frightened,
he remains in place and gains the [confused condition](ref/rule/awareness-conditions) for the
remainder of the fear effect, except he treats all results of "attack self" as "do nothing" and
treats "attack nearest creature" as "act normally." If the subject is panicked, he remains in place
and gains the confused condition for the duration of the fear effect.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
