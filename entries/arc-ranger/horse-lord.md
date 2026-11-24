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
features = [
  { anchor = "combat-style-feat", level = 2 },
  { anchor = "mounted-bond", level = 4 },
  { anchor = "strong-bond", level = 12 },
  { anchor = "spiritual-bond", level = 17 },
]
trades = [
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["mounted-bond"] },
  { replaces = "Camouflage", feature = "camouflage", by = ["strong-bond"] },
  { replaces = "Hide in plain sight", feature = "hide-in-plain-sight", by = ["spiritual-bond"] },
]
+++

Rangers of the plains use horses or other riding beasts to hunt their lands, forging a near-mystical
relationship with their mounts. Horse lords are unparalleled mounted combatants, the envy of even
the most dedicated cavalier. Though called "horse lords" as a generic term, these rangers are not
restricted to horses for their animal companions - any creature the ranger can ride is included in
these abilities. A horse lord has the following class features.

## Combat Style Feat (Ex) {#combat-style-feat}

At 2nd level, a horse lord must choose the mounted [combat style](ref/ability/combat-styles).

## Mounted Bond (Ex) {#mounted-bond}

At 4th level, the [horse](ref/companion/horse) lord forms a bond with an animal he can use as a
mount, which becomes his [animal companion](ref/sidekick/animal-companion). A Medium ranger can
select a [camel](ref/companion/camel) or a horse. A small ranger can select a
[pony](ref/companion/pony) or [wolf](ref/companion/wolf), but can also select a
[boar](ref/companion/boar) or [dog](ref/companion/dog) if he is at least 7th level. This ability
functions like the druid animal companion ability except that the ranger's effective druid level is
equal to his ranger level - 3. The ranger gains a +2 bonus on Handle Animal and Ride checks with his
animal companion mount. This ability replaces hunter's bond.

## Strong Bond (Ex) {#strong-bond}

At 12th level, the horse lord strengthens his bond with his mount. The ranger's effective druid
level for his mount is now equal to his ranger level. This ability replaces camouflage.

## Spiritual Bond (Su) {#spiritual-bond}

At 17th level, the horse lord can grant his animal companion
[temporary hit points](ref/rule/temporary-hit-points) equal to his ranger level once per day. While
these temporary hit points last, when his mount is within 30 feet of him, he can choose to share the
damage taken by his mount as if using _[shield other](ref/spell/shield-other)_. This ability
replaces hide in plain sight.
