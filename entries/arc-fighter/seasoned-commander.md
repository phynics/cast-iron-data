+++
id = "ref/arc-fighter/seasoned-commander"
kind = "archetype"
title = "Seasoned Commander"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Seasoned%20Commander"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "seasoned_commander", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "villain-codex"
page = "164"

[fields]
kind = "archetype"
features = [
  { anchor = "strategic-training", level = 1 },
  { anchor = "tactician", level = 3 },
  { anchor = "inspiring-speech", level = 5 },
  { anchor = "inspire-greatness", level = 9 },
  { anchor = "greater-tactician", level = 11 },
  { anchor = "inspire-heroics", level = 15 },
  { anchor = "master-tactician", level = 17 },
]
trades = [
  { replaces = "Bonus fighter combat feat gained at 1st level", feature = "bonus-feats", levels = [1], by = ["strategic-training"] },
  { replaces = "proficiency with heavy armor", feature = "weapon-and-armor-proficiencies", power = "heavy armor", by = ["strategic-training"] },
  { replaces = "tower shields", feature = "weapon-and-armor-proficiencies", power = "shields", by = ["strategic-training"] },
  { replaces = "Armor training 1", feature = "armor-training", levels = [3], by = ["tactician"] },
  { replaces = "Weapon training 1 and 3", feature = "weapon-training", levels = [5, 13], by = ["inspiring-speech"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["inspire-greatness"] },
  { replaces = "Armor training 3", feature = "armor-training", levels = [11], by = ["greater-tactician"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["inspire-heroics"] },
  { replaces = "Weapon training 4", feature = "weapon-training", levels = [17], by = ["master-tactician"] },
  { alters = "Skill ranks per level", by = ["strategic-training"] },
  { alters = "class skills", by = ["strategic-training"] },
]
+++

The seasoned commander excels at leading troops through inspiration and the use of unit tactics.

## Strategic Training (Ex) {#strategic-training}

A seasoned commander gains 4 skill ranks + a number of skill ranks equal to his Intelligence
modifier at each level instead of the normal 2 skill ranks + Intelligence modifier at each level. A
seasoned commander adds [Diplomacy](ref/skill/diplomacy),
[Knowledge (geography)](ref/skill/knowledge-geography),
[Knowledge (nobility)](ref/skill/knowledge-nobility), [Linguistics](ref/skill/linguistics), and
[Sense Motive](ref/skill/sense-motive) to his list of class skills.

This alters the fighter's skill ranks per level and class skills, and replaces the bonus fighter
combat feat gained at 1st level and proficiency with heavy armor and tower shields.

## Tactician (Ex) {#tactician}

At 3rd level, a seasoned commander gains the [cavalier's](ref/class/cavalier) tactician class
feature, treating his fighter level as his cavalier level for the purposes of this ability.

This ability replaces armor training 1.

## Inspiring Speech (Ex) {#inspiring-speech}

At 5th level, a seasoned commander can give an inspiring speech as a standard action once per day.
If he does, all allies who can hear his speech gain the benefits of
[inspire courage](ref/performance/inspire-courage), granting bonuses 1 lower than those granted by a
bard of the seasoned commander's fighter level, lasting 1 round per fighter level + his Charisma
modifier (abilities that affect a bardic performance, such as
[Lingering Performance](ref/feat/lingering-performance), have no effect on this ability). At 7th
level, he can perform the speech as a move action, and at 13th level, he can perform the speech as a
swift action.

This ability replaces weapon training 1 and 3.

## Inspire Greatness (Ex) {#inspire-greatness}

At 9th level, a seasoned commander gains an additional daily use of his inspiring speech ability,
and he can also choose to use his inspiring speech to grant the effects of
[inspire greatness](ref/performance/inspire-greatness) to one ally (instead of inspire courage). For
every 2 levels a seasoned commander attains beyond 9th, he can target one additional ally while
using this ability (up to a maximum of six at 19th level). This ability functions in all other
respects like the seasoned commander's inspire courage ability. Whichever inspiring speech he
chooses to use, if the seasoned commander uses an inspiring speech before the duration of his
previous inspiring speech ends, the new inspiring speech replaces the old speech.

This ability replaces weapon training 2.

## Greater Tactician (Ex) {#greater-tactician}

At 11th level, the seasoned commander gains the [cavalier's](ref/class/cavalier) greater tactician
class feature, treating his fighter level as his cavalier level for the purposes of this ability.

This ability replaces armor training 3.

## Inspire Heroics (Ex) {#inspire-heroics}

At 15th level, a seasoned commander gains an additional daily use of his inspiring speech, and he
can also choose to use his inspiring speech to grant the effects of
[inspire heroics](ref/performance/inspire-heroics) to one ally (instead of inspire courage or
inspire greatness). For every 2 levels a seasoned commander attains beyond 15th, he can target one
additional ally while using this ability. This ability functions in all other respects like the
seasoned commander's inspire courage ability.

This ability replaces armor training 4.

## Master Tactician (Ex) {#master-tactician}

At 17th level, the seasoned commander gains the cavalier's master tactician class feature, treating
his fighter level as his cavalier level for the purposes of this ability.

This ability replaces weapon training 4.
