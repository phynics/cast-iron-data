+++
id = "ref/arc-bard/sea-singer"
kind = "archetype"
title = "Sea Singer"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Sea%20Singer"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sea_singer", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "advanced-players-guide"
page = "84"

[fields]
kind = "archetype"
features = [
  { anchor = "sea-shanty", level = 1 },
  { anchor = "still-water", level = 3 },
  { anchor = "whistle-the-wind", level = 6 },
  { anchor = "call-the-storm", level = 18 },
  { anchor = "world-traveler", level = 1 },
  { anchor = "familiar", level = 2 },
  { anchor = "sea-legs", level = 2 },
]
trades = [
  { replaces = "Countersong", feature = "bardic-performance", power = "countersong", by = ["sea-shanty"] },
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["still-water"] },
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["whistle-the-wind"] },
  { replaces = "Mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["call-the-storm"] },
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["world-traveler"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["familiar"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["sea-legs"] },
]
+++

The sea singer calls the blue waters his home, and is much in demand among sea captains wishing good
fortune for their crew and hull as they ply the tradewinds far and wide.

## Bardic Performance {#bardic-performance}

A sea singer gains the following types of bardic performance.

## Sea Shanty (Su) {#sea-shanty}

A sea singer learns to counter seasickness and exhaustion during long sea voyages. Each round of a
sea shanty, he makes a Perform skill check. Allies within 30 feet (including the sea singer) may use
his Perform check in place of a saving throw against becoming exhausted, fatigued, nauseated, or
sickened; if already under such an effect, a new save is allowed each round of the sea shanty, using
the bard's Perform check for the save. A sea shanty has no effect on instantaneous effects or
effects that do not allow saves. This ability requires audible components. This performance replaces
countersong.

## Still Water (Su) {#still-water}

At 3rd level, a sea singer can use performance to calm rough waters within 30 feet, reducing the DC
for Profession (sailor) and Swim checks, as well as for Acrobatics and Climb checks aboard ship, by
an amount equal to the bard's level (to a minimum of DC 10) for as long he continues to perform. He
can extend this duration to 1 hour by playing for 10 consecutive rounds. This ability requires
audible components. This performance replaces inspire competence.

## Whistle the Wind (Su) {#whistle-the-wind}

A sea singer of 6th level or higher can use performance to create a
_[gust of wind](ref/spell/gust-of-wind)_. This wind lasts for as long as he continues his
performance. He can extend this duration to 1 minute by playing for 5 consecutive rounds. This
performance replaces suggestion.

## Call the Storm (Su) {#call-the-storm}

At 18th level, a sea singer can use performance to duplicate _control water, control weather,
control winds,_ or _[storm of vengeance](ref/spell/storm-of-vengeance)_, using his bard level as the
caster level. Using this ability requires 1 round of continuous performance per level of the spell
(as if he were a [druid](ref/class/druid)). These effects continue for as long as the bard continues
performing (the effects of _[control weather](ref/spell/control-weather)_ happen immediately), but
not longer than the spell's normal duration. This performance replaces mass suggestion.

## World Traveler (Ex) {#world-traveler}

A sea singer gains a bonus equal to [half](ref/misc/fractions-and-rounding) his bard level on
Knowledge (geography), Knowledge (local), Knowledge (nature), and Linguistics checks. He can reroll
a check against one of these skills, but must take the result of the second roll even if it is
worse. He can reroll one additional time per day at 5th level and every five levels thereafter. This
ability replaces bardic knowledge.

## Familiar {#familiar}

At 2nd level, a sea singer acquires an exotic pet—a [monkey](ref/monster/familiar-monkey) or parrot
(treat as [raven](ref/monster/familiar-raven))—that gains abilities as a wizard's
[familiar](ref/ability/familiars), using the sea singer's bard level as his wizard level. This
ability replaces versatile performance.

## Sea Legs (Ex) {#sea-legs}

At 2nd level, a sea singer gains a +4 bonus on saving throws against air and water effects and
effects that would cause the sea singer to slip, trip, or otherwise be knocked
[prone](ref/rule/prone). He gains a +2 bonus to CMD against grapple, overrun, and trip. This ability
replaces well-versed.
