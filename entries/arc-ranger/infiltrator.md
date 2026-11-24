+++
id = "ref/arc-ranger/infiltrator"
kind = "archetype"
title = "Infiltrator"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Infiltrator"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "infiltrator", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "advanced-players-guide"
page = "125"

[fields]
kind = "archetype"
features = [
  { anchor = "adaptation", level = 3 },
  { anchor = "aberration" },
  { anchor = "animal" },
  { anchor = "construct" },
  { anchor = "dragon" },
  { anchor = "fey" },
  { anchor = "humanoid-aquatic" },
  { anchor = "humanoid-dwarf" },
  { anchor = "humanoid-elf" },
  { anchor = "humanoid-giant" },
  { anchor = "humanoid-gnoll" },
  { anchor = "humanoid-gnome" },
  { anchor = "humanoid-goblinoid" },
  { anchor = "humanoid-halfling" },
  { anchor = "humanoid-human" },
  { anchor = "humanoid-orc" },
  { anchor = "humanoid-reptilian" },
  { anchor = "magical-beast" },
  { anchor = "monstrous-humanoid" },
  { anchor = "ooze" },
  { anchor = "outsider" },
  { anchor = "plant" },
  { anchor = "undead" },
  { anchor = "vermin" },
]
trades = [
  { replaces = "Favored terrain", feature = "favored-terrain", by = ["adaptation"] },
]
+++

Some rangers study their _favored enemies_ and learn their ways, applying this knowledge to their
own abilities and using their foes' strengths against them. Infiltrators are willing to walk a mile
in an enemy's shoes so as to learn eveything there is to know about their foes in order to more
effectively hunt and kill them.

## Adaptation (Ex) {#adaptation}

At 3rd level, an infiltrator learns how to copy the unusual abilities of his prey. He chooses one
type of creature he has selected as a favored enemy, such as "aberrations." The ranger selects one
ability or feat from the adaptation list for that type (see below). A ranger can use adaptations for
10 minutes per day per ranger level he possesses. This duration does not need to be consecutive, but
it must be used in 10-minute increments. If the adaptation requires the ranger to make a more
specific choice (such as what skill to use with [Skill Focus](ref/feat/skill-focus)), this choice is
permanent and cannot be changed.

At 8th, 13th, and 15th-level, the ranger chooses another one of his favored enemy types and selects
one adaptation from that type's list, as well as an additional adaptation from any one list of a
creature type he's selected (including the one just chosen, if so desired). The infiltrator can only
use one adaptation at a time. This class ability replaces favored terrain.

## Aberration {#aberration}

[amphibious](ref/umr/amphibious), [darkvision](ref/rule/darkvision) 60 ft.,
[Iron Will](ref/feat/iron-will), natural armor +2.

## Animal {#animal}

climb 15 ft., [darkvision](ref/rule/darkvision) 60 ft., [Great Fortitude](ref/feat/great-fortitude),
[Lightning Reflexes](ref/feat/lightning-reflexes), [low-light vision](ref/rule/low-light-vision),
natural armor (+2), swim 15 ft.

## Construct {#construct}

[darkvision](ref/rule/darkvision) 60 ft., Great Fortitude, Lightning Reflexes,
[low-light vision](ref/rule/low-light-vision).

## Dragon {#dragon}

[darkvision](ref/rule/darkvision) 60 ft., Great Fortitude, Iron Will, Lightning Reflexes,
[low-light vision](ref/rule/low-light-vision), [Lunge](ref/feat/lunge).

## Fey {#fey}

Iron Will, Lightning Reflexes, [low-light vision](ref/rule/low-light-vision).

## Humanoid (aquatic) {#humanoid-aquatic}

[low-light vision](ref/rule/low-light-vision), natural armor +2, [darkvision](ref/rule/darkvision),
swim 15 ft.

## Humanoid (dwarf) {#humanoid-dwarf}

[darkvision](ref/rule/darkvision) 60 ft., [defensive training](ref/race/dwarf), greed, hatred,
hardy, slow and steady, stability, stonecunning, weapon familiarity.

## Humanoid (elf) {#humanoid-elf}

[elf](ref/race/half-elf) blood, [low-light vision](ref/rule/low-light-vision), [elven](ref/race/elf)
immunities, elven magic, keen senses, Skill Focus (choose one skill), weapon familiarity.

## Humanoid (giant) {#humanoid-giant}

[low-light vision](ref/rule/low-light-vision), Lunge, natural armor +2, [resist](ref/umr/resistance)
energy 10 (choose cold, electricity, or fire), [Throw Anything](ref/feat/throw-anything).

## Humanoid (gnoll) {#humanoid-gnoll}

[darkvision](ref/rule/darkvision) 60 ft.,
[Exotic Weapon Proficiency](ref/feat/exotic-weapon-proficiency)
([dire flail](ref/eq-weapon/dire-flail)), natural armor +2.

## Humanoid (gnome) {#humanoid-gnome}

defensive training, [gnome](ref/race/gnome) magic, hatred, illusion resistance, keen senses,
low-light vision, obsessive, weapon familiarity.

## Humanoid (goblinoid) {#humanoid-goblinoid}

[darkvision](ref/rule/darkvision) 60 ft., goblin fast, Skill Focus (Stealth), natural armor (+2).

## Humanoid (halfling) {#humanoid-halfling}

fearless, [halfling](ref/race/halfling) luck, keen senses, sure-footed, weapon familiarity.

## Humanoid (human) {#humanoid-human}

Great Fortitude, Iron Will, Lightning Reflexes, Skill Focus (choose one skill).

## Humanoid (orc) {#humanoid-orc}

[darkvision](ref/rule/darkvision) 60 ft., [ferocity](ref/umr/ferocity),
[intimidating](ref/race/half-orc), orc blood, weapon familiarity.

## Humanoid (reptilian) {#humanoid-reptilian}

[darkvision](ref/rule/darkvision) 60 ft., kobold fast (as goblin fast),
[lizardfolk](ref/monster/lizardfolk)
[hold breath](ref/carried/bestiary/rules/universal-monster-rules/hold-breath), natural armor +2,
Skill Focus (choose Acrobatics, Perception, or Stealth).

## Magical Beast {#magical-beast}

[darkvision](ref/rule/darkvision) 60 ft., Great Fortitude,
[low-light vision](ref/rule/low-light-vision), natural armor +2.

## Monstrous Humanoid {#monstrous-humanoid}

[darkvision](ref/rule/darkvision) 60 ft., Lightning Reflexes,
[low-light vision](ref/rule/low-light-vision), natural armor +2.

## Ooze {#ooze}

acid resistance 10, Great Fortitude, Iron Will, Skill Focus (choose Climb, Escape Artist, or
Perception).

## Outsider {#outsider}

[darkvision](ref/rule/darkvision) 60 ft., energy resistance 5 (choose one type of energy from acid,
cold, electricity, or fire), Great Fortitude, Iron Will, Lightning Reflexes.

## Plant {#plant}

[low-light vision](ref/rule/low-light-vision), Great Fortitude, Iron Will.

## Undead {#undead}

[darkvision](ref/rule/darkvision) 60 ft., Great Fortitude, Iron Will, natural armor (+2). Skill
Focus (Stealth).

## Vermin {#vermin}

climb 15 ft., [darkvision](ref/rule/darkvision) 60 ft., Great Fortitude, Iron Will, swim 15 ft.
