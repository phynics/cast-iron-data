+++
id = "ref/arc-alchemist/horticulturist"
kind = "archetype"
title = "Horticulturist"
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
replaces = ["Mutagen, 2nd-level discovery", "Poison resistance", "poison use", "poison immunity", "The discovery gained at 4th level", "Persistent mutagen"]
alters = ["Bombs"]
+++

A horticulturist spends his time cultivating plants and plant creatures, allowing him to experiment
with strange and wondrous herbal concoctions.

**Seed Extract**

**Gained:** At 1st Level

**Passive:** A horticulturist adds _summon nature's ally I-VI_ as 1st- through 6th-level extracts,
respectively, to his class extract list. For example, he automatically adds
[summon nature's ally I](ref/spell/summon-natures-ally-1) to his formula book at 1st level and adds
the next higher-level spell to his formula book each time he gains the ability to use extracts of
that level. The horticulturist uses these special extracts to plant a seed that grows into a
creature, bypassing the restriction for single target or personal effects. Using these extracts
takes 1 round (as the spell's normal casting time), and the creature summoned must be placed in a
space adjacent to the horticulturist. The horticulturist can use these extracts to summon only
animals and plants on the appropriate summon nature's ally list.

**Replaces:** Mutagen, 2nd-level discovery

**Special:** Creatures the horticulturist summons with these extracts become creatures with the
plant type (gaining [low-light vision](ref/rule/low-light-vision) and immunity to mind-affecting,
paralysis, poison, polymorph, sleep, and stunning effects) rather than their normal type, but their
attack bonuses, Hit Dice, saving throws, and skills don't change. A horticulturist can't choose
mutagen discoveries.

**Herbal Bombs (Su)**

**Ability:** A horticulturist's bombs lack the power of a traditional alchemist's but can be
fine-tuned in ways normal alchemist explosives cannot. The horticulturist's bombs deal 1d4 points of
damage (instead of 1d6), plus 1d4 points of damage for every 2 alchemist levels beyond 1st. When the
horticulturist creates a bomb, he can formulate it to affect plants and other creatures normally,
affect only plant creatures, or affect only creatures not of the plant type.

**Alters:** Bombs

**Gained:** At 1st Level

**Plant Voice (Ex, Su)**

**At 10th Level:** He can speak to plants as a constant
[speak with plants](ref/spell/speak-with-plants) spell (this ability is supernatural).

**Gained:** At 2nd Level

**Passive:** A horticulturist gains a +2 bonus on Knowledge (nature) and Survival checks.

**Replaces:** Poison resistance, poison use, poison immunity

**Plant Familiar (Ex)**

**Ability:** A horticulturist creates a Diminutive or Tiny alchemical plant creature that vaguely
resembles a kind of animal suitable for a familiar (such as a cat) and acts as his
[familiar](ref/ability/familiars), granting the horticulturist a skill bonus, the
[Alertness](ref/feat/alertness) feat, and so on. The plant familiar has all the abilities of the
animal it resembles (for example, a bat-like plant familiar can fly) but is treated as a creature of
the plant type and has familiar abilities based on the horticulturist's alchemist level (though some
familiar abilities may be useless to the horticulturist).

**Gained:** At 4th Level

**Replaces:** The discovery gained at 4th level

**Special:** An alchemist's extracts and mutagens are considered spells for the purposes of familiar
abilities like _share spells_ or _deliver touch spells._ If a plant familiar is lost or dies, it can
be replaced 1 week later through a specialized procedure that costs 200 gp per alchemist level the
horticulturist has. The ritual takes 8 hours to complete.

**Fury of Nature (Sp)**

**Ability:** A horticulturist's connection with nature allows him to bring down nature's fury on his
opponents. He can cast one of the following spells, chosen at the time of casting, once per day as a
spell-like ability: [call lightning storm](ref/spell/call-lightning-storm),
[eagle aerie](ref/spell/eagle-aerie), or [liveoak](ref/spell/liveoak).

**Gained:** At 14th Level

**Replaces:** Persistent mutagen
