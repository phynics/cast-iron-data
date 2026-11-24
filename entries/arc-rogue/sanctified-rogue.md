+++
id = "ref/arc-rogue/sanctified-rogue"
kind = "archetype"
title = "Sanctified Rogue"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Sanctified%20Rogue"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sanctified_rogue", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-combat"
page = "74"

[fields]
kind = "archetype"
features = [
  { anchor = "divine-purpose", level = 4 },
  { anchor = "divine-epiphany", level = 8 },
]
trades = [
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["divine-purpose"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["divine-epiphany"] },
]
+++

The sanctified rogue serves a higher purpose, acting as a representative of a church or cult, or
following the tenets of a specific faith or deity. While most sanctified rogues share the beliefs or
ideals of the religions they represent, not all of them are necessarily pious. A handful of
disreputable holy thieves serve purely as mercenaries. At the other end of spectrum, however, more
sanctified rogues adhere to the tenets of their faith with fanatical devotion. Regardless, all seem
blessed with the ability to call upon divine favor to aid them in times of need.

## Divine Purpose (Su) {#divine-purpose}

At 4th level, the favor of a deity or religious institution grants a special blessing on a
sanctified rogue, shoring up some of her weaknesses. She gains a +1 sacred bonus on Fortitude and
Will saving throws. This ability replaces uncanny dodge.

## Divine Epiphany (Su) {#divine-epiphany}

At 8th level, once per day, a sanctified rogue can peer into the immediate future and predict the
results of a specific action as if she had cast an _[augury](ref/spell/augury)_ spell. The caster
level of this spell is equal to the sanctified rogue's rogue class level. This ability replaces
improved uncanny dodge.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the sanctified rogue archetype: esoteric scholar, major
magic, and minor magic.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the sanctified rogue archetype: feat and skill
mastery.
