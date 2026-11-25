+++
id = "ref/arc-oracle/planar-oracle"
kind = "archetype"
title = "Planar Oracle"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Planar%20Oracle"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planar_oracle", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "ultimate-magic"
page = "59"

[fields]
kind = "archetype"
features = [
  { anchor = "recommended-mysteries" },
  { anchor = "revelations", level = 1 },
  { anchor = "planar-resistance", level = 3 },
  { anchor = "final-revelation", level = 20 },
]
trades = [
  { replaces = "Mystery bonus spells at these levels", feature = "mystery", power = "bonus spells" },
  { replaces = "3rd-level revelation", feature = "revelation", levels = [3], by = ["revelations"] },
  { replaces = "Final revelation of the oracle's mystery", feature = "final-revelation", by = ["final-revelation"] },
]
+++

A planar oracle has an affinity with one of the Outer Planes. She is at home on the multiple planes
of the Great Beyond, and can eventually become an outsider herself.

## Recommended Mysteries {#recommended-mysteries}

dark tapestry, flame, heavens, stone, waves, wind.

## Bonus Spells {#bonus-spells}

_endure elements_ (2nd), _elemental speech_ (4th), _tongues_ (6th), _planar adaptation_ (8th),
_plane shift_ (10th), _mass planar adaptation_ (12th), _shadow walk_ (14th), _etherealness_ (16th),
_gate_ (18th). These bonus spells replace the oracle's mystery bonus spells at these levels.

## Revelations {#revelations}

At 1st level, you must choose one Outer Plane with which you have an affinity. This choice cannot be
changed. A planar oracle must take the following revelation at 3rd level.

## Planar Resistance (Su) {#planar-resistance}

At 3rd level, you gain energy resistance 10 against one energy type associated with your chosen
plane. At 11th level, your energy resistance increases to 20.

## Final Revelation {#final-revelation}

At 20th level, you become an [extraplanar](ref/subtype/extraplanar) creature. Choose one outer
plane, such as Heaven or the Abyss. You gain superficial physical characteristics as appropriate to
natives of your chosen outer plane (see the _Pathfinder RPG Bestiary_). For example, if your chosen
plane is Heaven, you gain angelic features such as a halo and metallic skin. This change does not
alter your Hit Dice, hit points, saving throws, skill points, class skills, or proficiencies. Your
type changes to "[outsider](ref/type/outsider) (extraplanar)," except on your associated plane,
where your type is "outsider (native)." In addition, you gain immunity to your associated energy
type and gain [damage reduction](ref/rule/damage-reduction) 10/magic. Unlike other outsiders, you
can still be brought back from the dead as if you were a member of your previous creature type. This
replaces the final revelation of the oracle's mystery.
