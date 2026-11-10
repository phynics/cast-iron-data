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
replaces = ["Eschew Materials, 3rd-level bloodline spell, 7th-level bloodline feat"]
replaces_features = ["eschew-materials"]
+++

Stone warders have an innate ability to create runes that allow them to ward areas with magic traps
built from their spells. These sorcerers are most common among dwarves, but have been known to
appear among other races who have strong ties to earth, rock, stone, mountains, and the Darklands.

**Prerequisites:** [deep earth](ref/sorcbloodline/deep-earth),
[draconic](ref/sorcbloodline/draconic) (copper dragon only),
[elemental](ref/sorcbloodline/elemental) (earth only), [orc](ref/sorcbloodline/orc), or
[shaitan](ref/sorcbloodline/shaitan) bloodline

**Power of Stone (Su)**

**Flavor:** A stone warder draws power from natural rock.

**Passive:** When in hills, mountains, or underground terrain, a stone warden gets a bonus to her
caster level equal to 1 + [one-fifth](ref/misc/fractions-and-rounding) of her sorcerer level.

**Special:** This strong elemental tie prevents a stone warder from casting spells that have the
air, cold, electricity, fire, or water descriptor.

**Rune of Warding (Sp)**

**Replaces:** Eschew Materials, 3rd-level bloodline spell, 7th-level bloodline feat

**Special:** The stone warder cannot create a _[rune of warding](ref/spell/rune-of-warding)_ in a
square occupied by an existing _[rune of warding](ref/spell/rune-of-warding)_ or another creature.
The _rune_ counts as a spell of the same level as the spell stored within it for the purposes of
dispelling. It is considered a magic trap and can be discovered with a successful Perception check
(DC = 25 + the level of the stored spell) and disarmed with a successful Disable Device check (DC =
25 + the level of the stored spell).

**Standard:** A stone warder can create a _warding rune_ in any adjacent square. The stone warder
selects a sorcerer spell known that is at least 1 level lower than the highest-level spell she can
cast, and casts it as part of creating the _[rune of warding](ref/spell/rune-of-warding)._ The spell
must have a casting time of 1 standard action or less, and it must target one or more creatures.
Rather than have its normal effect, the spell is stored in the _rune._ The first creature to enter
the square triggers the _[rune of warding](ref/spell/rune-of-warding),_ and becomes the target of
the selected spell. Regardless of the number of targets the spell can normally affect, it affects
only the creature that triggers the _rune._

The _rune_ is invisible and lasts a number of rounds equal to the stone warder's level or until
discharged. If placed on a solid rock or stone surface, it instead lasts 1 minute per sorcerer level
the stone warder has or until discharged.

**Usage:** Charisma3 modifier times/day
