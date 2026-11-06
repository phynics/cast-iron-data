+++
id = "ref/umr/energy-drain"
kind = "rule"
title = "Energy Drain"
source_ids = ["bestiary-5"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "energy_drain", path = "json/umr.json" },
]

[fields]
kind = "none"
+++

## Energy Drain (Su)

**Sources:** Bestiary 5 pg 292\
This attack happens automatically when a melee or ranged attack hits. Each successful energy drain
bestows one or more [negative levels](ref/rule/energy-drain-and-negative-levels) (the creature's
description specifies how many). If the creature confirms a critical hit with an attack that
includes energy drain, it inflicts twice the listed number of negative levels. Unless otherwise
specified in the creature's description, a draining creature gains 5 temporary hit points for each
negative level it inflicts on an opponent. These temporary hit points last for a maximum of 1 hour.
Negative levels remain until 24 hours have passed or until they are removed with a spell such as
[restoration](ref/spell/restoration). If a negative level is not removed before 24 hours have
passed, the affected creature must attempt a Fortitude save (DC = 10 + 1/2 draining creature's
racial HD + draining creature's Charisma modifier; the exact DC is given in the creature's
descriptive text). On a success, the negative level goes away with no harm to the creature. On a
failure, the negative level becomes permanent. A separate saving throw is required for each negative
level.

**Format**

**Details:** energy drain (2 levels, DC 18)

**Location**

**Details:** Special Attacks and individual attacks
