+++
id = "ref/arc-fighter/cad"
kind = "archetype"
title = "Cad"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Cad"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cad", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "ultimate-combat"
page = "45"

[fields]
kind = "archetype"
features = [
  { anchor = "skills" },
  { anchor = "dirty-maneuvers", level = 2 },
  { anchor = "catch-off-guard", level = 3 },
  { anchor = "payback", level = 5 },
  { anchor = "deadly-surprise", level = 7 },
  { anchor = "razor-sharp-chair-leg", level = 9 },
  { anchor = "craven-combatant", level = 11 },
  { anchor = "sweeping-prank", level = 13 },
  { anchor = "treacherous-blow", level = 15 },
  { anchor = "ultimate-payback", level = 20 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["dirty-maneuvers"] },
  { replaces = "Armor training 1", feature = "armor-training", levels = [3], by = ["catch-off-guard"] },
  { replaces = "Weapon training 1, 3, and 4", feature = "weapon-training", levels = [5, 13, 17], by = ["payback"] },
  { replaces = "Armor training 2", feature = "armor-training", levels = [7], by = ["deadly-surprise"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["razor-sharp-chair-leg"] },
  { replaces = "Armor training 3", feature = "armor-training", levels = [11], by = ["craven-combatant"] },
  { replaces = "Weapon training 3 and 4", by = ["sweeping-prank"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["treacherous-blow"] },
  { replaces = "Weapon mastery", feature = "weapon-mastery", by = ["ultimate-payback"] },
]
+++

In combat, most fighters have some sort of code of honor. Some believe that one should not kick
enemies when they are down, or should limit use of other such dirty tricks to the most dire of
circumstances. The cad places no such limitations on himself. Battles are for winning, and anything
that gives the cad the upper hand against his enemies is a legitimate tactic. No trick is too
treacherous if it leads to victory.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A cad is not proficient with medium armor, heavy armor, or tower shields.

## Skills {#skills}

Acrobatics (Dex), Bluff (Cha), Escape Artist (Dex), Sleight of Hand (Dex), and Stealth (Dex) are
class skills for a cad.

## Dirty Maneuvers (Ex) {#dirty-maneuvers}

At 2nd level, a cad becomes skilled at deceiving and discomfiting his opponents. The cad gains a +1
bonus on [disarm](ref/rule/disarm), [dirty trick](ref/rule/dirty-trick), and [steal](ref/rule/steal)
combat maneuver checks. The cad also gains a +1 bonus to CMD when attacked with the disarm, dirty
trick, and steal combat maneuvers. These bonuses increase by 1 for every four levels after 2nd (to a
maximum of +5 at 18th level). This ability replaces bravery.

## Catch Off-Guard {#catch-off-guard}

At 3rd level, the cad gains the [Catch Off-Guard](ref/feat/catch-off-guard) feat. This ability
replaces armor training 1.

## Payback (Ex) {#payback}

At 5th level, a cad gains a +1 bonus on attack and damage rolls against any creature that has
attacked the cad since the beginning of his last turn. This bonus increases by +1 for every four
levels beyond 5th (to a maximum of +4 at 17th level). This ability replaces weapon training 1, 3,
and 4.

## Deadly Surprise (Ex) {#deadly-surprise}

At 7th level, when a cad hits an opponent that is denied its Dexterity bonus to AC against him with
a weapon or unarmed attack, he may attempt a dirty trick combat maneuver as an immediate action as
part of the attack. This ability replaces armor training 2.

## Razor-Sharp Chair Leg (Ex) {#razor-sharp-chair-leg}

At 9th level, as a swift action, a cad may alter the type of damage dealt by an
[improvised weapon](ref/misc/improvised-weapons) to bludgeoning, piercing, or slashing damage. In
addition, the cad has a critical threat range of 19–20/×2 with any improvised melee weapon. This
ability replaces weapon training 2.

## Craven Combatant (Ex) {#craven-combatant}

At 11th level, when [fighting defensively](ref/misc/fighting-defensively) or using
[Combat Expertise](ref/feat/combat-expertise) or [total defense](ref/misc/total-defense), a cad
cannot be [flanked](ref/rule/flanking) except by a rogue or ninja whose level is four or more higher
than the cad's fighter level. This ability replaces armor training 3.

## Sweeping Prank (Ex) {#sweeping-prank}

At 13th level, as a standard action, a cad can use a dirty trick maneuver against any two adjacent
opponents that he can reach, making a separate combat maneuver check against each opponent. He must
use the same dirty trick maneuver against each opponent.

At 17th level, the cad can use this ability as a full-round action to attempt a dirty trick maneuver
against a number of enemies equal to 2 + his Dexterity bonus (if any). This ability replaces weapon
training 3 and 4.

## Treacherous Blow (Ex) {#treacherous-blow}

At 15th level, when a cad confirms a critical hit, he can attempt a dirty trick combat maneuver as
part of that attack as an immediate action. This ability replaces armor training 4.

## Ultimate Payback (Ex) {#ultimate-payback}

At 20th level, any critical threats a cad makes against an opponent that has attacked him since the
beginning of his last turn are automatically confirmed. This ability replaces weapon mastery.
