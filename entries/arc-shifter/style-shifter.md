+++
id = "ref/arc-shifter/style-shifter"
kind = "archetype"
title = "Style Shifter"
aon = "ArchetypeDisplay.aspx?FixedName=Shifter%20Style%20Shifter"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "style_shifter", path = "json/archetypes_shifter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shifter" },
]
[[sources]]
publication = "martial-arts-handbook"
page = "16"

[fields]
kind = "archetype"
features = [
  { anchor = "natural-strikes" },
  { anchor = "style-shifting", level = 1 },
  { anchor = "style-mastery", level = 1 },
  { anchor = "form-of-the-wild", level = 6 },
]
trades = [
  { replaces = "Shifter aspect", feature = "shifter-aspect", by = ["style-shifting"] },
  { replaces = "chimeric aspect", feature = "chimeric-aspect", by = ["style-shifting"] },
  { replaces = "greater chimeric aspect", feature = "greater-chimeric-aspect", by = ["style-shifting"] },
  { replaces = "final aspect", feature = "final-aspect", by = ["style-shifting"] },
  { alters = "Armor proficiencies", feature = "weapon-and-armor-proficiencies", power = "armor" },
  { alters = "Shifter claws", feature = "shifter-claws", by = ["natural-strikes"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["form-of-the-wild"] },
]
+++

Among the many warriors that train on Tian Xia's Wall of Heaven, a select few have been able to
perfect their combat techniques to the point where they can augment a combat style by partially
transforming into the creature that inspired it. These style shifters have honed their techniques
and shared them with the rest of Golarion.

## Armor Proficiency {#armor-proficiency}

A style shifter is not proficient with medium armor or shields.

This alters the shifter's armor proficiencies.

## Natural Strikes (Ex) {#natural-strikes}

A style shifter is considered to have [Improved Unarmed Strike](ref/feat/improved-unarmed-strike)
for the purposes of feat prerequisites and can apply the effects of feats that have Improved Unarmed
Strike as a prerequisite to her shifter claws.

This alters shifter claws.

## Style Shifting (Ex) {#style-shifting}

A style shifter gains access to style aspects. A style aspect provides benefits only while the style
shifter is in the style feat stance associated with the appropriate aspect (such as
[Boar Style](ref/feat/boar-style) with Form of the Boar). He can shift into his style aspect for a
number of minutes per day equal to 3 + his shifter level. The duration need not be consecutive but
must be spent in 1-minute increments. A style shifter can shift into a style aspect as a free action
as part of entering a style feat's stance. Otherwise, shifting into a style aspect is a swift
action, while ending the effect is a free action that can be taken only on the style shifter's turn.
He can shift between any aspects he has during the duration without additional cost.

This replaces shifter aspect, chimeric aspect, greater chimeric aspect, and final aspect.

## Style Mastery (Ex) {#style-mastery}

At 1st level, 5th level, and every 5 levels thereafter, a style shifter gains a bonus style feat. He
does not need to meet the prerequisites of the feat. Starting at 5th level, he can choose to instead
gain a wildcard style slot. Whenever he enters one or more styles, he can spend his wildcard style
slots to gain feats in those styles' feat paths (such as [Panther Claw](ref/feat/panther-claw) if he
enters [Panther Style](ref/feat/panther-style)) as long as he meets their prerequisites. Each time
he changes styles, he can also change these wildcard style slots.

## Form of the Wild (Su) {#form-of-the-wild}

At 6th level, a style shifter gains the ability to turn into other creatures. This functions as a
[druid's](ref/class/druid) wild shape ability, except he does not gain the ability to turn into an
elemental. The shifter's effective druid level is equal to his class level. He can use this ability
for a number of hours per day equal to 1/3 his effective druid level. This duration does not need to
be consecutive, but must be spent in 1-hour increments. For abilities that function based on uses of
wild shape, each hour of form of the wild counts as a use.

This alters wild shape.

## Style Aspects {#style-aspects}

A style shifter has access to the following style aspects.

### Form of the Boar {#form-of-the-boar}

Once per round when you hit a single foe with two or more unarmed strikes, you can tear flesh. When
you do, you deal an additional 1 point of [bleed](ref/umr/bleed) damage with the attack. At 8th
level, when you tear flesh, the target becomes [sickened](ref/misc/sickened) for 1 round. At 15th
level, whenever you confirm a critical hit, you can attempt an [Intimidate](ref/skill/intimidate)
check to demoralize a target within 30 feet as an immediate action.

### Form of the Crane {#form-of-the-crane}

You reduce the penalty on attack rolls for [fighting defensively](ref/misc/fighting-defensively) by
1, to a minimum penalty of 0. At 8th level, when an attack misses you, you can move 5 feet as an
immediate action without provoking attacks of opportunity. At 15th level, when an attack misses you,
you can move up to half your speed as an immediate action without provoking attacks of opportunity.

### Form of the Dragon {#form-of-the-dragon}

You gain a +1 dodge bonus to your AC for each ally you [charge](ref/rule/charge) through when
charging, up to a total equal to your Dexterity modifier (minimum +0). At 8th level, your unarmed
strike's damage die increases by one step against [shaken](ref/misc/shaken) targets. At 15th level,
whenever you confirm a critical hit against a shaken target, the target becomes
[frightened](ref/misc/frightened) for 1 round.

### Form of the Monkey {#form-of-the-monkey}

You gain a bonus on damage rolls while prone equal to your Wisdom modifier (minimum +0). You can
crawl up to half your speed as a move action. At 8th level, whenever a creature provokes an attack
of opportunity from you, that creature is considered [flat-footed](ref/rule/flat-footed) against
your attack. At 15th level, whenever you take a 5-foot step, you are treated as if you were still in
your original space for the purposes of [flanking](ref/rule/flanking) others until the start of your
next turn (though you can't use this aspect to provide flanking for yourself), and you can crawl up
to your full speed as a move action.

### Form of the Panther {#form-of-the-panther}

You gain a bonus to damage rolls for retaliatory unarmed strikes made with Panther Style equal to
your Wisdom modifier (minimum +0). At 8th level, this bonus increases to twice your Wisdom modifier.
At 15th level, if a creature misses an attack of opportunity against you prompted by your movement
through a threatened square, you can make a retaliatory unarmed strike against that creature, even
if you would not normally be able to make any more retaliatory strikes this turn.

### Form of the Snake {#form-of-the-snake}

Once per round when you hit a single foe with two or more unarmed strikes and deal piercing damage
on your turn, you knock that foe off-balance. The foe is flat-footed until the start of its turn. At
8th level, a foe you knock off-balance can't take attacks of opportunity until the start of its turn
and remains flat-footed until the end of its turn. At 15th level, when you confirm a critical hit,
the target is knocked off-balance and provokes attacks of opportunity from you and your allies.

### Form of the Snapping Turtle {#form-of-the-snapping-turtle}

You double your shield bonus to AC from [Snapping Turtle Style](ref/feat/snapping-turtle-style). At
8th level, you still gain your shield bonus to AC from Snapping Turtle Style even when you don't
have one hand free. At 15th level, there is a 10% chance that critical hits and sneak attacks fail
to affect you. This stacks with the _[light fortification](ref/magic-enh/fortification-light)_ armor
special ability and similar effects.

### Form of the Tiger {#form-of-the-tiger}

On a successful [bull rush](ref/rule/bull-rush), [overrun](ref/rule/overrun), or
[trip](ref/rule/trip) combat maneuver, you deal slashing damage equal to your Strength bonus to the
target of the maneuver. This damage increases to twice your Strength bonus at 8th level. At 15th
level, if you hit with two or more unarmed strikes and deal slashing damage on your turn, you also
rend your target, dealing damage equal to your unarmed strike plus 1-1/2 your Strength bonus.
