+++
id = "ref/arc-inquisitor/traceless-operative"
kind = "archetype"
title = "Traceless Operative"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Traceless%20Operative"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "traceless_operative", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "30"

[fields]
kind = "archetype"
replaces = ["Monster lore", "stern gaze", "Track", "Bane", "Greater bane"]
replaces_features = ["monster-lore", "stern-gaze", "track", "bane", "greater-bane"]
+++

Traceless operatives practice subterfuge and careful preparation in order to accomplish their divine
mandates.

**Conceal Evidence (Ex)**

**Ability:** A traceless operative knows how to clean up and obscure the evidence of foul play. It
takes her 1d3 &times& 10 minutes to conceal or alter evidence in a 10-foot-by-10-foot area. She uses
Disguise to alter evidence or Stealth to conceal it, though bonuses and penalties based on her
abilities or effects that disguise or hide her own body (such as from
[disguise self](ref/spell/disguise-self), a
[cloak of elvenkind](ref/magic-wondrous/cloak-of-elvenkind), or the size modifier on Stealth checks)
do not apply.

**Replaces:** Monster lore, stern gaze

**Special:** A creature attempting to investigate the scene using Perception must succeed at the
original Perception DC or a DC equal to the traceless operative's check, whichever is higher, in
order to discover the true evidence. A creature who fails against a traceless operative's Disguise
check potentially also derives the false evidence planted by the traceless operative.

**Trackless (Sp)**

**Flavor:** A traceless operative's deity helps obscure her path from others.

**Gained:** At 2nd Level

**Passive:** The DC to track the traceless operative (or a group including her) increases by
[half](ref/misc/fractions-and-rounding) her inquisitor level. This does not stack with similar
abilities, such as a [transporter's](ref/arc-ranger/transporter) _trailbreaker_ ability.

**Replaces:** Track

**Uncanny Dodge (Ex)**

**Ability:** A traceless operative can react to danger before her senses would normally allow her to
do so. She cannot be caught [flat-footed](ref/rule/flat-footed), nor does she lose her Dexterity
bonus to AC if the attacker is invisible. She still loses her Dexterity bonus to AC if immobilized.
A traceless operative with this ability can still lose her Dexterity bonus to AC if an opponent
successfully uses the feint action against her. If the traceless operative already possesses
[uncanny dodge](ref/ability/uncanny-dodge) from a different class, she automatically gains _improved
uncanny dodge_ instead.

**Gained:** At 5th Level

**Replaces:** Bane

**Improved Uncanny Dodge (Ex)**

**Gained:** At 12th Level

**Passive:** A traceless operative can no longer be [flanked](ref/rule/flanking). This defense
denies [rogues](ref/class/rogue) (or other classes with the [sneak attack](ref/ability/sneak-attack)
ability) the ability to _sneak attack_ the traceless operative by flanking her, unless the attacker
has at least 4 more rogue levels (or levels in a class that grants the _sneak attack_ class ability)
than the traceless operative has inquisitor levels. If the traceless operative already has
[improved uncanny dodge](ref/ability/improved-uncanny-dodge) from another class, the levels from the
classes that grant _improved uncanny dodge_ stack when determining the minimum rogue level (or level
in another class with the _sneak attack_ ability) required to flank the character.

**Replaces:** Greater bane
