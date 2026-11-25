+++
id = "ref/arc-shifter/elementalist-shifter"
kind = "archetype"
title = "Elementalist Shifter"
aon = "ArchetypeDisplay.aspx?FixedName=Shifter%20Elementalist%20Shifter"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elementalist_shifter", path = "json/archetypes_shifter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shifter" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "78"

[fields]
kind = "archetype"
features = [
  { anchor = "languages" },
  { anchor = "elemental-aspect", level = 1 },
  { anchor = "elemental-speech", level = 1 },
  { anchor = "elemental-strike", level = 1 },
  { anchor = "elemental-form", level = 4 },
  { anchor = "omnielementalist", level = 9 },
  { anchor = "ash-storm" },
  { anchor = "downpour" },
  { anchor = "mudslide" },
  { anchor = "sandstorm" },
  { anchor = "steam-cloud" },
  { anchor = "volcanic-stride" },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["elemental-speech"] },
  { replaces = "Shifter claws", feature = "shifter-claws", by = ["elemental-strike"] },
  { replaces = "Chimeric aspect", feature = "chimeric-aspect", by = ["volcanic-stride"] },
  { replaces = "greater chimeric aspect", feature = "greater-chimeric-aspect", by = ["volcanic-stride"] },
  { alters = "Languages", feature = "bonus-languages", by = ["languages"] },
  { alters = "Shifter aspect", feature = "shifter-aspect", by = ["elemental-aspect"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["elemental-form"] },
]
+++

Rather than drawing power from bestial aspects, elementalist shifters channel power from the Inner
Sphere and can take on powerful elemental forms at the cost of the greater diversity available to
traditional shifters. Although the elementalist shifter's powers seem more outlandish and
supernatural than those of others of their kind, they remain equally immersed in the druidic
traditions; their focus is simply rooted in expressions of nature found in extraplanar regions: the
planes of Air, Earth, Fire, and Water.

## Languages {#languages}

An elementalist shifter adds Aquan, Auran, Ignan, and Terran to her list of available bonus
languages.

This alters the shifter's languages.

## Elemental Aspect (Su) {#elemental-aspect}

At 1st level, an elementalist shifter chooses one elemental aspect (see page 79) rather than a
shifter aspect. This ability otherwise functions as shifter aspect. As the elementalist shifter
gains levels, she gains more elemental aspects: a second aspect at 5th level, a third at 10th, and a
fourth at 15th.

This alters shifter aspect.

## Elemental Speech (Su) {#elemental-speech}

When in her elemental aspect, an elementalist shifter gains the benefit of
_[tongues](ref/spell/tongues)_ with creatures of the elemental subtype that matches her elemental
aspect.

This replaces wild empathy.

## Elemental Strike (Su) {#elemental-strike}

At 1st level, as a swift action, an elementalist shifter can charge her melee attacks with elemental
energy. The elementalist shifter can charge her attacks only with an element she has chosen with
elemental aspect. Once charged, each melee attack the elementalist shifter makes until the start of
her next turn deals an additional 1d6 points of energy damage based on the element she chooses when
taking this action (see Elemental Aspects on page 79). This additional damage increases by 1d6 at
4th level and every 4 levels thereafter, to a maximum of 6d6 points of energy damage at 20th level.
An elementalist shifter can't use elemental strike while under a polymorph effect.

This replaces shifter claws.

## Elemental Form (Su) {#elemental-form}

At 4th level, when an elementalist shifter uses wild shape, she is instead affected as if by
_[elemental body I](ref/spell/elemental-body-1)_, but she gains only the benefits listed in her
elemental aspect. While in an elemental form, the elementalist shifter can speak only the elemental
language associated with that form, and she can do so only if she knows it.

This alters wild shape.

## Omnielementalist (Su) {#omnielementalist}

At 9th level, an elementalist shifter can fuse two elemental forms together, gaining combined powers
of the different aspects and manifesting them in ways that bring to mind powerful natural weather
phenomena.

When the elementalist shifter takes on one minor form each from two of her elemental aspects, she
gains an additional ability as long as she maintains the form. The effects of the abilities depend
on the elemental combination, as detailed below.

## Ash Storm (Su) {#ash-storm}

By combining air and fire, the elementalist shifter surrounds herself with a storm of swirling ash,
granting her a 20% miss chance against ranged attacks.

## Downpour (Su) {#downpour}

The elementalist shifter combines the powers of air and water to generate a torrential downpour in
her square and squares adjacent to her. This rain automatically extinguishes all nonmagical fires in
her square and squares adjacent to her (including flames on creatures that have caught on fire). It
also has a chance to extinguish ongoing magical fire (but not instantaneous magical fire effects
such as _[fireball](ref/spell/fireball)_) within or that enters the area, as if the elementalist
shifter had cast _[dispel magic](ref/spell/dispel-magic)_, using her elementalist shifter level as
her caster level for the effect.

## Mudslide (Su) {#mudslide}

Combining the elements of earth and water causes the elementalist shifter to generate an aura of
mud. This mud extends out to all squares adjacent to her and counts as
[difficult terrain](ref/rule/terrain-and-obstacles); it moves with her and vanishes when she ends
her elemental aspect.

## Sandstorm (Su) {#sandstorm}

Combining the high winds of air and fine particulates of earth produces a sandstorm that extends out
to a radius of 20 feet from the elementalist shifter. All [light levels](ref/rule/vision-and-light)
in the area diminish by one step, and creatures caught in the effect take 1d6 points of nonlethal
damage each round they remain within the sandstorm.

## Steam Cloud (Su) {#steam-cloud}

When the elementalist shifter enters a minor form of fire and water at the same time, the heat of
fire and moisture of water generate an explosive area of steam around her out to a radius of 20 feet
as per _[obscuring mist](ref/spell/obscuring-mist)_. The mist remains in place until she ends her
elemental aspect; it doesn't move with her.

## Volcanic Stride (Su) {#volcanic-stride}

By combining earth and fire, the elementalist shifter can damage the ground around herself. As a
standard action, she can deform a region of natural or artificial rock in her space, turning it into
difficult terrain and causing creatures that pass through it to take an amount of fire damage equal
to that dealt by her elemental strike with no save. Affected terrain remains transformed until the
shifter ends her elemental aspect.

This replaces chimeric aspect and greater chimeric aspect.
