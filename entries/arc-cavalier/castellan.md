+++
id = "ref/arc-cavalier/castellan"
kind = "archetype"
title = "Castellan"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Castellan"
source_ids = ["melee-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "castellan", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "melee-tactics-toolbox"
page = "9"

[fields]
kind = "archetype"
features = [
  { anchor = "castle-defender", level = 1 },
  { anchor = "castle-lore", level = 3 },
  { anchor = "guard-companion", level = 4 },
  { anchor = "mighty-defense", level = 11 },
  { anchor = "defending-challenge", level = 12 },
  { anchor = "supreme-defense", level = 20 },
]
trades = [
  { replaces = "Mount", feature = "mount", by = ["castle-defender"] },
  { replaces = "Cavalier's charge", feature = "cavalier-s-charge", by = ["castle-lore"] },
  { replaces = "Expert trainer", feature = "expert-trainer", by = ["guard-companion"] },
  { replaces = "Mighty charge", feature = "mighty-charge", by = ["mighty-defense"] },
  { replaces = "Demanding challenge", feature = "demanding-challenge", by = ["defending-challenge"] },
  { replaces = "Supreme charge", feature = "supreme-charge", by = ["supreme-defense"] },
]
+++

A castellan is a cavalier who dedicates himself to the defense of a castle or walled city. Though
not as celebrated as the cavaliers who ride forth to take on distant foes, the castellan is no less
brave or important, for the castellan and his allies are the last line of defense for those who
depend on the fortification for protection.

## Castle Defender {#castle-defender}

At 1st level, a castellan gains a +1 bonus to Armor Class and an additional +1 bonus on attack rolls
when he is on [higher ground](ref/rule/combat-modifiers). He also gains an additional +1 bonus to
Armor Class and on Reflex saves when he has [cover](ref/rule/cover) other than soft cover from other
creatures. At 6th level, a castellan gains [evasion](ref/ability/evasion) (as a rogue) when he has
cover (but not soft cover) against the source of the attack. At 11th level, these bonuses increase
by 1. At 16th level, he gains [improved evasion](ref/talent/improved-evasion) instead of evasion.
Both the evasion and improved evasion abilities work even when the castellan wears medium or heavy
armor. This ability replaces mount.

## Castle Lore {#castle-lore}

At 3rd level, the castellan gains a +2 bonus on initiative checks and Knowledge (engineering),
Knowledge (local), Knowledge (nobility), Perception, and Stealth checks when he is in urban terrain,
including fortifications. A castellan in an urban environment can always act in a surprise round,
though he remains [flat-footed](ref/rule/flat-footed) until he acts. At 8th level and every 5 levels
thereafter, the castellan's bonuses on skill and initiative checks increase by 2. This ability
replaces cavalier's charge.

## Guard Companion {#guard-companion}

At 4th level, the castellan forms a bond with an [animal companion](ref/sidekick/animal-companion)
that serves as a guard. While most castellans select birds or canines, the castellan can choose any
animal companions available to [rangers](ref/class/ranger). This ability functions like the
[druid](ref/class/druid) nature bond ability, except that the castellan's effective druid level is
equal to his cavalier level - 3 and his animal companion doesn't gain the share spells special
ability. This ability replaces expert trainer.

## Mighty Defense {#mighty-defense}

At 11th level, when the castellan [readies an action](ref/rule/ready) to make a melee attack against
a creature that is not yet adjacent to him, he doubles the threat range of any melee weapons wielded
during the attack. This increase doesn't stack with other effects that increase the threat range of
his weapons. In addition, the cavalier can attempt a free [dirty trick](ref/rule/dirty-trick),
[disarm](ref/rule/disarm), [sunder](ref/rule/sunder), or [trip](ref/rule/trip) combat maneuver if
his readied attack is successful. This free combat maneuver doesn't provoke an attack of
opportunity. This ability replaces mighty charge.

## Defending Challenge {#defending-challenge}

At 12th level, the castellan takes no penalty to Armor Class when using his challenge ability. This
ability replaces demanding challenge.

## Supreme Defense {#supreme-defense}

At 20th level, whenever the castellan readies an action to make a melee attack against a creature
that is not yet adjacent to him, his readied attack deals double the normal amount of damage (or
triple the damage if using a [brace](ref/misc/brace) weapon against a charge). In addition, if the
cavalier confirms a critical hit on the readied attack, the target is [stunned](ref/misc/stunned)
for 1d4 rounds. A successful Will save (DC = 10 + the cavalier's class level + the cavalier's
Strength modifier) reduces this to being [staggered](ref/misc/staggered) for 1d4 rounds. This
ability replaces supreme charge.
