+++
id = "ref/arc-shaman/unsworn-shaman"
kind = "archetype"
title = "Unsworn Shaman"
aon = "ArchetypeDisplay.aspx?FixedName=Shaman%20Unsworn%20Shaman"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unsworn_shaman", path = "json/archetypes_shaman.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shaman" },
]
[[sources]]
publication = "advanced-class-guide"
page = "112"

[fields]
kind = "archetype"
features = [
  { anchor = "minor-spirit", level = 1 },
  { anchor = "spirit-animal", level = 2 },
  { anchor = "wandering-spirit", level = 2 },
  { anchor = "spirit-magic", level = 2 },
]
trades = [
  { replaces = "Spirit", feature = "spirit", by = ["minor-spirit"] },
  { replaces = "Wandering hex", feature = "wandering-hex", by = ["wandering-spirit"] },
  { alters = "Hex", feature = "hex", by = ["minor-spirit"] },
  { alters = "Spirit animal", feature = "spirit-animal", by = ["spirit-animal"] },
  { alters = "Wandering spirit", feature = "wandering-spirit", by = ["wandering-spirit"] },
  { alters = "Spirit magic", feature = "spirit-magic", by = ["spirit-magic"] },
]
+++

An unsworn shaman never binds herself to one specific spirit, always making new deals as she deems
necessary for the circumstances that she finds herself in. While this weakens the powers she can
access from any one spirit, it gives her access to a broader overall range of abilities.

## Minor Spirit (Su) {#minor-spirit}

At 1st level, the unsworn shaman also forms a temporary bond with a minor spirit each day, granting
her access to a shaman or witch hex of her choosing, but not a major hex or a grand hex. She must
make this selection each day when she prepares her spells for the day. Until she changes the minor
spirit, she continues to have access to the shaman or witch hex. At 2nd level, she can instead
select a hex from one of her wandering spirits selected for that day. If she selects a witch hex,
she treats her shaman level as her witch level, and uses her Wisdom in place of her Intelligence for
the purpose of that hex.

She can make temporary bonds with two minor spirits (thus gaining two hexes) at 4th level, and with
one additional minor spirit (and hex) every 4 levels thereafter. This ability replaces spirit and
alters hex.

## Spirit Animal {#spirit-animal}

At 2nd level, an unsworn shaman's spirit animal gains the spirit animal bonus from one of her
wandering spirits (see below). This bonus can be changed each day when the shaman prepares spells,
but it must correspond to one of the shaman's wandering spirits. This ability alters spirit animal.

## Wandering Spirit (Su) {#wandering-spirit}

At 2nd level, the unsworn shaman gains access to the wandering spirit class feature. At 10th level,
she gains the abilities listed in the greater version of her wandering spirit. At 18th level, she
gains the abilities listed in the true version of her wandering spirit.

Additionally, at 6th level, she also gains a second wandering spirit, gaining the abilities listed
in the greater version of that spirit at 14th level, and the abilities listed in the true version at
20th level. This ability alters wandering spirit and replaces wandering hex.

## Spirit Magic (Sp) {#spirit-magic}

The unsworn shaman gains this ability at 2nd level rather than at 1st. This ability alters spirit
magic.
