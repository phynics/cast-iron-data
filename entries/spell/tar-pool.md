+++
id = "ref/spell/tar-pool"
kind = "spell"
title = "Tar Pool"
aon = "SpellDisplay.aspx?ItemName=Tar%20Pool"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tar_pool", path = "json/spells10.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "246"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["earth", "fire"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a ball of hardened tar)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "20-ft.-radius burst" },
]
duration = "1 round/level"
saving_throw = "Reflex partial, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Summoner\
6: Arcanist, Druid, Hunter, Sorcerer, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a ball of hardened tar)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Reflex partial, see text
Spell resistance: no
Area: 20-ft.-radius burst
Descriptors: earth, fire
:::

You convert a layer of the ground to hot tar. Creatures in the area when the tar appears take 1d6
points of fire damage per two caster levels (maximum of 10d6) and must succeed at a Reflex save or
become entangled. An entangled creature receives a saving throw each round to free itself from the
tar, and can also attempt to free itself by spending a move action to attempt a Strength check or
Escape Artist check (DC = spell saving throw DC).

It costs 2 squares of movement to enter a square in the area of effect, and the DC of Acrobatics
checks within the area of effect increases by 5. The area is difficult terrain. A creature that
moves into or starts its turn in the area takes 2d6 points of fire damage and must reattempt this
Reflex save or become entangled. A creature that falls prone in the area takes a -4 penalty on its
Reflex save against the tar and on Strength and Escape Artist checks to escape the tar.

A creature that escapes the tar still takes fire damage from the tar until the spell ends or that
creature spends a full-round action removing the tar. A creature with tar on it takes a -4 penalty
on Acrobatics and Fly checks made to fly with wings or similar appendages.
