+++
id = "ref/arc-druid/reincarnated-druid"
kind = "archetype"
title = "Reincarnated Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Reincarnated%20Druid"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reincarnated_druid", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-magic"
page = "39"

[fields]
kind = "archetype"
features = [
  { anchor = "mysterious-stranger", level = 2 },
  { anchor = "resist-death-s-touch", level = 4 },
  { anchor = "many-lives", level = 5 },
  { anchor = "wild-shape", level = 6 },
  { anchor = "cheat-death", level = 9 },
  { anchor = "tongue-of-the-sun-and-moon", level = 15 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["mysterious-stranger"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["resist-death-s-touch"] },
  { replaces = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["cheat-death"] },
  { replaces = "Timeless body", feature = "timeless-body", by = ["tongue-of-the-sun-and-moon"] },
]
+++

Spun off into the endless circle of life, a reincarnated druid is an embodiment of nature's eternal
renewal. She lives many lives and wanders the world devoid of attachments, a stranger to all yet one
with all life.

## Mysterious Stranger (Ex) {#mysterious-stranger}

At 2nd level, a reincarnated druid adds 1/2 her druid level to the DC of Sense Motive, Diplomacy,
and Knowledge checks to learn about her. This ability replaces woodland stride.

## Resist Death's Touch (Ex) {#resist-death-s-touch}

At 4th level, a reincarnated druid gains a +4 bonus on saving throws against death effects, energy
drain, and necromancy effects, and on stabilization checks when dying. This ability replaces resist
nature's lure.

## Many Lives (Ex) {#many-lives}

At 5th level, if a reincarnated druid is killed, she may automatically
_[reincarnate](ref/spell/reincarnate)_ (as the spell) 1 day later. The reincarnated druid appears in
a safe location within 1 mile of her previous body. At will for the next 7 days, she can sense the
presence of her remains as if using _[locate object](ref/spell/locate-object)_ as a
[spell-like ability](ref/umr/spell-like-abilities). If she is killed during these 7 days, she
remains dead and does not reincarnate. The many lives ability does not function if the reincarnated
druid is slain by a death effect. A reincarnated druid cannot be
[raised from the dead](ref/spell/raise-dead) or [resurrected](ref/spell/resurrection), though she
can be reincarnated.

## Wild Shape (Su) {#wild-shape}

A reincarnated druid gains this ability at 6th level, and it functions at her druid level - 2.

## Cheat Death (Ex) {#cheat-death}

At 9th level, once per day, a reincarnated druid may reroll a save against a death effect, energy
drain, or necromancy effect before the result of the roll is revealed, or reroll a failed
stabilization check while dying. She must take the result of the second roll, even if it is worse
than the original roll. This ability replaces venom immunity.

## Tongue of the Sun and Moon (Ex) {#tongue-of-the-sun-and-moon}

At 15th level, a reincarnated druid can speak with any living creature. This ability replaces
timeless body.
