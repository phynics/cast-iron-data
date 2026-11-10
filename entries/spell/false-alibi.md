+++
id = "ref/spell/false-alibi"
kind = "spell"
title = "False Alibi"
aon = "SpellDisplay.aspx?ItemName=False%20Alibi"
source_ids = ["inner-sea-gods", "pathfinder-59-the-price-of-infamy"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "false_alibi", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/modify-memory" },
]
[[sources]]
publication = "inner-sea-gods"
page = "234"
[[sources]]
publication = "pathfinder-59-the-price-of-infamy"
page = "75"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 round"
components = "V, S, M (emerald dust worth 100 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "permanent; see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Cleric, Inquisitor, Oracle, Skald, Warpriest
Casting time: 1 round
Components: V, S, M (emerald dust worth 100 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent; see text
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

This spell functions similarly to [modify memory](ref/spell/modify-memory), except you can modify
the target's memory only in a specific way. In response to a triggering condition you determine, up
to the last 5 minutes of the target's memory are eliminated and replaced with a memory of your
choosing (or no memory at all). For example, you could cast this on an assassin, set it to trigger
when he completes his kill, and replace his memory of the murder with the memory of him discovering
the body and picking up the murder weapon. You can cast this spell multiple times on the same
target, even with the same trigger, affecting different memories. A single casting of false alibi
affects a creature only until the specified condition has been triggered; once a condition has been
triggered and the target's memory altered, that condition no longer triggers this spell unless the
victim is subject to another casting of false alibi that specifies the same trigger.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
