+++
id = "ref/spell/orb-of-the-void"
kind = "spell"
title = "Orb of the Void"
aon = "SpellDisplay.aspx?ItemName=Orb%20of%20the%20Void"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "orb_of_the_void", path = "json/spells7.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "230"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, M (a black gemstone of any kind worth 50 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "1-ft.-diameter sphere" },
]
duration = "1 round/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 8: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a black gemstone of any kind worth 50 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
Effect: 1-ft.-diameter sphere
:::

You create a small weightless sphere of pure negative energy. As a move action, you can move it up
to 30 feet per round in any direction. If it enters a space with a living creature, it stops moving
for the round and that creature gains one negative level (Fortitude negates). Any creature passing
through or ending its turn in the space occupied by the sphere gains one negative level (Fortitude
negates). Twenty-four hours after gaining a negative level from the sphere, the subject must make a
Fortitude saving throw (the DC of this save is equal to the DC of this spell) for each negative
level. If the save succeeds, that negative level is removed. If it fails, that negative level
becomes permanent.

If more than one orb (from different castings of the spell) enters the same space, the orbs
automatically fuse together. The resulting orb uses the higher of the two orbs' DCs as its DC and
whichever duration has more time left. If the orbs are from different casters, each must make an
opposed Intelligence check to move the sphere.

An undead creature that passes through or ends its turn in the space occupied by the orb gains 2d4 ×
5 temporary hit points for 1 hour.
