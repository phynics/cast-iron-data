+++
id = "ref/arc-ranger/dandy"
kind = "archetype"
title = "Dandy"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dandy", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "41"

[fields]
kind = "archetype"
replaces = ["Favored enemy", "Wild empathy", "Woodland stride"]
alters = ["Favored terrain", "Hunter's bond", "Spellcasting"]
+++

The antithesis of the gruff and wild woodsmen, a dandy takes effort to master the subtle etiquette
of noble courts, the whispers of dark rumors, and the customs of the cultured world. Nonetheless, he
is still a ranger at heart, and he hunts for rumors and gossip throughout the grand ballrooms of the
wealthy and powerful just as most rangers hunt for enemies in the wilderness.

**Gained class skills:** bluff, diplo, kl, kno, sm

**Lost class skills:** ha, kd, kg, kna, sur

**Favored Nation (Ex)**

**Ability:** A dandy can attempt the appropriate Knowledge checks untrained to identify such people
from the selected country.

**Choice:** Each time he would select a _favored enemy,_ a dandy instead selects a country with
whose courtly graces he is wholly versed and studied. He gains a +2 bonus on Bluff, Diplomacy,
Knowledge, Perception, Sense Motive, and Survival checks against courtiers, officials, nobles, and
gentry from that nation. Likewise, he gains a +2 bonus on weapon attack and damage rolls against
them.

**Replaces:** Favored enemy

**Special:** A dandy gains additional favored nations, and can increase the bonuses of one of his
current favored nations, in the same way he would with a normal ranger's _favored enemy._

**Rumor Empathy (Ex)**

**Action:** Ability

**Replaces:** Wild empathy

A dandy can alter the flow and spread of [rumors](ref/rule/rumors) in his favor. This functions
similarly to _wild empathy,_ except that it takes 1 day (8 hours of work), instead of 1 minute, and
it affects the general tenor of a rumor instead of a wild animal.

A successful _rumor empathy_ check allows the dandy to increase or decrease the rumor's tone by one
step. For example, he could make an indifferent rumor friendly and thus positive toward its target,
or an unfriendly rumor hostile and thus even more negative toward its target than it was originally.

The difficulty of influencing a rumor depends on the size of the community in which it is spreading.
The DC of the check is 15 in a village or smaller settlement. This DC increases by 5 and the number
of days required to attempt the check increases by 2 for every
[settlement size category](ref/rule/settlements-and-districts) larger than a village - to a maximum
of DC 40 and 11 days to affect a rumor spreading through an entire metropolis.

If the rumor is only spreading through a smaller segment of the population, such as the elven
district in a larger metropolis, use the population of that smaller segment to determine the DC and
number of days of work required to use _rumor empathy._ The DC also increases by 10 if the rumor is
about the dandy himself, since the dandy is obviously a biased source with respects to rumors about
his own person.

**Favored Terrain (Ex)**

**Ability:** A dandy gains _favored terrain (urban),_ and though the ability continues to increase
at the same levels, he doesn't add additional terrains.

**Alters:** Favored terrain

**At 8th Level:** Whenever he is at a courtly function or party, his _favored terrain_ bonuses
increase by an additional 2.

**Gained:** At 3rd Level

**Hobnob (Ex)**

**Ability:** In addition to the usual _hunter's bond_ ability, the dandy can spend 10 minutes at a
particular event or party hobnobbing and introducing his allies to the right people in order to
provide them with half the skill bonuses of his favored nation (though not the bonuses on attack and
damage rolls) for the duration of the event.

**Alters:** Hunter's bond

**Info:** A dandy must choose his allies as his _hunter's bond,_ not an animal companion.

**Gained:** At 4th Level

**Dandy Spells (Su)**

**Alters:** Spellcasting

**Flavor:** The dandy gains a different sort of spellcasting than most rangers.

**Info:** A dandy uses his Charisma instead of his Wisdom to determine spells per day, DCs, and
other factors related to spellcasting. He casts spells spontaneously from the bard spell list
(rather than the ranger spell list) with the same number of spells known and spells per day as a
[medium](ref/class/medium) of his ranger level.

**Gained:** At 4th Level

**Party Crasher (Ex)**

**Ability:** The dandy is able to finagle his way into fancy parties, kings' balls, and other social
events meant for the cream of society. To do so, he must attempt a DC 25 Diplomacy check, which
takes 1d4 hours. If he succeeds, he finds himself an invitation, an invitee looking for a date, a
staff member willing to look the other way, or some other way to enter the party. This does not
allow him to break into restricted areas or to infiltrate strictly closed gatherings, such as secret
meetings; it only allows him access to social events.

**Gained:** At 7th Level

**Replaces:** Woodland stride
