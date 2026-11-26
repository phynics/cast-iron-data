+++
id = "ref/arc-gunslinger/gun-scavenger"
kind = "archetype"
title = "Gun Scavenger"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Gun%20Scavenger"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gun_scavenger", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "inner-sea-combat"
page = "38"

[fields]
kind = "archetype"
features = [
  { anchor = "gunsmith", level = 1 },
  { anchor = "go-by-feel" },
  { anchor = "change-out", level = 1 },
  { anchor = "jury-rig", level = 7 },
  { anchor = "arbitrary-aim", level = 2 },
]
trades = [
  { replaces = "Quick clear deed", feature = "deeds", power = "quick clear", by = ["change-out"] },
  { replaces = "Targeting deed", feature = "deeds", power = "targeting", by = ["jury-rig"] },
  { replaces = "Nimble", feature = "nimble", by = ["arbitrary-aim"] },
  { alters = "Gunsmith", feature = "gunsmith", by = ["gunsmith"] },
]
+++

Although Alkenstar is the center of firearm production and innovation in the Inner Sea, the crack of
flint and tang of gun smoke is enough to inspire enthusiasts elsewhere to try their hand at making
their own guns using intuition instead of blueprints. A gun scavenger collects scraps, spare parts,
and other components that might—if modified properly—give her firearm an extra edge.

## Gunsmith {#gunsmith}

The gun scavenger's starting weapon is a mishmash of pieces that even other gunpowder enthusiasts
fail to comprehend. Anyone other than the gun scavenger treats her starting weapon as
[broken](ref/misc/broken), even if she uses the [Gunsmithing](ref/feat/gunsmithing) feat to repair
it. This ability works in all other ways like the gunslinger's gunsmith class feature.

## Go By Feel (Ex) {#go-by-feel}

A gun scavenger's intuitive and unique style leaves her firearms prone to misfire, whether as a
result of using too much powder, using imperfectly milled parts, or any number of other minor
inconsistencies. When using a firearm, a gun scavenger cannot reduce that firearm's misfire chance
to 0; it can always misfire on a natural 1.

## Deeds {#deeds}

A gun scavenger gains the following deeds at the listed level.

## Change Out (Ex) {#change-out}

At 1st level, as a full-round action, a gun scavenger can remove the broken condition from a single
firearm she is currently wielding, as long as that condition was gained by a firearm misfire. When
she does, she can replace the broken part with a specialized, short-lived component that does one of
the following: gives the firearm the [scatter](ref/misc/scatter) weapon quality; increases the
damage dealt by the [pistol-whip](ref/deed/pistol-whip) deed by one die size; or increases the
firearm's range increment by 10 feet. A firearm with such a modification increases its misfire
chance cumulatively by 1 each time it is fired until it misfires. When it does misfire, the effects
of the temporary component are lost. A gun scavenger must have at least 1 grit point to perform this
deed. Alternatively, if the gun scavenger spends 1 grit point to perform a change out, she can
either perform the change out as a standard action instead of a full-round action, or perform the
change out on a firearm that isn't broken. This deed replaces the quick clear deed.

## Jury-Rig (Ex) {#jury-rig}

At 7th level, as a standard action, a gun scavenger can adjust a firearm she is currently wielding
to fire in an unconventional way. She can spend 1 grit point to grant her firearm one of the
following magic weapon enhancements for 1 round per gunslinger level:
_[distance](ref/magic-enh/distance), [flaming](ref/magic-enh/flaming),
[glamered](ref/magic-enh/glamered-weapon)_, or _[thundering](ref/magic-enh/thundering)_. If she
spends 2 grit points, she can instead grant the firearm
_[flaming burst](ref/magic-enh/flaming-burst)_ or _[stalking](ref/magic-enh/stalking)_. Multiple
uses of this ability don't stack with themselves. This deed replaces the targeting deed.

## Arbitrary Aim (Ex) {#arbitrary-aim}

Starting at 2nd level, a gun scavenger's attacks with firearms are difficult to predict. When
shooting a firearm at a creature that has a dodge or insight bonus to its Armor Class, the gun
scavenger treats the combined bonus as if it were 1 lower. This value increases by 1 for every 4
levels beyond 2nd level (to a maximum of 5 at 20th level). This ability replaces nimble.
