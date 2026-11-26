+++
id = "ref/arc-fighter/ustalavic-duelist"
kind = "archetype"
title = "Ustalavic Duelist"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Ustalavic%20Duelist"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ustalavic_duelist", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "inner-sea-combat"
page = "47"

[fields]
kind = "archetype"
features = [
  { anchor = "duelist-stance", level = 1 },
  { anchor = "duelist-training", level = 5 },
  { anchor = "lepidstadt-thrust", level = 9 },
  { anchor = "science-of-the-blade", level = 13 },
  { anchor = "surgical-strike", level = 17 },
]
trades = [
  { replaces = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { replaces = "The fighter's 1st-level bonus feat", feature = "bonus-feats", levels = [1], by = ["duelist-stance"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["duelist-training"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["lepidstadt-thrust"] },
  { replaces = "Weapon training 3", feature = "weapon-training", levels = [13], by = ["science-of-the-blade"] },
  { replaces = "Weapon training 4", feature = "weapon-training", levels = [17], by = ["surgical-strike"] },
]
+++

The University of Lepidstadt has developed a reputation for churning out fearsome duelists. At the
end of each academic year, the students all gather together and duel one another with light blades.
Each student duels one opponent after another until he is marked on the cheek by an adversary's
blade. These "Lepidstadt scars" are recognized throughout the Inner Sea region and beyond as marks
of their prowess. The Lepidstadt Style is one of fluid motion and precise thrusts.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

An Ustalavic duelist is proficient with all simple and martial weapons and with all light and medium
armor and shields (except tower shields). This replaces the fighter's normal weapon and armor
proficiencies.

## Duelist Stance (Ex) {#duelist-stance}

At 1st level, an Ustalavic duelist gains a +1 dodge bonus to AC as long as he is wearing no armor or
light armor, wields a melee weapon in one hand, and his other hand is empty. This bonus increases by
1 for every 5 levels the duelist possesses to a maximum of +5 at 20th level. This ability replaces
the fighter's 1st-level bonus feat.

## Duelist Training (Ex) {#duelist-training}

At 5th level, an Ustalavic duelist must select the light blades [group](ref/ability/weapon-groups)
for the weapon training class feature. The Ustalavic duelist's weapon training bonus with light
blades increases by 1 on attack and damage rolls for every 4 levels he possesses beyond 5th (to a
maximum of +4 on attack and damage rolls at 17th level). If he is using his duelist stance, this
damage bonus increases by 2. The Ustalavic duelist does not gain weapon training in any other groups
as he increases in level. This ability replaces weapon training 1.

## Lepidstadt Thrust (Ex) {#lepidstadt-thrust}

At 9th level, when using [Vital Strike](ref/feat/vital-strike),
[Improved Vital Strike](ref/feat/improved-vital-strike), or
[Greater Vital Strike](ref/feat/greater-vital-strike), an Ustalavic duelist adds his Intelligence
modifier to damage rolls (this bonus to damage is not multiplied on a critical hit). If the duelist
confirms a critical hit while using one of these feats, he automatically deals maximum damage. This
ability replaces weapon training 2.

## Science of the Blade (Ex) {#science-of-the-blade}

At 13th level, an Ustalavic duelist is able to apply his specialized knowledge of anatomy and
physiology to his bladework. The duelist can make [dirty trick](ref/rule/dirty-trick),
[disarm](ref/rule/disarm), and [trip](ref/rule/trip) combat maneuvers using any one-handed piercing
or slashing weapon. This ability replaces weapon training 3.

## Surgical Strike (Ex) {#surgical-strike}

At 17th level, when an Ustalavic duelist confirms a critical hit with a light or one-handed piercing
or slashing weapon, he deals [ability damage](ref/rule/ability-damage-drain) in addition to the
normal bonus damage from the critical hit. The duelist chooses which ability is damaged, and deals
an amount of damage equal to the critical multiplier of the wielded weapon. This ability replaces
weapon training 4.
