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
replaces = ["Shifter aspect", "chimeric aspect", "greater chimeric aspect", "final aspect"]
alters = ["Armor proficiencies", "Shifter claws", "Wild shape"]
+++

Among the many warriors that train on Tian Xia's Wall of Heaven, a select few have been able to
perfect their combat techniques to the point where they can augment a combat style by partially
transforming into the creature that inspired it. These style shifters have honed their techniques
and shared them with the rest of Golarion.

**Armor Proficiency**

**Alters:** Armor proficiencies

**Info:** A style shifter is not proficient with medium armor or shields.

**Natural Strikes (Ex)**

**Alters:** Shifter claws

**Info:** A style shifter is considered to have
[Improved Unarmed Strike](ref/feat/improved-unarmed-strike) for the purposes of feat prerequisites
and can apply the effects of feats that have Improved Unarmed Strike as a prerequisite to her
_shifter claws._

**Style Shifting (Ex)**

**Ability:** A style shifter gains access to _style aspects._ A style aspect provides benefits only
while the style shifter is in the style feat stance associated with the appropriate aspect (such as
[Boar Style](ref/feat/boar-style) with _Form of the Boar_).

**Replaces:** Shifter aspect, chimeric aspect, greater chimeric aspect, final aspect

**Special:** A style shifter can shift into a style aspect as a **free action** as part of entering
a style feat's stance. Otherwise, shifting into a style aspect is a **swift action**, while ending
the effect is a **free action** that can be taken only on the style shifter's turn. He can shift
between any aspects he has during the duration without additional cost.

**Usage:** 1 minute/day per shifter3 level; these minutes need not be consecutive, but must be spent
in 1-minute increments

**Form of the Boar**

**Ability:** Once per round when you hit a single foe with two or more unarmed strikes, you can tear
flesh. When you do, you deal an additional 1 point of [bleed](ref/umr/bleed) damage with the attack.

**At 15th Level:** Whenever you confirm a critical hit, you can attempt an
[Intimidate](ref/skill/intimidate) check to demoralize a target within 30 feet as an **immediate
action**.

**At 8th Level:** When you tear flesh, the target becomes [sickened](ref/misc/sickened) for 1 round.

**Form of the Crane**

**Ability:** You reduce the penalty on attack rolls for
[fighting defensively](ref/misc/fighting-defensively) by 1, to a minimum penalty of 0.

**At 15th Level:** When an attack misses you, you can move up to half your speed as an **immediate
action** without provoking attacks of opportunity.

**At 8th Level:** When an attack misses you, you can move 5 feet as an **immediate action** without
provoking attacks of opportunity.

**Form of the Dragon**

**Ability:** You gain a +1 dodge bonus to your AC for each ally you [charge](ref/rule/charge)
through when charging, up to a total equal to your Dexterity modifier (minimum +0).

**At 15th Level:** Whenever you confirm a critical hit against a shaken target, the target becomes
[frightened](ref/misc/frightened) for 1 round.

**At 8th Level:** Your unarmed strike's damage die increases by one step against
[shaken](ref/misc/shaken) targets.

**Form of the Monkey**

**Ability:** You gain a bonus on damage rolls while prone equal to your Wisdom modifier (minimum
+0).

**At 15th Level:** Whenever you take a 5-foot step, you are treated as if you were still in your
original space for the purposes of [flanking](ref/rule/flanking) others until the start of your next
turn (though you can't use this aspect to provide flanking for yourself), and you can crawl up to
your full speed as a **move action**.

**At 8th Level:** Whenever a creature provokes an attack of opportunity from you, that creature is
considered [flat-footed](ref/rule/flat-footed) against your attack.

**Move:** You can crawl up to half your speed.

**Form of the Panther**

**Ability:** You gain a bonus to damage rolls for retaliatory unarmed strikes made with Panther
Style equal to your Wisdom modifier (minimum +0).

**At 15th Level:** If a creature misses an attack of opportunity against you prompted by your
movement through a threatened square, you can make a retaliatory unarmed strike against that
creature, even if you would not normally be able to make any more retaliatory strikes this turn.

**At 8th Level:** This bonus increases to twice your Wisdom modifier.

**Form of the Snake**

**Ability:** Once per round when you hit a single foe with two or more unarmed strikes and deal
piercing damage on your turn, you knock that foe off-balance. The foe is flat-footed until the start
of its turn.

**At 15th Level:** When you confirm a critical hit, the target is knocked off-balance and provokes
attacks of opportunity from you and your allies.

**At 8th Level:** A foe you knock off-balance can't take attacks of opportunity until the start of
its turn and remains flat-footed until the end of its turn.

**Form of the Snapping Turtle**

**Ability:** You double your shield bonus to AC from
[Snapping Turtle Style](ref/feat/snapping-turtle-style).

**At 15th Level:** There is a 10% chance that critical hits and sneak attacks fail to affect you.
This stacks with the [light fortification](ref/magic-enh/fortification-light) armor special ability
and similar effects.

**At 8th Level:** You still gain your shield bonus to AC from Snapping Turtle Style even when you
don't have one hand free.

**Form of the Tiger**

**Ability:** On a successful [bull rush](ref/rule/bull-rush), [overrun](ref/rule/overrun), or
[trip](ref/rule/trip) combat maneuver, you deal slashing damage equal to your Strength bonus to the
target of the maneuver.

**At 15th Level:** If you hit with two or more unarmed strikes and deal slashing damage on your
turn, you also rend your target, dealing damage equal to your unarmed strike plus 1-1/2 your
Strength bonus.

**At 8th Level:** This damage increases to twice your Strength bonus.

**Style Mastery (Ex)**

**At 1st Level:** A style shifter gains a bonus style feat.

**At 5th Level:** A style shifter gains either a bonus style feat, or can instead gain a wildcard
style slot. Whenever he enters one or more styles, he can spend his wildcard style slots to gain
feats in those styles' feat paths (such as [Panther Claw](ref/feat/panther-claw) if he enters
[Panther Style](ref/feat/panther-style)) as long as he meets their prerequisites. Each time he
changes styles, he can also change these wildcard style slots.

**Repeat:** He can gain another style feat or wildcard style slot., 10, 5

**Special:** If he chooses to gain a new style feat, he does not need to meet the prerequisites of
it.

**Form of the Wild (Su)**

**Ability:** A style shifter gains the ability to turn into other creatures. This functions as a
[druid's](ref/class/druid) _wild shape_ ability, except he does not gain the ability to turn into an
elemental. The shifter's effective druid level is equal to his class level.

**Alters:** Wild shape

**Gained:** At 6th Level

**Special:** For abilities that function based on uses of _wild shape,_ each hour of _form of the
wild_ counts as a use.

**Usage:** 1 hour/day per 3 druid levels; these hours need not be consecutive, but must be spent in
1-hour increments
