+++
id = "ref/carried/bestiary/rules/universal-monster-rules/energy-drain"
kind = "rule"
title = "Energy Drain"
source_ids = ["bestiary"]
section = ["Rules", "Universal Monster Rules"]
parent = "ref/carried/bestiary/rules/universal-monster-rules"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary/Rules/Universal Monster Rules/Energy Drain", path = "bestiary/rules/universal_monster_rules.json" },
]

[fields]
kind = "none"
+++

::: statblock
Ability Type: Supernatural
:::

This attack saps a living opponent's vital energy and happens automatically when a melee or ranged
attack hits. Each successful energy drain bestows one or more negative levels (the creature's
description specifies how many). If an attack that includes an energy drain scores a critical hit,
it bestows twice the listed number of negative levels. Unless otherwise specified in the creature's
description, a draining creature gains 5 temporary hit points for each negative level it bestows on
an opponent. These temporary hit points last for a maximum of 1 hour. Negative levels remain until
24 hours have passed or until they are removed with a spell such as
_[restoration](ref/spell/restoration)_. If a negative level is not removed before 24 hours have
passed, the affected creature must attempt a Fortitude save (DC 10 + 1/2 the draining creature's
racial HD + the draining creature's Cha modifier; the exact DC is given in the creature's
descriptive text). On a success, the negative level goes away with no harm to the creature. On a
failure, the negative level becomes permanent. A separate saving throw is required for each negative
level.

## Format {#format}

energy drain (2 levels, DC 18); _Location_: Special Attacks and individual attacks.
