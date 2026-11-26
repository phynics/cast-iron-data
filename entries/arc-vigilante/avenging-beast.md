+++
id = "ref/arc-vigilante/avenging-beast"
kind = "archetype"
title = "Avenging Beast"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Avenging%20Beast"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "avenging_beast", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "96"

[fields]
kind = "archetype"
features = [
  { anchor = "animal-mask", level = 1 },
  { anchor = "spellcasting" },
  { anchor = "patron-spells", level = 1 },
  { anchor = "wild-shape", level = 5 },
]
trades = [
  { replaces = "Vigilante talents gained at 4th, 8th, 10th, 14th, and 16th level", feature = "vigilante-talent", levels = [4, 8, 10, 14, 16], by = ["spellcasting"] },
  { replaces = "Vigilante specialization", feature = "vigilante-specialization", by = ["patron-spells"] },
  { replaces = "Startling appearance", feature = "startling-appearance", by = ["wild-shape"] },
  { replaces = "frightening appearance", feature = "frightening-appearance", by = ["wild-shape"] },
  { replaces = "stunning appearance", feature = "stunning-appearance", by = ["wild-shape"] },
  { alters = "Skill ranks per level" },
  { alters = "Dual identity", feature = "dual-identity", by = ["animal-mask"] },
  { alters = "Class skills" },
]
+++

Some vigilantes turn to natural traditions and supernatural forces to transform into beasts,
unleashing a primal fury on their foes before returning to an ordinary guise.

## Class Skills {#class-skills}

An avenging beast gains Knowledge (nature) and Spellcraft as class skills, but does not gain Disable
Device, Knowledge (engineering), Perform, and Sleight of Hand as class skills.

This alters the vigilante's class skills.

## Skill Ranks per Level {#skill-ranks-per-level}

An avenging beast gains a number of skill ranks equal to 4 + his Intelligence modifier at each
level, instead of 6 + his Intelligence modifier.

This alters the vigilante's skill ranks per level.

## Animal Mask (Ex) {#animal-mask}

An avenging beast gains an ornate animal-headed mask that is a focus for his power and must be worn
when assuming his vigilante identity. This mask symbolizes one specific animal, and the animal
cannot be changed once chosen. Without this mask, an avenging beast cannot assume his vigilante
identity. An avenging beast who loses his mask can replace it after 1 week through a specialized
ritual that takes 8 hours to complete and costs 200 gp per avenging beast level.

This alters dual identity.

## Spellcasting {#spellcasting}

An avenging beast casts divine spells as a [hunter](ref/class/hunter) and uses the hunter's spell
list.

This replaces the vigilante talents gained at 4th, 8th, 10th, 14th, and 16th level.

## Patron Spells {#patron-spells}

An avenging beast selects a patron from the witch patron list and adds the patron bonus spells to
his spell list (up to 6th-level spells). Patron spells of 7th level or higher are not counted as
being on the avenging beast's spell list.

This replaces vigilante specialization.

## Wild Shape (Su) {#wild-shape}

At 5th level, when in his vigilante identity, the avenging beast gains the ability to take on the
shape of the animal represented by his animal mask. This ability functions identically to the
[druid's](ref/class/druid) wild shape ability, except the ability does not improve beyond
functioning as _[beast shape I](ref/spell/beast-shape-1)_. The avenging beast treats his vigilante
level as his druid level for the purposes of this ability. An avenging beast can use wild shape once
per day at 5th level and one additional time per day at 7th level and every 2 levels thereafter, for
a total of eight times per day at 19th level.

This replaces startling appearance, frightening appearance, and stunning appearance.
