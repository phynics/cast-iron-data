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
replaces = ["Countersong", "Inspire competence", "Suggestion", "Mass suggestion", "Bardic knowledge", "Versatile performance", "Well-versed"]
replaces_features = ["bardic-knowledge", "versatile-performance", "well-versed"]
+++

The sea singer calls the blue waters his home, and is much in demand among sea captains wishing good
fortune for their crew and hull as they ply the tradewinds far and wide.

**Bardic Performance**

**Info:** A sea singer gains the following types of bardic performance.

**Sea Shanty (Su)**

**Ability:** A sea singer learns to counter seasickness and exhaustion during long sea voyages. Each
round of a sea shanty, he makes a Perform skill check. Allies within 30 feet (including the sea
singer) may use his Perform check in place of a saving throw against becoming exhausted, fatigued,
nauseated, or sickened; if already under such an effect, a new save is allowed each round of the sea
shanty, using the bard's Perform check for the save.

**Replaces:** Countersong

**Special:** A sea shanty has no effect on instantaneous effects or effects that do not allow saves.
This ability requires audible components.

**Still Water (Su)**

**At 3rd Level:** A sea singer can use performance to calm rough waters within 30 feet, reducing the
DC for Profession (sailor) and Swim checks, as well as for Acrobatics and Climb checks aboard ship,
by an amount equal to the bard's level (to a minimum of DC 10) for as long he continues to perform.
He can extend this duration to 1 hour by playing for 10 consecutive rounds.

**Replaces:** Inspire competence

**Special:** This ability requires audible components.

**Whistle the Wind (Su)**

**At 6th Level:** A sea singer can use performance to create a
[gust of wind](ref/spell/gust-of-wind). This wind lasts for as long as he continues his performance.
He can extend this duration to 1 minute by playing for 5 consecutive rounds.

**Replaces:** Suggestion

**Call the Storm (Su)**

**At 18th Level:** A sea singer can use performance to duplicate
[control water](ref/spell/control-water), [control weather](ref/spell/control-weather),
[control winds](ref/spell/control-winds), or [storm of vengeance](ref/spell/storm-of-vengeance),
using his bard level as the caster level. Using this ability requires 1 round of continuous
performance per level of the spell (as if he were a [druid](ref/class/druid)). These effects
continue for as long as the bard continues performing (the effects of
_[control weather](ref/spell/control-weather)_ happen immediately), but not longer than the spell's
normal duration.

**Replaces:** Mass suggestion

**World Traveler (Ex)**

**Ability:** He can reroll a check against one of these skills, but must take the result of the
second roll even if it is worse.

**Passive:** A sea singer gains a bonus equal to [half](ref/misc/fractions-and-rounding) his bard
level on Knowledge (geography), Knowledge (local), Knowledge (nature), and Linguistics checks.

**Replaces:** Bardic knowledge

**Usage:** 1 time/day + 1 per 5 bard levels

**Familiar**

**Ability:** A sea singer acquires an exotic pet - a [monkey](ref/monster/familiar-monkey) or parrot
(treat as [raven](ref/monster/familiar-raven)) - that gains abilities as a wizard's
[familiar](ref/ability/familiars), using the sea singer's bard level as his wizard level.

**Gained:** At 2nd Level

**Replaces:** Versatile performance

**Sea Legs (Ex)**

**Gained:** At 2nd Level

**Passive:** A sea singer gains a +4 bonus on saving throws against air and water effects and
effects that would cause the sea singer to slip, trip, or otherwise be knocked
[prone](ref/rule/prone). He gains a +2 bonus to CMD against grapple, overrun, and trip.

**Replaces:** Well-versed
