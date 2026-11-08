+++
id = "ref/arc-druid/troll-fury"
kind = "archetype"
title = "Troll Fury"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "troll_fury", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]

[fields]
kind = "archetype"
replaces = ["Wild empathy", "Resist nature's lure", "Venom immunity"]
+++

**Sources:** Monster Codex pg 224\
Troll furies combine a druid's love of natural balance with a single-minded devotion to the welfare
of the troll tribe. Trolls require a lot of prey to keep fed, and if their hunting grounds are upset
by incursions of other monsters, civilized deforestation, or careless trolls who eat more than they
need, a troll tribe can find itself without a sustainable food source.

Troll furies take the long view on sustainability, protecting the trolls' territory from gluttonous
trolls and outsiders alike, and even hunting down tribal enemies when necessary. Holding themselves
aloof from the rest of troll society, troll furies command great respect and can rally a region's
trolls quickly to deal with threats to their existence and the health of their environment.

**Prerequisites:** [Troll](ref/monster/troll)

**Inspire Fervor (Ex)**

**Gained:** At 1st Level

**Replaces:** Wild empathy

**Standard:** Once per day, a troll fury can chant over another troll within 30 feet, bolstering it
against fear and improving its combat abilities. This works like the
[inspire courage](ref/performance/inspire-courage) bard ability, but affects only one troll and
lasts 1 minute. The troll fury uses her druid level as her bard level to determine the effects of
this ability.

**Chosen Prey (Ex)**

**Ability:** A troll fury can change her favored enemy type once per week by performing a ritual
that takes 1 hour to perform.

**Choice:** A troll fury can select one creature type from the ranger's
[favored enemy](ref/ability/favored-enemy) list and gains a favored enemy bonus against that
creature type with an effective ranger level equal to her druid level. This ability never grants the
troll fury favored enemy bonuses against a second favored enemy creature type.

**Gained:** At 4th Level

**Replaces:** Resist nature's lure

**Special:** If a troll fury already has a favored enemy from another class, the levels from the
classes that grant favored enemies stack with this one to determine the favored enemy bonuses, and
in this case she can gain other favored enemy creature types.

**Troll Fury's Mark (Su)**

**Gained:** At 9th Level

**Passive:** Each time a troll fury or her animal companion damages a creature with a natural
attack, the troll fury gains a +10 insight bonus on Survival checks to track that creature for 24
hours. The duration of this ability does not stack with itself. Each time the troll fury or her
animal companion hits the target, this ability lasts for the next 24 hours.

**Replaces:** Venom immunity
