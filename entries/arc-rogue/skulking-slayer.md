+++
id = "ref/arc-rogue/skulking-slayer"
kind = "archetype"
title = "Skulking Slayer"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Skulking%20Slayer"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "skulking_slayer", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-race-guide"
page = "55"

[fields]
kind = "archetype"
features = [
  { anchor = "class-skills" },
  { anchor = "skill-ranks-per-level" },
  { anchor = "pass-for-human", level = 1 },
  { anchor = "underhanded-maneuvers", level = 1 },
  { anchor = "bold-strike", level = 3 },
  { anchor = "shifty", level = 6 },
  { anchor = "unexpected-charge", level = 9 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["underhanded-maneuvers"] },
  { replaces = "Trap sense +1 and +4", feature = "trap-sense", levels = [3, 12], by = ["bold-strike"] },
  { replaces = "Trap sense +2", feature = "trap-sense", levels = [6], by = ["shifty"] },
  { replaces = "Trap sense +3", feature = "trap-sense", levels = [9], by = ["unexpected-charge"] },
]
+++

Pushed into a life of crime by the society around them, half-orcs gravitate toward criminal
activities that suit them best. Half-orc rogues leave subtle tactics and finesse to halflings and
elves, and rely on brute strength and thuggery when they go about making mischief. Skulking slayers
have turned the use of raw strength and surprise into an art form. A skulking slayer has the
following class features.

**Prerequisites:** Half-Orc

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

The skulking slayer gains proficiency with [greatclubs](ref/eq-weapon/greatclub) and
[whips](ref/eq-weapon/whip), but loses proficiency with rapiers and hand crossbows.

## Class Skills {#class-skills}

The skulking slayer does not gain Disable Device, Linguistics, and Sleight of Hand as class skills.

## Skill Ranks per Level {#skill-ranks-per-level}

6 + Int modifier.

## Pass for Human (Ex) {#pass-for-human}

At 1st level, when trying to conceal her [half](ref/misc/fractions-and-rounding)-orc heritage, a
skulking slayer gains a bonus on Disguise checks equal to half her level. When using disguise to
appear as a specific individual, skulking stalkers ignore the normal -2 penalty to appear as another
race.

## Underhanded Maneuvers (Ex) {#underhanded-maneuvers}

At 1st level, when she could normally make a sneak attack, a slayer may instead make a
[dirty trick](ref/rule/dirty-trick) or [steal](ref/rule/steal) combat maneuver with a bonus on her
roll. This bonus is equal to her number of sneak attack dice for a dirty trick combat maneuver, or
1-1/2 her number of sneak attack dice for a steal combat maneuver. This ability replaces
trapfinding.

## Bonus Feats {#bonus-feats}

At 2nd level, a skulking slayer can select the
[Surprise Follow-Through](ref/feat/surprise-follow-through) feat (see below) in place of a rogue
talent. At 10th level, she can select the
[Improved Surprise Follow-Through](ref/feat/improved-surprise-follow-through) feat (if she already
has Surprise Follow-Through) in place of an advanced rogue talent.

## Bold Strike (Ex) {#bold-strike}

At 3rd level, when a skulking slayer [charges](ref/rule/charge) and makes a sneak attack with a
two-handed weapon, she rolls d8s instead of d6s for her sneak attack damage. This ability replaces
trap sense +1 and +4.

## Shifty (Ex) {#shifty}

At 6th level, a skulking slayer gains a bonus on Bluff checks to feint equal to half her level. This
ability replaces trap sense +2.

## Unexpected Charge (Ex) {#unexpected-charge}

At 9th level, a skulking slayer can make a [Bluff](ref/skill/bluff) check to feint as a swift action
before a charge. This ability replaces trap sense +3.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the skulking slayer archetype: combat trick, surprise attack
(_Core Rulebook_); combat swipe, powerful sneak (_Advanced Player's Guide_); terrain mastery
(_Ultimate Combat_).

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the skulking slayer archetype: crippling strike
(_Core Rulebook_); deadly sneak (_Advanced Player's Guide_); unwitting ally (_Ultimate Combat_).
