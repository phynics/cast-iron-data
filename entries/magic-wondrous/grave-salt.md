+++
id = "ref/magic-wondrous/grave-salt"
kind = "item"
title = "Grave Salt"
source_ids = ["ultimate-equipment"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "grave_salt", path = "json/magic_wondrous_slotless03.json" },
]

[fields]
kind = "item"
category = "Wondrous Items"
price = "1,100 gp"
weight = "5 lbs."
slot = "none"
aura = "faint evocation"
caster_level = "5th"
+++

**Sources:** Ultimate Equipment pg 301\
**Aura** faint evocation; **CL** 5th\
**Slot** none; **Price** 1,100 gp; **Weight** 5 lbs.

When poured on ground in a circle, this pure white salt sanctifies the enclosed area as the spell
_[consecrate](ref/spell/consecrate)._ Applying the salt takes 1 round per dose. A single dose is
sufficient to form a 5-foot radius circle, with each additional dose increasing the circle's radius
by 5 feet.^[1](ref/magic-wondrous/grave-salt#footnote-m)^ The area within the circle remains
consecrated for 1 hour per dose, though any corporeal creature can spend a standard action to break
the circle and end the effect prematurely. A newly created pouch of grave salt holds 5 doses.

Grave salt can also be used directly against restless spirits. A single dose can be hurled up to 15
feet as a ranged touch attack. An incorporeal undead creature struck by the salt must make a DC 14
Will save or take 1d4 points of [Charisma damage](ref/rule/ability-damage-drain). Strong winds and
other effects that penalize ranged attacks make it impossible to employ the salt in this manner.

### Construction

**Requirements** [Craft Wondrous Item](ref/feat/craft-wondrous-item),
[consecrate](ref/spell/consecrate); **Cost** 550 gp

###### ^1^ {#footnote-m}

This may seem mathematically sketchy, but it's actually true. The perimeter (length) of a 5-foot
radius circle is 10π feet. Increasing the radius by 5 feet increases the perimeter by another 10π
feet. Therefore, each dose contains enough salt to make a line roughly 31.4 ft. long.
