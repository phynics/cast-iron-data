+++
id = "ref/spell/dimensional-lock"
kind = "spell"
title = "Dimensional Lock"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dimensional_lock", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Summoner", level = 6 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "20-ft.-radius emanation centered on a point in space" },
]
duration = "1 day/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 6: Summoner\
8: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 day/level
Saving throw: none
Spell resistance: yes
Area: 20-ft.-radius emanation centered on a point in space
:::

**Sources:** PRPG Core Rulebook pg 270

You create a shimmering emerald barrier that completely blocks extradimensional travel. Forms of
movement barred include [astral projection](ref/spell/astral-projection), [blink](ref/spell/blink),
[dimension door](ref/spell/dimension-door), [ethereal jaunt](ref/spell/ethereal-jaunt),
[etherealness](ref/spell/etherealness), [gate](ref/spell/gate), [maze](ref/spell/maze),
[plane shift](ref/spell/plane-shift), [shadow walk](ref/spell/shadow-walk),
[teleport](ref/spell/teleport), and similar [spell-like abilities](ref/umr/spell-like-abilities).
Once dimensional lock is in place, extradimensional travel into or out of the area is not possible.

A dimensional lock does not interfere with the movement of creatures already in ethereal or astral
form when the spell is cast, nor does it block extradimensional perception or attack forms. Also,
the spell does not prevent summoned creatures from disappearing at the end of a summoning spell.

### Mythic Dimensional Lock

**Sources:** Mythic Adventures pg 91\
The spell doesn't interfere with your extradimensional travel spells and effects.

_Augmented (4th):_ You can augment mythic dimensional lock to redirect teleporting creatures to
another location. If you expend two uses of mythic power, designate a location that you're very
familiar with. This location must be on the same plane as you. Any creature attempting to use
extradimensional travel from outside the spell's area into that area is instead redirected to this
other location.

The creature can attempt a Spellcraft check against your caster level. If it succeeds, it's aware of
the redirection (though not the destination) and can interrupt its spellcasting, losing the spell
but not teleporting.
