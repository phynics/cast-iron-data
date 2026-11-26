+++
id = "ref/arc-wizard/wind-listener"
kind = "archetype"
title = "Wind Listener"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Wind%20Listener"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wind_listener", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "advanced-race-guide"
page = "158"

[fields]
kind = "archetype"
features = [
  { anchor = "arcane-school" },
  { anchor = "spontaneous-divination", level = 1 },
  { anchor = "abjuration-sense", level = 5 },
  { anchor = "wispy-form", level = 10 },
  { anchor = "listening-to-the-wind", level = 15 },
]
trades = [
  { replaces = "Arcane bond", feature = "arcane-bond", by = ["spontaneous-divination"] },
  { replaces = "Bonus feat gained at 5th level", feature = "bonus-feats", levels = [5], by = ["abjuration-sense"] },
  { replaces = "Bonus feat gained at 10th level", feature = "bonus-feats", levels = [10], by = ["wispy-form"] },
  { replaces = "Bonus feat gained at 15th level", feature = "bonus-feats", levels = [15], by = ["listening-to-the-wind"] },
]
+++

The wind listener takes a sylph's natural curiosity to the extreme, enhancing his natural skill at
subterfuge and eavesdropping with potent arcane magic. A wind listener has the following class
features.

## Class Skills {#class-skills}

A wind listener adds Perception to his list of class skills.

## Arcane School {#arcane-school}

A wind listener cannot select divination or illusion as an opposition school.

## Spontaneous Divination (Su) {#spontaneous-divination}

At 1st level, a wind listener can reshape stored spell energy into divination spells he did not
prepare ahead of time. The wind listener can "lose" any prepared spell that is not a cantrip in
order to cast a divination spell of the same spell level or lower. The new spell must be one the
wind listener knows and is capable of casting. Spells cast with this ability increase their casting
time to a full-round action (if the spell's normal casting time is longer than a full-round action,
it remains unchanged). This ability replaces arcane bond.

## Abjuration Sense (Ex) {#abjuration-sense}

At 5th level, a wind listener develops a sixth sense for spotting spells designed to guard against
his investigations. He gains a bonus on Perception checks equal to 1/2 his level to notice spells of
the abjuration school and on [Spellcraft](ref/skill/spellcraft) checks to identify abjuration
effects, spells, and magic items. This ability replaces the bonus feat gained at 5th level.

## Wispy Form (Ex) {#wispy-form}

At 10th level, the wind listener gains the ability to become airy and translucent as a standard
action, gaining DR 10/magic and the effects of
_[greater invisibility](ref/spell/invisibility-greater)_ for a number of rounds per day equal to his
level. These rounds need not be consecutive. Like the
[natural invisibility](ref/umr/natural-invisibility) universal monster ability (_Bestiary 2_ 299),
this ability is not subject to _[invisibility purge](ref/spell/invisibility-purge)_. This ability
replaces the bonus feat gained at 10th level.

## Listening to the Wind (Sp) {#listening-to-the-wind}

At 15th level, the wind listener can call upon spirits of the air to uncover lost lore about a
legendary person, place, or thing. Invoking the spirits takes 10 minutes, during which time the wind
listener must be free of distractions and able to concentrate. Once called, the spirits seek out
information on the subject of the wind listener's inquiries. This functions as the spell
_[legend lore](ref/spell/legend-lore)_ (caster level equal to the wind listener's level), except
that the wind listener is free to engage in other activities while spirits investigate on his
behalf. The time required for the air spirits to return with this information is equal to what the
casting time of the spell _[legend lore](ref/spell/legend-lore)_ would have been if the wind
listener had cast it. The wind listener can use this ability once per week, and only if he does not
currently have air spirits searching for information. If the air spirits are currently searching for
information, the wind listener can end their task early as a standard action, dismissing the magical
effect and not returning any information. This ability replaces the bonus feat gained at 15th level.
