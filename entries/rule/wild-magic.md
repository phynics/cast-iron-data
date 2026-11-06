+++
id = "ref/rule/wild-magic"
kind = "rule"
title = "Wild Magic"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wild_magic", path = "json/rules_subsystems04.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 147

Though many spellcasters like to consider their use of magic a science, the effects of magic are not
always easy to predict. Wild, uncontrolled magic sometimes surges as a side effect of spellcasting
or magical experimentation. Wild magic can be used in any situation where magic might cause
randomness and chaotic effects. When a character casts a spell or takes an action that could trigger
a surge of wild magic (see [Implementing Wild Magic](ref/rule/implementing-wild-magic)), roll on
Table 4-4: Wild Magic Surge.

Roll to determine the surge effect before the spell is cast, but apply the effect after the spell is
cast unless it alters the spell itself in some way (such as changing the effective caster level).
Any reference on the table to the spell or the spell's level applies to the spell being cast,
supernatural ability being used, or magic item effect being activated. Similarly, any reference to
the caster applies to the character who triggers the surge. If an effect requires a caster level,
use the caster's full character level.

If the wild magic surge effect you roll isn't possible due to the nature of the spell or effect,
roll instead on Table 4-5: Universal Surge Effects. A wild magic surge effect doesn't allow a saving
throw, even if it's replicating a spell that normally would, and any effect that would normally have
a limit on the amount of Hit Dice it can affect ignores that limit. Higher results on the table are
more likely to be beneficial, so a GM might give a bonus or penalty on the check if an action would
alter how likely it is that the wild magic surge would be helpful.

### Table 4-4: Wild Magic Surge

|d%|Surge Effect|
| --- | --- |
|01-02|The caster takes 1d6 points of damage per spell level.|
|03-04|The caster is affected by a [slow](ref/spell/slow) spell for 5 rounds.|
|05|The spell takes effect at a random location within the spell's range.|
|06|The caster is confused for 1 round (as [confusion](ref/spell/confusion)).|
|07|The caster takes 1 point of Constitution bleed.|
|08|The caster takes 1 point of ability bleed that matches her spellcasting ability score (determine randomly if the creature isn't a spellcaster).|
|09-10|The caster is dazed for 1 round (as [daze monster](ref/spell/daze-monster)).|
|11-12|The spell deals half as much damage as normal.|
|13|The caster takes 1d4 points of bleed damage.|
|14|The caster falls asleep for 1 minute (as [sleep](ref/spell/sleep)).|
|15-16|The caster can't cast or concentrate on spells for 1 round.|
|17|The caster is affected by [reduce person](ref/spell/reduce-person) for 1 minute.|
|18-19|The caster becomes sickened for 5 rounds.|
|20|A [zone of truth](ref/spell/zone-of-truth) appears, centered on the caster.|
|21-29|The caster is affected as if targeted by the spell.|
|30-32|All targets of the spell are affected by [lesser restoration](ref/spell/restoration-lesser).|
|33-38|All targets of the spell are healed of 1d8+1 points of damage. This is a positive energy effect.|
|39-43|The spell's area or the targets of the spell become affected by [silence](ref/spell/silence) for 3 rounds.|
|44-50|All targets of the spell become invisible for 1 round (as [invisibility](ref/spell/invisibility)).|
|51-58|The area of the spell is filled with [daylight](ref/spell/daylight).|
|59-64|A [shatter](ref/spell/shatter) spell affects a 5-foot radius around each target of the spell (or the spell's area).|
|65-71|The spell's area is coated in [grease](ref/spell/grease).|
|72-74|One random tree or animal targeted by the spell or in the spell's area is affected by [awaken](ref/spell/awaken).|
|75-78|An instrument appears adjacent to each target (as [summon instrument](ref/spell/summon-instrument)).|
|79-80|Every door within 100 feet of the caster is affected by a [knock](ref/spell/knock) spell.|
|81-83|The caster teleports to a square of her choice adjacent to the spell's target or within the spell's area.|
|84-86|The next spell targeting the caster is turned back, as [spell turning](ref/spell/spell-turning).|
|87-90|The caster gains 2d6 temporary hit points that last 1 hour and don't stack with any other temporary hit points.|
|91-92|A random creature from the [summon monster I](ref/spell/summon-monster-1) list is summoned in a square adjacent to the caster. It is under the caster's control.|
|93-95|The caster is affected by tongues for 10 minutes.|
|96-97|The caster is affected by haste for 5 rounds.|
|98|The spell is [extended](ref/feat/extend-spell).|
|99|The spell is [maximized](ref/feat/maximize-spell).|
|100|The spell slot used to cast the spell is not expended.|

### Table 4-5: Universal Surge Effects

|d%|Surge Effect|
| --- | --- |
|01-20|The caster takes 1d6 points of damage that can't be prevented in any way.|
|21-80|The caster is affected by [faerie fire](ref/spell/faerie-fire) for 1 round.|
|81-100|The caster gains 1d6 temporary hit points that last for 1 hour. These don't stack with other temporary hit points.|

**Compare:** [Primal Magic](ref/rule/primal-magic), Wild Magic under
[Planar Magic Traits](ref/rule/magic-traits)
