+++
id = "ref/arc-alchemist/horticulturist"
kind = "archetype"
title = "Horticulturist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Horticulturist"
source_ids = ["ultimate-wilderness", "heroes-of-the-wild"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "horticulturist", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "35"
[[sources]]
publication = "heroes-of-the-wild"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "seed-extract", level = 1 },
  { anchor = "herbal-bombs" },
  { anchor = "plant-voice", level = 2 },
  { anchor = "plant-familiar", level = 4 },
  { anchor = "fury-of-nature", level = 14 },
]
trades = [
  { replaces = "Mutagen", feature = "mutagen", by = ["seed-extract"] },
  { replaces = "Discovery normally gained at 2nd level", feature = "discovery", levels = [2], by = ["seed-extract"] },
  { replaces = "Poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["plant-voice"] },
  { replaces = "poison use", feature = "poison-use", by = ["plant-voice"] },
  { replaces = "poison immunity", feature = "poison-resistance", levels = [10], by = ["plant-voice"] },
  { replaces = "The discovery gained at 4th level", feature = "discovery", levels = [4], by = ["plant-familiar"] },
  { replaces = "Persistent mutagen", feature = "persistent-mutagen", by = ["fury-of-nature"] },
  { alters = "Bombs", feature = "bomb", by = ["herbal-bombs"] },
]
+++

A horticulturist spends his time cultivating plants and plant creatures, allowing him to experiment
with strange and wondrous herbal concoctions.

## Seed Extract {#seed-extract}

At 1st level, a horticulturist adds _[summon nature's ally I](ref/spell/summon-natures-ally-1)–VI_
as 1st-through 6th-level extracts, respectively, to his class extract list. For example, he
automatically adds _summon nature's ally I_ to his formula book at 1st level and adds the next
higher-level spell to his formula book each time he gains the ability to use extracts of that level.
The horticulturist uses these special extracts to plant a seed that grows into a creature, bypassing
the restriction for single target or personal effects. Using these extracts takes 1 round (as the
spell's normal casting time), and the creature summoned must be placed in a space adjacent to the
horticulturist. The horticulturist can use these extracts to summon only animals and plants on the
appropriate _summon nature's ally_ list. Creatures the horticulturist summons with these extracts
become creatures with the plant type (gaining [low-light vision](ref/rule/low-light-vision) and
immunity to mind-affecting, paralysis, poison, polymorph, sleep, and stunning effects) rather than
their normal type, but their attack bonuses, Hit Dice, saving throws, and skills don't change.

This replaces the mutagen class feature and the discovery normally gained at 2nd level. A
horticulturist can't choose mutagen discoveries.

## Herbal Bombs (Su) {#herbal-bombs}

A horticulturist's bombs lack the power of a traditional alchemist's but can be fine-tuned in ways
normal alchemist explosives cannot. The horticulturist's bombs deal 1d4 points of damage (instead of
1d6), plus 1d4 points of damage for every 2 alchemist levels beyond 1st. When the horticulturist
creates a bomb, he can formulate it to affect plants and other creatures normally, affect only plant
creatures, or affect only creatures not of the plant type.

This alters the bomb class feature.

## Plant Voice (Ex, Su) {#plant-voice}

At 2nd level, a horticulturist gains further knowledge about plants, and he eventually learns to
speak with them. He gains a +2 bonus on Knowledge (nature) and Survival checks, and at 10th level,
he can speak to plants as a constant _[speak with plants](ref/spell/speak-with-plants)_ spell (this
ability is supernatural).

This replaces poison resistance, poison use, and poison immunity.

## Plant Familiar (Ex) {#plant-familiar}

At 4th level, a horticulturist creates a Diminutive or Tiny alchemical plant creature that vaguely
resembles a kind of animal suitable for a [familiar](ref/ability/familiars) (such as a cat) and acts
as his familiar, granting the horticulturist a skill bonus, the [Alertness](ref/feat/alertness)
feat, and so on. The plant familiar has all the abilities of the animal it resembles (for example, a
bat-like plant familiar can fly) but is treated as a creature of the plant type and has familiar
abilities based on the horticulturist's alchemist level (though some familiar abilities may be
useless to the horticulturist). An alchemist's extracts and mutagens are considered spells for the
purposes of familiar abilities like share spells or deliver touch spells. If a plant familiar is
lost or dies, it can be replaced 1 week later through a specialized procedure that costs 200 gp per
alchemist level the horticulturist has. The ritual takes 8 hours to complete.

This replaces the discovery gained at 4th level.

## Fury of Nature (Sp) {#fury-of-nature}

At 14th level, a horticulturist's connection with nature allows him to bring down nature's fury on
his opponents. He can cast one of the following spells, chosen at the time of casting, once per day
as a spell-like ability: _[call lightning storm](ref/spell/call-lightning-storm)_,
_[eagle aerie](ref/spell/eagle-aerie)_, or _[liveoak](ref/spell/liveoak)_.

This replaces persistent mutagen.
