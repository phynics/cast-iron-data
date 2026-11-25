+++
id = "ref/arc-fighter/lore-warden"
kind = "archetype"
title = "Lore Warden"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Lore%20Warden"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lore_warden", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "adventurers-guide"
page = "144"

[fields]
kind = "archetype"
features = [
  { anchor = "scholastic" },
  { anchor = "skill-over-strength", level = 2 },
  { anchor = "swords-secret" },
  { anchor = "exploit-weakness" },
  { anchor = "hair-s-breadth" },
  { anchor = "know-thy-enemy" },
  { anchor = "maneuver-training" },
  { anchor = "swift-assessment" },
]
trades = [
  { replaces = "Proficiency with medium armor", feature = "weapon-and-armor-proficiencies", power = "medium armor", by = ["scholastic"] },
  { replaces = "heavy armor", feature = "weapon-and-armor-proficiencies", power = "heavy armor", by = ["scholastic"] },
  { replaces = "and shields", feature = "weapon-and-armor-proficiencies", power = "shields", by = ["scholastic"] },
  { replaces = "Bravery", feature = "bravery", by = ["skill-over-strength"] },
  { replaces = "the fighter bonus feat gained at 2nd level", feature = "bonus-feats", levels = [2], by = ["skill-over-strength"] },
  { replaces = "Armor training", feature = "armor-training", by = ["swift-assessment"] },
  { replaces = "armor mastery", feature = "armor-mastery", by = ["swift-assessment"] },
]
+++

Quick wits and deceptive techniques can often succeed where brute force might not. A lore warden is
the consummate warrior-scholar of the [Pathfinder Society](ref/rule/aff-scholars), outsmarting her
competition even when locking blades with powerful foes. Outside of combat, a lore warden's
extensive education also helps her document the past and survive great danger.

## Scholastic (Ex) {#scholastic}

A lore warden gains 2 additional skill ranks each level. These ranks must be spent on
Intelligence-based skills. All [Craft](ref/skill/craft-any) and [Knowledge](ref/skill/knowledge-all)
skills are class skills for lore wardens, as are [Linguistics](ref/skill/linguistics) and
[Spellcraft](ref/skill/spellcraft).

This ability replaces the fighter's proficiency with medium armor, heavy armor, and shields.

## Skill Over Strength (Ex) {#skill-over-strength}

At 2nd level, a lore warden qualifies for feats and other abilities as though she had the
[Combat Expertise](ref/feat/combat-expertise) feat. At 6th level, she gains Combat Expertise as a
bonus feat, even if she would not normally qualify for the feat. If she already has Combat
Expertise, she instead gains any one combat feat that includes Combat Expertise as a prerequisite
(and for which she otherwise qualifies). At 10th level, she can treat her base attack bonus as
though it were 2 higher for the purpose of calculating the effects of Combat Expertise.

This ability replaces bravery and the fighter bonus feat gained at 2nd level.

## Swords Secret (Ex) {#swords-secret}

A lore warden learns specialized techniques that help her to quickly analyze and defeat her foes. At
3rd level, a lore warden gains one swords secret, and she gains an additional swords secret for
every 4 fighter levels gained after 3rd. Except where noted, a lore warden cannot select the same
swords secret more than once.

## Exploit Weakness (Ex) {#exploit-weakness}

The lore warden adds [one-third](ref/misc/fractions-and-rounding) her class level on attack rolls to
confirm critical hits. At 11th level, whenever she confirms a critical hit, her weapon attacks
ignore the first 5 points of [damage reduction](ref/rule/damage-reduction) or
[hardness](ref/umr/hardness) the target has until the end of her next turn. At 19th level, the lore
warden can automatically confirm a critical hit once per round when she threatens a critical hit.

## Hair's Breadth (Ex) {#hair-s-breadth}

Once per day when subject to a critical hit, the lore warden can attempt an Acrobatics check to
reduce the damage as an immediate action. If the result of this Acrobatics check is greater than the
opponent's confirmation roll, she negates the critical hit; the attack still hits and deals normal
damage. The lore warden must be at least 11th level to select this swords secret.

At 15th level she can use this secret one additional time per day.

## Know Thy Enemy (Ex) {#know-thy-enemy}

When the lore warden succeeds at a Knowledge check to identify a creature's abilities and
weaknesses, she can also use a standard action to grant herself a +2 insight bonus on all attack and
weapon damage rolls made against that enemy. This bonus lasts for a number of rounds equal to half
her class level (minimum 2 rounds), or until the lore warden uses this ability against a different
creature. At 11th level, she also gains a +2 bonus to her AC against the creature when using this
ability. At 19th level, the insight bonus increases to +3.

## Maneuver Training (Ex) {#maneuver-training}

The lore warden gains a [brawler](ref/class/brawler)'s maneuver training class feature, treating her
fighter level as her brawler level.

## Swift Assessment (Ex) {#swift-assessment}

The lore warden can now use her know thy enemy swords secret as a move action. At 15th level, she
can use this ability as a swift action. She must have the know thy enemy swords secret before
choosing this swords secret.

This replaces armor training and armor mastery.
