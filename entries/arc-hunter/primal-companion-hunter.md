+++
id = "ref/arc-hunter/primal-companion-hunter"
kind = "archetype"
title = "Primal Companion Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Primal%20Companion%20Hunter"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "primal_companion_hunter", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "advanced-class-guide"
page = "97"

[fields]
kind = "archetype"
features = [
  { anchor = "primal-transformation" },
  { anchor = "primal-surge", level = 8 },
  { anchor = "primal-master", level = 20 },
]
trades = [
  { replaces = "Animal focus", feature = "animal-focus", by = ["primal-transformation"] },
  { replaces = "Second animal focus", feature = "second-animal-focus", by = ["primal-surge"] },
  { replaces = "Master hunter", feature = "master-hunter", by = ["primal-master"] },
]
+++

Most hunters are skilled at awakening the primal beasts inside themselves. However, some can instead
activate the primal essence within their animal companion. These primal companion hunters bestow
upon their companions the ability to suddenly manifest new and terrifying powers - throwbacks to
long-extinct beasts, bizarre mutations from extreme environments, or new abilities crafted from
generations of selective breeding.

## Primal Transformation (Su) {#primal-transformation}

At first level, a primal companion hunter can awaken a primal creature from within his animal
companion as a swift action. The animal companion gains a pool of 2 evolution points that can be
used to temporarily give the companion evolutions as if it were an eidolon. A primal companion
hunter uses her hunter level to determine her effective [summoner](ref/class/summoner) level for the
purpose of qualifying for evolutions and determining their effects. At 8th level, the number of
evolution points in her pool increases to 4, and at 15th level, it increases to 6.

Activating these evolutions on the animal companion is a swift action. A primal companion hunter can
use this ability for 1 minute per day per hunter level. This duration need not to be consecutive,
but it must be spent in 1-minute increments. An animal companion transformed in this way cannot
exceed the maximum number of attacks available to the eidolon of a summoner whose class level equals
that of the hunter. While transformed in this way, the animal companion's type changes to
[magical beast](ref/type/magical-beast), though the primal companion hunter still treats it as an
animal for the purpose of the Handle Animal skill.

If a primal companion hunter's animal companion is dead, she can apply these evolutions to herself
instead of to her animal companion. Uses of this ability count toward the hunter's maximum daily
duration of evolution use. This ability replaces animal focus.

## Primal Surge (Su) {#primal-surge}

At 8th level, once per day as a swift action, a primal companion hunter can touch her animal
companion and grant it one evolution that costs up to 4 evolution points. The companion must meet
the prerequisites of the selected evolution. Unlike the evolutions from primal transformation, this
evolution is not set; it can be changed each time the hunter uses this ability. Using primal surge
activates the primal transformation ability on the companion if it isn't already active. This effect
lasts until the hunter ends the primal transformation. This does not allow a companion to exceed its
maximum number of natural attacks.

This ability can grant only one evolution at a time, even if the chosen evolution could be selected
multiple times.

This ability can grant an evolution that allows additional evolution points to be spent to upgrade
that evolution (such as [damage reduction](ref/evolution/damage-reduction) or
[flight](ref/evolution/flight)), and any points left over can be spent on such upgrades. This
ability cannot be used to grant an upgrade to an evolution that the companion already possesses.
This ability replaces second animal focus.

## Primal Master (Su) {#primal-master}

At 20th level, a primal companion hunter becomes in tune with his primal nature. He can activate his
companion's primal aspect as a free action. When using primal surge, he can grant his companion two
evolutions instead of one (each costing up to 4 evolution points). This ability replaces master
hunter.
