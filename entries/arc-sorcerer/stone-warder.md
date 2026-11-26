+++
id = "ref/arc-sorcerer/stone-warder"
kind = "archetype"
title = "Stone Warder"
aon = "ArchetypeDisplay.aspx?FixedName=Sorcerer%20Stone%20Warder"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stone_warder", path = "json/archetypes_sorcerer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/sorcerer" },
]
[[sources]]
publication = "arcane-anthology"
page = "29"

[fields]
kind = "archetype"
features = [
  { anchor = "blood-of-the-earth" },
  { anchor = "power-of-stone" },
  { anchor = "rune-of-warding", level = 1 },
]
trades = [
  { replaces = "Eschew Materials", feature = "eschew-materials", by = ["rune-of-warding"] },
  { replaces = "The bloodline spell gained at 3rd level", feature = "bloodline", levels = [3], power = "bloodline spell", by = ["rune-of-warding"] },
  { replaces = "The bloodline feat gained at 7th level", feature = "bloodline", levels = [7], power = "bloodline feat", by = ["rune-of-warding"] },
]
+++

Stone warders have an innate ability to create runes that allow them to ward areas with magic traps
built from their spells. These sorcerers are most common among dwarves, but have been known to
appear among other races who have strong ties to earth, rock, stone, mountains, and the Darklands.

## Blood of the Earth {#blood-of-the-earth}

Stone warders must have a bloodline with strong ties to earth and rock. A stone warder must select
the deep earth, draconic (copper dragon only), elemental (earth only), orc (_Pathfinder Player
Companion: Orcs of Golarion_ 14), or shaitan bloodline.

## Power of Stone (Su) {#power-of-stone}

A stone warder draws power from natural rock, and gains a +1 bonus to her caster level when in
hills, mountains, or underground terrain. This bonus increases to +2 at 5th level, and by an
additional 1 every 5 sorcerer levels thereafter. However, this strong elemental tie prevents a stone
warder from casting spells that have the air, cold, electricity, fire, or water descriptor.

## Rune of Warding (Sp) {#rune-of-warding}

As a standard action, a stone warder can create a warding rune in any adjacent square. The stone
warder selects a sorcerer spell known that is at least 1 level lower than the highest-level spell
she can cast, and casts it as part of creating the [rune of warding](ref/spell/rune-of-warding). The
spell must have a casting time of 1 standard action or less, and it must target one or more
creatures. Rather than have its normal effect, the spell is stored in the rune. The first creature
to enter the square triggers the [rune of warding](ref/spell/rune-of-warding), and becomes the
target of the selected spell. Regardless of the number of targets the spell can normally affect, it
affects only the creature that triggers the rune.

The rune is invisible and lasts a number of rounds equal to the stone warder's level or until
discharged. If placed on a solid rock or stone surface, it instead lasts 1 minute per sorcerer level
the stone warder has or until discharged. The stone warder cannot create a
[rune of warding](ref/spell/rune-of-warding) in a square occupied by an existing
[rune of warding](ref/spell/rune-of-warding) or another creature. The rune counts as a spell of the
same level as the spell stored within it for the purposes of dispelling. It is considered a magic
trap and can be discovered with a successful Perception check (DC = 25 + the level of the stored
spell) and disarmed with a successful Disable Device check (DC = 25 + the level of the stored
spell). The stone warder can use this ability a number of times per day equal to 3 + her Charisma
modifier.

This ability replaces Eschew Materials, the bloodline spell gained at 3rd level, and the bloodline
feat gained at 7th level.
