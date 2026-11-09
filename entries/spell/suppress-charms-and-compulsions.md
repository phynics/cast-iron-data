+++
id = "ref/spell/suppress-charms-and-compulsions"
kind = "spell"
title = "Suppress Charms and Compulsions"
aon = "SpellDisplay.aspx?ItemName=Suppress%20Charms%20and%20Compulsions"
source_ids = ["adventurers-guide", "andoran-spirit-of-liberty"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "suppress_charms_and_compulsions", path = "json/spells10.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "77"
[[sources]]
publication = "andoran-spirit-of-liberty"
page = "27"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature plus one additional creature per 4 levels, no two of which can be more than 30 ft. apart" },
]
duration = "10 minutes or concentration (up to 1 round/level); see text"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Arcanist, Bard, Cleric, Mesmerist, Oracle, Paladin, Psychic, Shaman, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes or concentration (up to 1 round/level); see text
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature plus one additional creature per 4 levels, no two of which can be more than 30 ft. apart
:::

You bolster the subject's sense of willpower and self-worth when you cast this spell. As you cast
it, you must decide if you want to grant a bonus to saving throws against charms and compulsions or
suppress charms and compulsions.

If you grant a bonus to saving throws, you grant all affected creatures a +4 morale bonus on saving
throws against charm and compulsion effects for 10 minutes.

If instead you suppress charms and compulsions, the spell's duration drops to concentration, to a
maximum duration of 1 round per level. As long as you continue to concentrate, the spell suppresses
all existing charm and compulsion effects affecting the targets, regardless of whether the effect is
beneficial or harmful. New charm or compulsion effects that successfully target such a protected
creature are automatically suppressed as long as you continue concentrating. If you cease
concentrating, the spell effect immediately ends, and remaining charm or compulsion effects resume
for the rest of their remaining durations as normal.
