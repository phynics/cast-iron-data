+++
id = "ref/arc-warpriest/cult-leader"
kind = "archetype"
title = "Cult Leader"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Cult%20Leader"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cult_leader", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "advanced-class-guide"
page = "128"

[fields]
kind = "archetype"
features = [
  { anchor = "class-skills" },
  { anchor = "skill-ranks-per-level" },
  { anchor = "well-hidden", level = 1 },
  { anchor = "sneak-attack", level = 3 },
  { anchor = "enthrall", level = 4 },
  { anchor = "hide-in-plain-sight", level = 12 },
]
trades = [
  { replaces = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Focus weapon", feature = "focus-weapon", by = ["well-hidden"] },
  { replaces = "Bonus feats gained at 3rd, 9th, and 15th levels", feature = "bonus-feats", levels = [3, 9, 15], by = ["sneak-attack"] },
  { replaces = "Channel energy", feature = "channel-energy", by = ["enthrall"] },
  { replaces = "Bonus feat gained at 12th level", feature = "bonus-feats", levels = [12], by = ["hide-in-plain-sight"] },
]
+++

Referred to as fanatics, lunatics, or obsessives, cultists see themselves as genuine devotees of
their deity. And the hierarchs of those devotees, the cult leaders, are the most fanatical of them
all. Cult leaders are known for turning reasonable hearts toward corrupted teachings and striking at
those that get in the way of their agenda.

## Class Skills {#class-skills}

The cult leader's class skills are Acrobatics (Dex), Bluff (Cha), Climb (Str), Craft (Int),
Diplomacy (Cha), Disguise (Cha), Escape Artist (Dex), Heal (Wis), Intimidate (Cha), Knowledge
(local) (Int), Knowledge (religion) (Int), Perception (Wis), Profession (Wis), Sense Motive (Wis),
Slight of Hand (Dex), Spellcraft (Int), and Stealth (Dex). These skills replace the warpriest's
class skills.

## Skill Ranks per Level {#skill-ranks-per-level}

4 + Int modifier.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Cult leaders are proficient with all simple weapons, plus the
[hand crossbow](ref/eq-weapon/hand-crossbow), [rapier](ref/eq-weapon/rapier),
[sap](ref/eq-weapon/sap), [shortbow](ref/eq-weapon/shortbow), and
[short sword](ref/eq-weapon/short-sword), as well as the favored weapon of their deity. They are
proficient with light armor and light shields. The cult leader does not gain
[Weapon Focus](ref/feat/weapon-focus) as a bonus feat as a warpriest normally would. This replaces
the warpriest's weapon and armor proficiencies.

## Well-Hidden (Ex) {#well-hidden}

A cult leader gains a +2 bonus on Disguise and Stealth checks. This ability replaces focus weapon.

## Sneak Attack (Ex) {#sneak-attack}

At 3rd level, a cult leader gains the [sneak attack](ref/ability/sneak-attack) ability, as the rogue
class feature. If he already has sneak attack from another class, the extra damage from the classes
that grant sneak attack stack for the purpose of determining the sneak attack's extra damage dice.
This extra damage is 1d6 at 3rd level and increases by 1d6 every 3 levels thereafter. This ability
replaces the bonus feats gained at 3rd, 9th, and 15th levels.

## Enthrall (Sp) {#enthrall}

At 4th level, a cult leader can cast _[enthrall](ref/spell/enthrall)_. Using this ability consumes
two uses of his fervor ability. This ability replaces channel energy.

## Hide in Plain Sight (Su) {#hide-in-plain-sight}

At 12th level, a cult leader can use the Stealth skill even while being observed. As long as he is
within 10 feet of an area of [dim light](ref/rule/vision-and-light), a cult leader can hide himself
from view in the open without anything to actually hide behind. He cannot, however, hide in his own
shadow. This ability replaces the bonus feat gained at 12th level.
