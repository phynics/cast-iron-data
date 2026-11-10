+++
id = "ref/arc-bard/demagogue"
kind = "archetype"
title = "Demagogue"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Demagogue"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "demagogue", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ultimate-magic"
page = "26"

[fields]
kind = "archetype"
replaces = ["Inspire courage +1", "Lore master", "Suggestion", "Mass suggestion"]
replaces_features = ["lore-master"]
+++

Not content with providing amusing and occasionally instructive performances, the demagogue seeks to
inflame and ignite his audience, driving them toward a specific purpose with carefully chosen words
and tones that may spark momentous change.

**Famous**

**Choice:** A demagogue may choose a region where he is famous, and within that region, the locals
are more likely to react favorably toward him. The bard gains a bonus on Bluff and Intimidate checks
in that area and to influence people from that area.

**At 1st Level:** This region is a settlement or settlements with a total population of 1,000 or
fewer people, and the modifier on Bluff and Intimidate checks is +1. As the demagogue grows more
famous, additional areas learn of him (typically places where he has lived or traveled, or
settlements adjacent to those where he is known) and his bonuses apply to even more people.

**At 13th Level:** The region is a settlement or settlements with a total population of up to
100,000 people, and the modifier to Bluff and Intimidate is +4.

**At 17th Level:** The demagogue's renown has spread far, and most civilized folk know of him (GM's
discretion); the demagogue's modifier on Bluff and Intimidate checks is +5.

**At 5th Level:** The region is a settlement or settlements with a total population of 5,000 or
fewer people, and the modifier on Bluff and Intimidate checks is +2.

**At 9th Level:** The region is a settlement or settlements with a total population of up to 25,000
people, and the modifier on Bluff and Intimidate checks is +3.

**Gained:** At 1st Level

**Replaces:** Inspire courage +1

**Bardic Performance**

**Info:** A demagogue gains the following type of bardic performance.

**Gather Crowd (Ex)**

**Ability:** The demagogue is skilled at drawing an audience to his performances. If he is in a
settlement or populated area, he can shout, sing, or otherwise make himself noticed in order to
attract an audience to his impromptu stage. The size of the crowd depends on the local population,
but typically is a number of people equal to [half](ref/misc/fractions-and-rounding) the bard's
class level &times& the result of the bard's Perform check. The crowd gathers over the next 1d10
rounds.

**Gained:** At 5th Level

**Replaces:** Lore master

**Special:** If the bard fails to engage the crowd (such as by performing, kissing babies, trying to
use _fascinate,_ and so on), it disperses over the next 1d10 rounds.

**Incite Violence (Ex)**

**Ability:** The demagogue can use his performance to fan the fury of a crowd of people he has
fascinated. Using this ability does not disrupt the _fascinate_ effect, but does require a
**standard action** to activate (in addition to the **free action** to continue the _fascinate_
effect). The bard selects a number of targets equal to his level, who must make Will saves (DC 10 +
1/2 the bard's level + the bard's Charisma modifier) or be affected by [rage](ref/spell/rage) for a
number of rounds equal to the bard's level. The bard indicates who is the intended target of
violence (either after using this ability or as part of the performance leading to it) and the
enraged members of the crowd immediately attack the target if possible. The target does not need to
be present (&quot&kill the king&quot& is a suitable choice) and can be an object instead of a person
(&quot&destroy the prison!&quot& is likewise appropriate). Other members of the crowd may follow
suit, though they do not gain the benefits of _rage._

**Gained:** At 6th Level

**Replaces:** Suggestion

**Special:** This is a sound-based effect and is affected by _countersong._ If two or more bards are
attempting to direct the crowd against different targets, they must make opposed Charisma checks,
with the crowd following the directions of the winner.

**Righteous Cause (Ex)**

**Ability:** The demagogue can lift a crowd's emotions and turn them toward a common purpose. First,
he must _fascinate_ the crowd, and then use _incite violence_ without designating a target, at which
point he can use _righteous cause._ Instead of driving the crowd with anger, he fills them with
purpose. Fascinated creatures must make Will saves (DC 10 + 1/2 the bard's level + the bard's
Charisma modifier) to resist. Those who fail are affected by
[mass suggestion](ref/spell/suggestion-mass) of a plausible idea that lingers with them for one day.
Typical uses of this ability are to spark rebellion, overthrow a king, build a beneficial structure
such as an orphanage, or donate money to a cause.

**Gained:** At 18th Level

**Replaces:** Mass suggestion
