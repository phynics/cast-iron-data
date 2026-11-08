+++
id = "ref/arc-ranger/guildbreaker"
kind = "archetype"
title = "Guildbreaker"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "guildbreaker", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]

[fields]
kind = "archetype"
replaces = ["Wild empathy", "Hunter's bond", "Woodland stride"]
alters = ["Favored enemy"]
+++

**Sources:** Ultimate Intrigue pg 41\
Some rangers aren't the type to put their steel and sweat behind fighting particular kinds of
creatures. Instead, these shrewd warriors alter their focus and dedicate their efforts to
dismantling enemy organizations. Guildbreakers stoke their enmity for their foes, and they train to
track the movements of rival organizations, and even to infiltrate these groups to gather secret
intelligence.

**Gained class skills:** bluff, dis, kl

**Lost class skills:** ha, heal, kg

**Favored Organization (Ex)**

**Ability:** When a guildbreaker selects a _favored enemy,_ he can opt to select a specific
organization, such as a particular thieves' guild, in lieu of a specific creature type. The
guildbreaker must select this option for his first _favored enemy,_ but he can choose either option
for his later _favored enemies._

**Alters:** Favored enemy

**Special:** The guildbreaker's bonuses from _favored enemy_ apply against official members of this
organization regardless of their creature type, but not against the organization's allies, paid
mercenaries, or forced labor. This ability only applies if the guildbreaker knows that the target is
a member of the organization.

**Read the City (Ex)**

**Ability:** When in an urban environment, a guildbreaker can use the Survival skill to gather
information, but only about the movements of creatures and what sort of people (races, social
classes, predominant professions, and the like) occupy the community. Unlike with the normal way to
gather information, the guildbreaker studies the signs of the city instead of asking around, so it
doesn't spread word about the nature of his questions to others.

**Flavor:** A guildbreaker spends most of his time in cities and large population centers. As a
result, he gains an innate sense of comings and goings in the hustle around him.

**Replaces:** Wild empathy

**Deep Cover (Ex, Su)**

**Flavor:** Guildbreakers may work to dismantle their enemies' power structures from within, and
they know how to gather resources and the necessary trappings in order to masquerade as a member of
those organizations.

**Gained:** At 4th Level

**Passive:** A guildbreaker adds a circumstance bonus equal to twice his _favored organization_
bonus to all Bluff and Disguise checks to appear to be a member of the organization (this does not
apply on Disguise checks to change his appearance and replace a specific member, but rather to
checks related to appear to be a general member of the organization).

**Replaces:** Hunter's bond

**Special:** The bonus on Bluff checks from _deep cover_ stacks with the guildbreaker's overall
bonus from _favored organization_ if the person he is attempting to deceive is also a member of that
organization.

A guildbreaker posing as a member of one of his _favored enemy_ organizations automatically defeats
truth-telling magic (as if under the effects of [glibness](ref/spell/glibness)), but only for the
purpose of claiming to be a member of the organization. Truth-telling magic can still expose him
with a more indirect question, such as a member of a non-religious evil organization asking the
guildbreaker for the identity of his patron deity.

**Crowd Stride (Ex)**

**At 7th Level:** A guildbreaker can slip through crowded streets with ease. His movement speed is
not reduced when moving through a crowd.

**Replaces:** Woodland stride
