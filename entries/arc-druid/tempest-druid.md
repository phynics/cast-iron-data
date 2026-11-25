+++
id = "ref/arc-druid/tempest-druid"
kind = "archetype"
title = "Tempest Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Tempest%20Druid"
source_ids = ["adventurers-guide", "inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tempest_druid", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "adventurers-guide"
page = "183"
[[sources]]
publication = "inner-sea-magic"
page = "41"

[fields]
kind = "archetype"
features = [
  { anchor = "armor-and-weapon-proficiencies" },
  { anchor = "spontaneous-domain-casting" },
  { anchor = "nature-bond" },
  { anchor = "sodden-shore-sense", level = 1 },
  { anchor = "electrical-resistance", level = 3 },
  { anchor = "eyes-of-the-storm", level = 4 },
  { anchor = "bend-bolt", level = 9 },
]
trades = [
  { replaces = "The druid's normal ability to spontaneously cast summon spells", feature = "spontaneous-casting", by = ["spontaneous-domain-casting"] },
  { replaces = "Nature sense", feature = "nature-sense", by = ["sodden-shore-sense"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["electrical-resistance"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["eyes-of-the-storm"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["bend-bolt"] },
  { alters = "Armor and weapon proficiencies", feature = "weapon-and-armor-proficiencies", by = ["armor-and-weapon-proficiencies"] },
  { alters = "Nature bond", feature = "nature-bond", by = ["nature-bond"] },
  { alters = "Alignment" },
]
+++

Many of the druids who train under the aegis of the [Storm Kindlers](ref/rule/aff-storms) focus on
different areas of nature than those classically paid homage to by their kind. These so-called
tempest druids see the personification of nature in the fury of the storm alone and to some extent
eschew the veneration of plant or animal life, and the nature of their powers shifts accordingly.
They still understand the place of plants and animals in the natural order, however; they simply
view such entities—and indeed, all forms of life—as subservient to the true power found in the
storms that lash the world.

## Alignment {#alignment}

The beliefs held by tempest druids are inherently more chaotic than those held by most druids, and
as a result, tempest druids must be chaotic neutral.

This alters the druid's alignment.

## Armor and Weapon Proficiencies {#armor-and-weapon-proficiencies}

A tempest druid is proficient with the [trident](ref/eq-weapon/trident), in addition to the druid's
normal armor and weapon proficiencies.

This alters the druid's armor and weapon proficiencies.

## Spontaneous Domain Casting {#spontaneous-domain-casting}

A tempest druid can channel stored spell energy into domain spells that he has not prepared ahead of
time. He can "lose" a prepared spell to cast any domain spell of the same level or lower.

This replaces the druid's normal ability to spontaneously cast summon spells.

## Nature Bond (Ex) {#nature-bond}

As a result of his beliefs, a tempest druid has little connection to the spirituality of animals or
plants. He can't choose an animal companion, and must instead select a domain or subdomain from the
following list when he gains the nature bond ability: [Air](ref/domain/air),
[Aquatic](ref/druiddomain/aquatic), [Cloud](ref/domain/air), Storm, [Swamp](ref/druiddomain/swamp),
[Weather](ref/domain/weather), or [Wind](ref/domain/air).

This alters nature bond.

## Sodden Shore Sense (Ex) {#sodden-shore-sense}

A tempest druid gains a +4 bonus on Knowledge (nature) and Survival checks in coastal or marshy
lands.

This ability replaces nature sense.

## Electrical Resistance (Ex) {#electrical-resistance}

At 3rd level, a tempest druid gains electricity resistance 5. As a standard action, he can transfer
this resistance to another creature for 1 hour, after which time it reverts to him.

This ability replaces trackless step.

## Eyes of the Storm (Ex) {#eyes-of-the-storm}

At 4th level, a tempest druid can see through 10 feet of magical fog, mist, rain, wind, or similar
inclement weather conditions, ignoring any concealment such conditions might grant. This distance
increases by 5 feet for every 4 levels beyond 4th.

This ability replaces resist nature's lure.

## Bend Bolt (Su) {#bend-bolt}

At 9th level, a tempest druid can redirect nearby electrical attacks. As an immediate action, the
druid can shift the area or target of an electricity attack by 5 feet in any direction. If the
electricity affects an area, the druid selects one square to be unaffected and an adjacent square to
be affected. If the adjacent square is already in the area, this has no additional effect in that
square. If the electricity affects a target, the druid selects an adjacent target. For example, if
he were in the line of a wizard's _lightning bolt_, he could have the spell skip his square and
instead affect an adjacent square, even if this meant the spell did not form a continuous line. If
another druid attacked him with _[call lightning](ref/spell/call-lightning)_, he could shift the
called bolt to an adjacent square, affecting a creature in that square (if any).

He can't redirect electricity damage conducted to him by physical contact with an object or creature
(such as a _[shocking grasp](ref/spell/shocking-grasp)_ or a _[shock](ref/magic-enh/shock)_ weapon).
He can use this ability a number of times per day equal to his Wisdom bonus.

This ability replaces venom immunity.
