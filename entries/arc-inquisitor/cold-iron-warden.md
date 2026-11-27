+++
id = "ref/arc-inquisitor/cold-iron-warden"
kind = "archetype"
title = "Cold Iron Warden"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Cold%20Iron%20Warden"
source_ids = ["demon-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cold_iron_warden", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "demon-hunters-handbook"
page = "15"

[fields]
kind = "archetype"
features = [
  { anchor = "track-teleportation", level = 2 },
  { anchor = "abyssal-scourge", level = 3 },
  { anchor = "favored-judgment", level = 3 },
  { anchor = "bane", level = 5 },
  { anchor = "translate-telepathy", level = 5 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["track-teleportation"] },
  { replaces = "teamwork feats gained at 12th and 18th level", feature = "teamwork-feat", levels = [12, 18], by = ["track-teleportation"] },
  { replaces = "Solo tactics", feature = "solo-tactics", by = ["abyssal-scourge"] },
  { replaces = "teamwork feats gained at 6th and 15th level", feature = "teamwork-feat", levels = [6, 15], by = ["abyssal-scourge"] },
  { replaces = "Teamwork feats gained at 3rd and 9th level", feature = "teamwork-feat", levels = [3, 9], by = ["favored-judgment"] },
  { replaces = "Discern lies", feature = "discern-lies", by = ["translate-telepathy"] },
  { alters = "Bane", feature = "bane", by = ["bane"] },
]
+++

The natural enemies of [demoniacs](ref/pclass/demoniac) and other cultists of fiendish forces, cold
iron wardens are inquisitors who dedicate their lives to eradicating the taint of
[demonkind](ref/family/demon) from Golarion.

## Track Teleportation (Su) {#track-teleportation}

At 2nd level, a cold iron warden may acquire clues about a teleporting creature's destination by
closely examining the place it once stood. As a full-round action while standing in a square that a
creature occupied when it cast a conjuration (teleportation) spell or
[spell-like ability](ref/umr/spell-like-abilities), the cold iron warden may attempt a Survival
check (DC 10 + the teleportation spell's caster level) to sense the direction of the creature's
destination as well as whether the destination lies within 25 feet, 100 feet, 1,000 feet, or more
than 1,000 feet of her. She must use this ability within a number of rounds after the creature's
teleportation equal to 1/2 her inquisitor level, after which the trail goes cold. A cold iron warden
may use this ability once per day plus one additional time per day for every 4 levels she has beyond
2nd.

At 12th level, if the cold iron warden exceeds the Survival check DC by 5 or more, she can also
sense the creature's location as if using the [locate creature](ref/spell/locate-creature) spell,
using her inquisitor level as the caster level. At 18th level, if the cold iron warden exceeds the
Survival check DC by 10 or more, she can also sense the creature's location as if she had cast
[discern location](ref/spell/discern-location). This ability replaces track and the teamwork feats
gained at 12th and 18th level.

## Abyssal Scourge (Su) {#abyssal-scourge}

At 3rd level, a cold iron warden gains [Alignment Channel](ref/feat/alignment-channel) as a bonus
feat and must choose either chaotic or evil outsiders. She can
[channel energy](ref/ability/channel-energy) as a cleric of her inquisitor level - 2 a number of
times per day equal to 3 + her Charisma modifier, but only to use Alignment Channel to damage
outsiders. The DC of the Will save to halve the damage is equal to 10 + 1/2 the inquisitor's level +
the inquisitor's Charisma modifier. At 6th level, the energy lingers in the affected area for 1
round as a shimmering, barely perceptible, mist that disrupts Abyssal magic. A creature in the mist
that casts a conjuration (summoning) spell or [spell-like ability](ref/umr/spell-like-abilities)
with the selected alignment subtype must succeed at a [concentration](ref/rule/concentration) check
or lose the spell. At 15th level, any chaotic or evil creature that casts a conjuration
(teleportation) spell or [spell-like ability](ref/umr/spell-like-abilities) while in the mist must
succeed at a concentration check or lose the spell. The concentration check DC for both abilities is
equal to 15 + double the level of the conjuration spell.

A cold iron warden can take other feats to add to this ability such as Improved Channeling, but not
feats that alter this ability, such as [Command Undead](ref/feat/command-undead). This ability
replaces solo tactics and the teamwork feats gained at 6th and 15th level.

## Favored Judgment {#favored-judgment}

At 3rd level, the inquisitor gains [Favored Judgment](ref/feat/favored-judgment) as a bonus feat but
must choose either outsider (chaotic) or outsider (evil). At 9th level, she gains Favored Judgment
as a bonus feat a second time and must choose either outsider (chaotic) or outsider (evil). This
ability replaces the teamwork feats gained at 3rd and 9th level.

## Bane (Su) {#bane}

A cold iron warden reduces the amount of bonus damage dealt when using her bane ability against
creatures that are not outsiders with the chaotic or evil subtype by 1d6. She increases the amount
of bonus damage by 1d6 when she selects outsiders with the chaotic or evil subtype. This ability
modifies the bane ability.

## Translate Telepathy (Su) {#translate-telepathy}

At 5th level, an inquisitor can sense when a creature within 5 feet of her receives or sends a
telepathic message. The distance at which she can detect telepathic messages increases by 5 feet for
every 5 additional inquisitor levels she has beyond 5th level, to a maximum of 20 feet at 20th
level. By making a Perception check (DC 15 + the highest CR of the creatures using telepathy) as an
immediate action, she may listen to all telepathic messages sent to and by creatures in this area
for a number of rounds per day equal to her inquisitor level. These rounds do not need to be
consecutive. This ability replaces discern lies.
