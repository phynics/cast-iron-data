+++
id = "ref/arc-gunslinger/gun-scavenger"
kind = "archetype"
title = "Gun Scavenger"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gun_scavenger", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]

[fields]
kind = "archetype"
replaces = ["Quick clear deed", "Targeting deed", "Nimble"]
alters = ["Gunsmith"]
+++

**Sources:** Inner Sea Combat pg 38\
Although Alkenstar is the center of firearm production and innovation in the Inner Sea, the crack of
flint and tang of gun smoke is enough to inspire enthusiasts elsewhere to try their hand at making
their own guns using intuition instead of blueprints. A gun scavenger collects scraps, spare parts,
and other components that might - if modified properly - give her firearm an extra edge.

**Gunsmith**

**Alters:** Gunsmith

**Info:** The gun scavenger's starting weapon is a mishmash of pieces that even other gunpowder
enthusiasts fail to comprehend. Anyone other than the gun scavenger treats her starting weapon as
[broken](ref/misc/broken), even if she uses the [Gunsmithing](ref/feat/gunsmithing) feat to repair
it. This ability works in all other ways like the gunslinger's _gunsmith_ class feature.

**Go By Feel (Ex)**

**Flavor:** A gun scavenger's intuitive and unique style leaves her firearms prone to misfire,
whether as a result of using too much powder, using imperfectly milled parts, or any number of other
minor inconsistencies.

**Info:** When using a firearm, a gun scavenger cannot reduce that firearm's misfire chance to 0; it
can always misfire on a natural 1.

**Deeds**

**Info:** A gun scavenger gains the following deeds at the listed level.

**Change Out (Ex)**

**Action:** Full-Round Action

**Gained:** At 1st Level

**Replaces:** Quick clear deed

**Special:** A gun scavenger must have at least 1 grit point to perform this deed. Alternatively, if
the gun scavenger spends 1 grit point to perform a _change out,_ she can either perform the _change
out_ as a **standard action** instead of a full-round action, or perform the _change out_ on a
firearm that isn't broken.

A gun scavenger can remove the broken condition from a single firearm she is currently wielding, as
long as that condition was gained by a firearm misfire. When she does, she can replace the broken
part with a specialized, short-lived component that does one of the following.

- Gives the firearm the [scatter](ref/misc/scatter) weapon quality
- Increases the damage dealt by the [pistol-whip](ref/deed/pistol-whip) deed by one die size
- Increases the firearm's range increment by 10 feet.

A firearm with such a modification increases its misfire chance cumulatively by 1 each time it is
fired until it misfires. When it does misfire, the effects of the temporary component are lost.

**Jury-Rig (Ex)**

**Gained:** At 7th Level

**Replaces:** Targeting deed

**Special:** Multiple uses of this ability don't stack with themselves.

**Standard:** A gun scavenger can adjust a firearm she is currently wielding to fire in an
unconventional way. She can spend 1 grit point to grant her firearm one of the following magic
weapon enhancements for 1 round per gunslinger level: [distance](ref/magic-enh/distance),
[flaming](ref/magic-enh/flaming), [glamered](ref/magic-enh/glamered-weapon), or
[thundering](ref/magic-enh/thundering). If she spends 2 grit points, she can instead grant the
firearm [flaming burst](ref/magic-enh/flaming-burst) or [stalking](ref/magic-enh/stalking).

**Arbitrary Aim (Ex)**

**Flavor:** A gun scavenger's attacks with firearms are difficult to predict.

**Gained:** At 2nd Level

**Passive:** When shooting a firearm at a creature that has a dodge or insight bonus to its Armor
Class, the gun scavenger treats the combined bonus as if it were 1 lower.

**Replaces:** Nimble

At 6th level: The reduction 2.

At 10th level: The reduction 3.

At 14th level: The reduction 4.

At 18th level: The reduction 5.
