+++
id = "ref/arc-inquisitor/umbral-stalker"
kind = "archetype"
title = "Umbral Stalker"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Umbral%20Stalker"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "umbral_stalker", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "31"

[fields]
kind = "archetype"
features = [
  { anchor = "dark-descent" },
  { anchor = "judgment" },
  { anchor = "swift-and-silent", level = 1 },
  { anchor = "deadly-efficiency", level = 14 },
]
trades = [
  { replaces = "Justice judgment", feature = "judgment", power = "justice", by = ["judgment"] },
  { replaces = "Stern gaze", feature = "stern-gaze", by = ["swift-and-silent"] },
  { alters = "Domain", feature = "domain", by = ["dark-descent"] },
  { alters = "Exploit weakness", feature = "exploit-weakness", by = ["deadly-efficiency"] },
]
+++

As a consummate lurker in the shadows, an umbral stalker observes the enemies of her faith and
strikes before the unfortunate victims even know she is skulking nearby.

## Class Skills {#class-skills}

An umbral stalker adds Acrobatics to her list of class skills, instead of Diplomacy.

This alters the inquisitor's class skills.

## Dark Descent (Su) {#dark-descent}

An umbral stalker gains the Darkness domain with the Night subdomain, even if her deity normally
doesn't offer it.

This ability alters domain.

## Judgment {#judgment}

Umbral stalkers are most effective when they get the drop on an opponent. An umbral stalker gains
access to the following judgment.

### Stalking {#stalking}

The umbral stalker gains a +2 sacred bonus on attack rolls against creatures that are unaware of her
presence (typically because she is invisible or using Stealth). This bonus increases by 2 for every
5 inquisitor levels she has.

This ability replaces the justice judgment.

## Swift and Silent (Ex) {#swift-and-silent}

Umbral stalkers often descend upon their prey with deadly grace and efficiency. An umbral stalker
gains a morale bonus on all Acrobatics and Stealth checks equal to
[half](ref/misc/fractions-and-rounding) her inquisitor level (minimum +1).

This ability replaces stern gaze.

## Deadly Efficiency (Ex) {#deadly-efficiency}

At 14th level, an umbral stalker becomes even deadlier against enemies who haven't yet noticed her
in the shadows. Whenever she confirms a critical hit against a foe that is unaware of her presence,
she ignores any [damage reduction](ref/rule/damage-reduction) the target might have and adds her
Wisdom bonus to her damage roll (this multiplies on the critical hit as normal); in addition, if the
target has [regeneration](ref/umr/regeneration), the creature loses regeneration on the round
following the critical hit and can die normally during that round. Creatures whose regeneration
always functions are immune to this ability.

Finally, if the umbral stalker deals energy damage to a creature unaware of her presence with
vulnerability to that energy type, she deals 2 extra points of damage per die rolled.

This ability alters exploit weakness.
