+++
id = "ref/arc-slayer/bloody-jake"
kind = "archetype"
title = "Bloody Jake"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Bloody%20Jake"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bloody_jake", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "horror-adventures"
page = "66"

[fields]
kind = "archetype"
features = [
  { anchor = "favored-terrain", level = 1 },
  { anchor = "cruel-tricks" },
  { anchor = "distant-voices", level = 1 },
  { anchor = "lose-your-way", level = 4 },
  { anchor = "something-s-not-right", level = 8 },
  { anchor = "the-woods-have-eyes", level = 12 },
  { anchor = "poor-study", level = 5 },
  { anchor = "sadistic-snare", level = 6 },
  { anchor = "cruel-trick", level = 11 },
  { anchor = "woodland-shortcut", level = 13 },
]
trades = [
  { replaces = "Proficiency in medium armor", feature = "weapon-and-armor-proficiencies", power = "medium armor", by = ["favored-terrain"] },
  { replaces = "shields", feature = "weapon-and-armor-proficiencies", power = "shields", by = ["favored-terrain"] },
  { replaces = "The 1st-level studied target", feature = "studied-target", levels = [1], by = ["the-woods-have-eyes"] },
  { replaces = "slayer talents gained at 4th, 8th, 12th, and 16th level", feature = "slayer-talents", levels = [4, 8, 12, 16], by = ["the-woods-have-eyes"] },
  { replaces = "Slayer talent gained at 6th level", feature = "slayer-talents", levels = [6], by = ["sadistic-snare"] },
  { replaces = "Swift tracker", feature = "swift-tracker", by = ["cruel-trick"] },
  { replaces = "Slayer's advance", feature = "slayer-s-advance", by = ["woodland-shortcut"] },
  { alters = "Studied target", feature = "studied-target", by = ["poor-study"] },
]
+++

Bloody jakes are cruel backwoods folk who prey upon their country cousins while terrorizing
civilized people who venture into their rural range.

## Alignment {#alignment}

A bloody jake must be of an evil alignment. A bloody jake who becomes nonevil cannot gain new levels
as a slayer but retains all his class abilities.

## Favored Terrain (Ex) {#favored-terrain}

At 1st level, a bloody jake can select a type of terrain from the
[favored terrain](ref/ability/favored-terrain) table for [rangers](ref/class/ranger), though he is
restricted to cold, desert, forest, jungle, mountains, plains, and swamp. His bonuses when in this
terrain increase by 2 at 5th level and every 5 slayer levels thereafter, though he does not gain the
ability to select additional favored terrains unless he takes the
[terrain mastery](ref/talent/terrain-mastery) rogue talent.

This ability replaces the slayer's proficiency in medium armor and shields.

## Cruel Tricks {#cruel-tricks}

Bloody jakes use backwoods folk magic to confuse, terrify, and weaken their prey. A bloody jake can
use this ability a number of times per day equal to his slayer level + his Charisma modifier. He
gains the cruel tricks below at the indicated slayer levels.

## Distant Voices (Sp) {#distant-voices}

At 1st level, a bloody jake can cause his voice to seem to emanate from somewhere else, as per
[ventriloquism](ref/spell/ventriloquism). This ability doesn't take any other action to activate and
can be used as part of speaking (as a free action); it costs one use of cruel tricks to affect his
speech for 1 round.

## Lose Your Way (Sp) {#lose-your-way}

At 4th level, as a standard action, a bloody jake can spend one use of cruel tricks to cause a
creature that is within 30 feet and within the bloody jake's favored terrain to become disoriented,
taking a penalty on Survival checks equal to the bloody jake's slayer level and a -2 penalty on
saving throws against fear and illusions. This effect lasts for 1 hour per slayer level of the
bloody jake or for as long as the affected creature remains within the bloody jake's favored
terrain, whichever is shorter.

## Something's Not Right (Su) {#something-s-not-right}

At 8th level, as a move action, a bloody jake can spend one use of cruel tricks to cause all foes
within 30 feet to become [shaken](ref/misc/shaken) for 1 round. This is a fear effect that doesn't
increase in strength by applying other effects that cause creatures to become shaken. At 12th level,
he can use this ability as a swift action. At 16th level, a bloody jake can make any number of the
affected foes [frightened](ref/misc/frightened) for 1 round, though such foes receive a Will save
(DC = 10 + 1/2 the bloody jake's slayer level + his Charisma modifier) to negate the frightened
condition; even so, such a foe is still shaken.

## The Woods Have Eyes (Sp) {#the-woods-have-eyes}

At 12th level, a bloody jake in his favored terrain can spend one use of cruel tricks as a swift
action to gain [blindsense](ref/umr/blindsense) in a 30-foot radius for 1 round; this
[blindsense](ref/rule/blindsight-and-blindsense) is sound-based.

This replaces the 1st-level studied target and the slayer talents gained at 4th, 8th, 12th, and 16th
level.

## Poor Study (Ex) {#poor-study}

A bloody jake gains this ability at 5th level rather than 1st level, beginning with a bonus of +1 at
5th level and increasing by 1 for every 5 slayer levels thereafter. A bloody jake must be 11th level
to study an opponent as a move or swift action.

This ability alters studied target.

## Sadistic Snare (Ex) {#sadistic-snare}

At 6th level, a bloody jake gains [Learn Ranger Trap](ref/feat/learn-ranger-trap) as a bonus feat,
benefiting from it as if he were a ranger. He can expend two uses of his traps ability to add his
sneak attack damage to the trap's damage; any slayer talents or rogue talents he has that modify
sneak attack damage, such as [bleeding attack](ref/talent/bleeding-attack), also apply to sneak
attack damage dealt by his ranger traps.

This replaces the slayer talent gained at 6th level.

## Cruel Trick (Ex) {#cruel-trick}

At 11th level, a bloody jake can maim or humiliate his target with a sneak attack, substituting 1
point of [Dexterity or Charisma damage](ref/rule/ability-damage-drain) per die of sneak attack
damage forfeited. A successful Will save negates this ability damage (DC = 10 + 1/2 the bloody
jake's slayer level + his Charisma modifier).

This ability replaces swift tracker.

## Woodland Shortcut (Sp) {#woodland-shortcut}

At 13th level, a bloody jake can move with supernatural ease among the trees once per day, as if
using _[tree stride](ref/spell/tree-stride)_ with a caster level equal to his slayer level.

This ability replaces slayer's advance.
