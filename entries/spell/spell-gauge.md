+++
id = "ref/spell/spell-gauge"
kind = "spell"
title = "Spell Gauge"
source_ids = ["inner-sea-gods", "faiths-of-balance"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_gauge", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, F (a silver piece)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Arcanist, Bard, Cleric, Inquisitor, Oracle, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a silver piece)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: mind-affecting
:::

**Sources:** Inner Sea Gods pg 242, Faiths of Balance pg 29

You immediately discover some of the spells that the target knows or has prepared. The number of
spells revealed to you is equal to your caster level. The target's lowest-level spells are revealed
first - ignoring 0-level spells - in a random order. Once all of the target's 1st-level spells are
revealed, the spell begins revealing 2nd-level spells, then 3rd-level spells. This spell does not
reveal spells of 4th level or higher, nor does it reveal
[spell-like abilities](ref/umr/spell-like-abilities) or other special abilities. If cast on a
creature that is not a spellcaster, that has only 0-level spells or spells of 4th level or higher
prepared, that has expended all of its spells, or that has not prepared any spells that day, the
spell has no effect.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
