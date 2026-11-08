+++
id = "ref/arc-hunter/primal-companion-hunter"
kind = "archetype"
title = "Primal Companion Hunter"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "primal_companion_hunter", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]

[fields]
kind = "archetype"
replaces = ["Animal focus", "Second animal focus", "Master hunter"]
+++

**Sources:** Advanced Class Guide pg 97\
Most hunters are skilled at awakening the primal beasts inside themselves. However, some can instead
activate the primal essence within their animal companion. These primal companion hunters bestow
upon their companions the ability to suddenly manifest new and terrifying powers - throwbacks to
long-extinct beasts, bizarre mutations from extreme environments, or new abilities crafted from
generations of selective breeding.

**Primal Transformation (Su)**

**Action:** Ability

**At 15th Level:** It increases to 6.

**At 8th Level:** The number of evolution points in her pool increases to 4

**Gained:** At 1st Level

**Replaces:** Animal focus

**Usage:** 1 minute/day per hunter level; these minutes need not be consecutive, but must be spent
in 1-minute increments

A primal companion hunter can awaken a primal creature from within his animal companion. The animal
companion gains a pool of 2 evolution points that can be used to temporarily give the companion
evolutions as if it were an eidolon. A primal companion hunter uses her hunter level to determine
her effective [summoner](ref/class/summoner) level for the purpose of qualifying for evolutions and
determining their effects.

Activating these evolutions on the animal companion is a **swift action**. An animal companion
transformed in this way cannot exceed the maximum number of attacks available to the eidolon of a
summoner whose class level equals that of the hunter. While transformed in this way, the animal
companion's type changes to [magical beast](ref/type/magical-beast), though the primal companion
hunter still treats it as an animal for the purpose of the Handle Animal skill.

If a primal companion hunter's animal companion is dead, she can apply these evolutions to herself
instead of to her animal companion. Uses of this ability count toward the hunter's maximum daily
duration of evolution use.

**Primal Surge (Su)**

**Gained:** At 8th Level

**Replaces:** Second animal focus

**Special:** This ability can grant only one evolution at a time, even if the chosen evolution could
be selected multiple times. This ability can grant an evolution that allows additional evolution
points to be spent to upgrade that evolution (such as
[damage reduction](ref/evolution/damage-reduction) or [flight](ref/evolution/flight)), and any
points left over can be spent on such upgrades. This ability cannot be used to grant an upgrade to
an evolution that the companion already possesses.

**Swift:** A primal companion hunter can touch her animal companion and grant it one evolution that
costs up to 4 evolution points. The companion must meet the prerequisites of the selected evolution.
Unlike the evolutions from _primal transformation,_ this evolution is not set; it can be changed
each time the hunter uses this ability. Using _primal surge_ activates the _primal transformation_
ability on the companion if it isn't already active. This effect lasts until the hunter ends the
_primal transformation._ This does not allow a companion to exceed its maximum number of natural
attacks.

**Usage:** Once per day

**Usage:** Once per day

**Primal Master (Su)**

**Ability:** A primal companion hunter becomes in tune with his primal nature. He can activate his
companion's primal aspect as a **free action**. When using _primal surge,_ he can grant his
companion two evolutions instead of one (each costing up to 4 evolution points).

**Gained:** At 20th Level

**Replaces:** Master hunter
