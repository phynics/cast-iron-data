+++
id = "ref/arc-fighter/tactician"
kind = "archetype"
title = "Tactician"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Tactician"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tactician", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "ultimate-combat"
page = "47"

[fields]
kind = "archetype"
features = [
  { anchor = "strategic-training", level = 1 },
  { anchor = "tactical-awareness", level = 2 },
  { anchor = "tactician", level = 5 },
  { anchor = "cooperative-combatant", level = 11 },
  { anchor = "battle-insight", level = 15 },
]
trades = [
  { replaces = "The bonus fighter combat feat gained at 1st level", feature = "bonus-feats", levels = [1], by = ["strategic-training"] },
  { replaces = "Bravery", feature = "bravery", by = ["tactical-awareness"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["tactician"] },
  { replaces = "Armor training 3", feature = "armor-training", levels = [11], by = ["cooperative-combatant"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["battle-insight"] },
  { alters = "Proficiency with heavy armor", feature = "weapon-and-armor-proficiencies", power = "heavy armor" },
  { alters = "tower shields", feature = "weapon-and-armor-proficiencies", power = "shields" },
]
+++

While many fighters focus on the fundamentals of melee and ranged combat, there are those who are
trained to view the bigger picture on the battlefield. These fighters use their training and
tactical acumen to overcome challenges that would overwhelm mere brute strength and skill at arms.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A tactician is not proficient with heavy armor or tower shields.

## Strategic Training (Ex) {#strategic-training}

A tactician gains 4 skill points + a number of skill points equal to his Intelligence modifier at
each level, instead of the normal 2 skill points + Intelligence modifier at each level. Furthermore,
[Diplomacy](ref/skill/diplomacy) (Cha), [Knowledge (geography)](ref/skill/knowledge-geography)
(Int), [Knowledge (nobility)](ref/skill/knowledge-nobility) (Int),
[Linguistics](ref/skill/linguistics) (Int), and [Sense Motive](ref/skill/sense-motive) (Wis) are all
class skills for the tactician. This ability replaces the bonus fighter combat feat gained at 1st
level.

## Bonus Feats {#bonus-feats}

A tactician may choose [Skill Focus](ref/feat/skill-focus) or any teamwork feat, in addition to
combat feats, as bonus feats.

## Tactical Awareness (Ex) {#tactical-awareness}

At 2nd level, a tactician gains a +1 bonus on initiative checks. This bonus increases by +1 for
every four levels after 2nd level (to a maximum of +5 at 18th level). This ability replaces bravery.

## Tactician (Ex) {#tactician}

At 5th level, a tactician gains this ability as the [cavalier](ref/class/cavalier) class feature. He
may use this ability once per day at 5th level, plus one additional time for every five levels after
5th (to a maximum of four times at 20th level). If the tactician also has cavalier levels, these
levels stack for determining the number of uses per day, and he can take the better progression.
This ability replaces weapon training 1.

## Cooperative Combatant (Ex) {#cooperative-combatant}

At 11th level, when a tactician uses the [aid another](ref/rule/aid-another-2) special attack, he
may affect one additional ally per point of Intelligence bonus. For each ally that a tactician aids,
he can pick whether to grant that ally the +2 bonus on its next attack against the opponent or the
+2 bonus to AC against the opponent's next attack on that ally, and can grant different allies
different bonuses. This ability replaces armor training 3.

## Battle Insight (Ex) {#battle-insight}

At 15th level, as a swift action, a tactician can grant his Intelligence modifier as an insight
bonus on the attack rolls made by a single ally within line of sight that can both see and hear the
tactician. That ally gains the bonus until the end of the tactician's next turn. The tactician can
use this ability a number of times per day equal to 3 + his Intelligence modifier. This ability
replaces armor training 4.
