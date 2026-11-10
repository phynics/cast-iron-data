+++
id = "ref/arc-cavalier/daring-general"
kind = "archetype"
title = "Daring General"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Daring%20General"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "daring_general", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "24"

[fields]
kind = "archetype"
replaces = ["Bonus feats gained at 6th, 12th, and 18th levels", "Demanding challenge", "Supreme charge"]
+++

Most cavaliers are great tacticians, but some stand above the rest for their ability to lead troops
under their command, and inspire them to great accomplishments. Those cavaliers most gifted at
command often become daring generals.

**Aides-de-Camp (Ex)**

**Action:** Ability

**At 12th Level:** The daring general gains an additional cohort (though see Special below) and a
number of additional followers equal to the number of followers he gained from the Leadership feat
(doubling his followers).

**At 18th Level:** The daring general gains a third cohort (though see Special below) and a number
of additional followers equal to the number of followers he gained from the Leadership feat (ending
up with triple the number of followers normally granted by Leadership).

**Gained:** At 6th Level

**Replaces:** Bonus feats gained at 6th, 12th, and 18th levels

**Special:** All cohorts that the daring general gains from this ability must have levels only in
classes that grant a full base attack bonus (such as barbarian, fighter, paladin, or ranger), and
must be at least 4 levels lower than the daring general himself. When determining the kinds of
cohorts the daring general can attract, he treats his Leadership score as 3 lower for each
subsequent cohort (effectively taking a -3 penalty for the second cohort and a -6 penalty for the
third cohort).

A daring general gains a modified version of the [Leadership](ref/feat/leadership) feat, even if he
doesn't meet the prerequisites. All followers that the daring general gains as a result of this
version of the Leadership feat can only have levels in the [warrior](ref/npcclass/warrior) class.

Additionally, the daring general can grant special roles to his cohorts, as outlined below. Unless
otherwise stated, only one cohort can fill any given role at any given time. Designating a cohort as
filling a special role requires a 24-hour ceremonial ritual.

Beyond the rules noted above, if the daring general uses his followers to create an army using the
[mass combat](ref/rule/mass-combat) rules, that army starts with one extra
[tactic](ref/rule/army-tactics) of the daring general's choice and a +2 bonus to its morale score.

The daring general can assign each of his followers individually to serve as either footmen or honor
guards (described below). He does not need to assign either role to a given follower, if he prefers.
He can change the role of a follower at any time, but it takes 1 day per level for the follower to
change her tactics to suit her new role. Followers with a particular role must group together with
other followers with the same role to form an army in mass combat.

**Groom (Cohort Role)**

**Ability:** The groom cares for the daring general's mount. She does not take an armor check
penalty on Ride checks while riding the cavalier's mount. Additionally, once per day, the groom can
spend 10 minutes preparing the daring general's mount for battle. If she does, the mount's speed
increases by 10 feet and its Dexterity score increases by 2. These benefits last for 1 hour.

**Squire (Cohort Role)**

**Ability:** The squire's main task is to care for the daring general's arms and armor. If the
squire aids the daring general in donning his armor, it takes
[half](ref/misc/fractions-and-rounding) as much time to don as it would if someone else aided the
daring general. Additionally, when the squire is adjacent to the daring general, as a **standard
action**, she can grant a +2 bonus to the daring general's AC against the first attack made against
the daring general before the squire's next turn. This counts as an application of the
[aid another](ref/rule/aid-another-2) action, but the squire does not need to threaten the attacker
in question.

**Standard Bearer (Cohort Role)**

**Ability:** The daring general's standard bearer can carry his banner in his stead, granting the
benefits of his _banner_ ability (and later, his _greater banner_ ability) to all allies within 60
feet of the standard bearer. If the standard bearer becomes unconscious or dead, she ceases to grant
these benefits.

**Footman (Follower Role)**

**Passive:** Each follower gains a +2 bonus on attack and damage rolls, but takes a -2 penalty to
her AC and on saving throws. A footman unit gains a +2 bonus to its OM and takes a -2 penalty to its
DV in mass combat.

**Honor Guard (Follower Role)**

**Passive:** The follower gains a +2 bonus to her AC and on saving throws, but takes a -2 penalty on
attack and damage rolls. An honor guard unit gains a +2 bonus to its DV and takes a -2 penalty to
its OM in mass combat.

**Shared Challenge (Ex)**

**Gained:** At 12th Level

**Passive:** When a daring general issues a _challenge,_ his followers and cohorts take up that
_challenge_ alongside him. Whenever the daring general uses his _challenge_ class feature, as long
as the _challenge_ remains in effect, each of the daring general's followers and cohorts that are
within 30 feet of him gain a +4 morale bonus on attack rolls made against the target of his
_challenge._

**Replaces:** Demanding challenge

**Supreme Tactician (Ex)**

**Ability:** At 20th level, whenever the daring general uses his _tactician_ ability, he can grant
any number of teamwork feats that he knows to his allies, and when he uses his _tactician_ ability
as a **standard action** in combat, it does not count against his daily uses of _tactician._

**Gained:** At 20th Level

**Replaces:** Supreme charge
