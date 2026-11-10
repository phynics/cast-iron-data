+++
id = "ref/arc-shifter/rageshaper"
kind = "archetype"
title = "Rageshaper"
aon = "ArchetypeDisplay.aspx?FixedName=Shifter%20Rageshaper"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rageshaper", path = "json/archetypes_shifter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shifter" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "82"

[fields]
kind = "archetype"
replaces = ["Wild shape", "shifter aspect", "Defensive instinct", "chimeric aspect", "greater chimeric aspect", "Woodland stride", "Trackless step"]
alters = ["Alignment", "Shifter claws"]
replaces_features = ["wild-shape", "shifter-aspect", "defensive-instinct", "chimeric-aspect", "greater-chimeric-aspect", "woodland-stride", "trackless-step"]
alters_features = ["shifter-claws"]
+++

Not all shifters represent the balance of nature. The rageshaper is a destructive force of nature
brought to bear - a wild and uncontrollable engine of annihilation fueled by wrath. Rageshapers fly
into bloodletting frenzies and rain down devastation like unstoppable natural disasters.

**Alignment**

**Alters:** Alignment

**Info:** A rageshaper can be any nonlawful alignment. A rageshaper who becomes lawful cannot take
any further levels in rageshaper, but he does not lose access to any rageshaper abilities he has
already gained.

**Devastating Form (Su)**

**Action:** Ability

**At 10th Level:** The rageshaper can grow up to a maximum of two size categories larger with
_devastating form_ and his _rage_ is now treated as _greater rage._

**At 20th Level:** The rageshaper can grow up to a maximum of three size categories larger with
_devastating form_ and his _rage_ is treated as _mighty rage._

**Replaces:** Wild shape, shifter aspect

A rageshaper can enter a state of intense fury, transforming into a living engine of destruction.
This ability functions as the [barbarian's](ref/class/barbarian) _rage_ class feature, except
entering this state of fury requires a **full-round action** that provokes attacks of opportunity
and has additional effects as noted below. At the start of the rageshaper's next turn, he not only
gains the benefit of _rage_ but also grows one size category larger (though worn equipment and held
items do not increase in size).

Armor or clothing the rageshaper wears that doesn't accommodate his changing size immediately gains
the [broken](ref/misc/broken) condition. If insufficient room is available to accommodate this
change, the rageshaper attains the maximum possible size for the available space and can attempt a
Strength check (using his increased Strength) to burst any enclosures in the process. If the check
fails, he is constrained but not harmed by the materials enclosing him.

[Look here](ref/rule/adding-racial-hit-dice) for rules on attribute and skill bonuses and penalties
due to a change of size.

A rageshaper can remain in his _devastating form_ for a number of rounds per day equal to his
shifter level. He can dismiss _devastating form_ only with a successful Will save (DC = 10 + his
shifter level) made as a **free action**. On a failed save, the attempted remains in _devastating
form_ for an additional round. If the rageshaper does not successfully end his _devastating form_
before he runs out of daily rounds, the next time he fails his Will save to revert, he flies into an
uncontrollable frenzy as if affected by [confusion](ref/spell/confusion), but he treats a roll of
26-50 as "attacks nearest creature." Each round the rageshaper spends in an uncontrollable frenzy,
the Will save DC to exit devastating form decreases by 2.

When a rageshaper ends his _devastating form_ ability, he is [fatigued](ref/misc/fatigued) for a
number of rounds equal to twice the number of rounds he spent in _devastating form._ A rageshaper
cannot enter _devastating form_ again while fatigued or exhausted. If a rageshaper falls
unconscious, his _devastating form_ ends immediately.

**Rage (Ex)**

**Ability:** You gain a +4 morale bonus to your Strength and Constitution, as well as a +2 morale
bonus on Will saves. The increase to Constitution grants you 2 hit points per Hit Dice, but these
disappear when the _rage_ ends and are not lost first like
[temporary hit points](ref/rule/temporary-hit-points).

**Flavor:** Relevant text from the barbarian ability.

**Passive:** While in _rage,_ you take a -2 penalty to Armor Class, and you cannot use any
Charisma-, Dexterity-, or Intelligence-based skills (except Acrobatics, Fly, Intimidate, and Ride)
or any ability that requires patience or concentration.

**Special:** Temporary increases to Constitution, such as those gained from _rage_ and spells like
[bear's endurance](ref/spell/bears-endurance), do not increase the total number of rounds that a
barbarian can _rage_ per day. The total number of rounds of _rage_ per day is renewed after resting
for 8 hours, although these hours do not need to be consecutive.

**Greater Rage (Ex)**

**Flavor:** Relevant text from the barbarian ability.

**Passive:** When you enter a _rage,_ the morale bonus to your Strength and Constitution increase to
+6 and the morale bonus on your Will saves increases to +3.

**Mighty Rage (Ex)**

**Flavor:** Relevant text from the barbarian ability.

**Passive:** When you enter a _rage,_ the morale bonus to your Strength and Constitution increase to
+8 and the morale bonus on your Will saves increases to +4.

**Terrible Slam (Su)**

**Ability:** A rageshaper can deliver blows that demolish his foes. This functions as the _shifter
claws_ class ability, except his natural weapons are treated as slam attacks. Additionally, rather
than granting the ability to bypass different kinds of
[damage reduction](ref/rule/damage-reduction), the rageshaper's _terrible slam_ ignores some of an
object's [hardness](ref/umr/hardness).

**Alters:** Shifter claws

**At 1st Level:** _Terrible slam_ ignores 5 points of an object's [hardness](ref/umr/hardness).

At 5th level: This 10 points.

At 10th level: This 15 points.

At 15th level: This 20 points.

At 20th level: This 25 points.

**Invulnerable Defenses (Ex)**

**Flavor:** A rageshaper becomes difficult to harm in his _devastating form._

**Gained:** At 2nd Level

**Passive:** Whenever the rageshaper takes on his _devastating form_ and is unencumbered and either
wearing no armor or wearing light or medium nonmetal armor, he gains a +2 natural armor bonus to his
AC and DR 2/-.

**Replaces:** Defensive instinct, chimeric aspect, greater chimeric aspect

**Unrestrained Stride (Ex)**

**Ability:** Whenever the rageshaper is in _devastating form,_ he ignores movement penalties from
[difficult terrain](ref/rule/terrain-and-obstacles) and is immune to the
[entangled](ref/rule/entangled) condition.

**Gained:** At 3rd Level

**Replaces:** Woodland stride

**Terrible Leap (Ex)**

**Gained:** At 5th Level

**Move:** When a rageshaper is in his _devastating form,_ he can perform a _terrible leap_ without
attempting an Acrobatics check, jumping any distance up to his move speed (upward movement counts as
double, as when flying).

**Replaces:** Trackless step

**Usage:** 1 time/day per shifter level
