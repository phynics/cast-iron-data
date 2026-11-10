+++
id = "ref/arc-ranger/horse-lord"
kind = "archetype"
title = "Horse Lord"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Horse%20Lord"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "horse_lord", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "advanced-players-guide"
page = "125"

[fields]
kind = "archetype"
replaces = ["Hunter's bond", "Camouflage", "Hide in plain sight"]
replaces_features = ["hunter-s-bond", "camouflage", "hide-in-plain-sight"]
+++

Rangers of the plains use horses or other riding beasts to hunt their lands, forging a near-mystical
relationship with their mounts. Horse lords are unparalleled mounted combatants, the envy of even
the most dedicated cavalier. Though called "horse lords" as a generic term, these rangers are not
restricted to horses for their animal companions - any creature the ranger can ride is included in
these abilities. A horse lord has the following class features.

**Combat Style Feat (Ex)**

**Choice:** A horse lord must choose the mounted [combat style](ref/ability/combat-styles).

**Gained:** At 2nd Level

**Mounted Bond (Ex)**

**Ability:** The horse lord forms a bond with an animal he can use as a mount, which becomes his
[animal companion](ref/sidekick/animal-companion). A Medium ranger can select a
[camel](ref/companion/camel) or a [horse](ref/companion/horse). A small ranger can select a
[pony](ref/companion/pony) or [wolf](ref/companion/wolf), but can also select a
[boar](ref/companion/boar) or [dog](ref/companion/dog) if he is at least 7th level. This ability
functions like the druid animal companion ability except that the ranger's effective druid level is
equal to his ranger level - 3.

**Gained:** At 4th Level

**Passive:** The ranger gains a +2 bonus on Handle Animal and Ride checks with his animal companion
mount.

**Replaces:** Hunter's bond

**Strong Bond (Ex)**

**Ability:** The ranger's effective druid level for his mount is now equal to his ranger level.

**Flavor:** The horse lord strengthens his bond with his mount.

**Gained:** At 12th Level

**Replaces:** Camouflage

**Spiritual Bond (Su)**

**Ability:** The horse lord can grant his animal companion
[temporary hit points](ref/rule/temporary-hit-points) equal to his ranger level once per day. While
these temporary hit points last, when his mount is within 30 feet of the him, he can choose to share
the damage taken by his mount as if using [shield other](ref/spell/shield-other).

**Gained:** At 17th Level

**Replaces:** Hide in plain sight
