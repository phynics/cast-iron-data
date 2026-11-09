+++
id = "ref/spell/animate-rope"
kind = "spell"
title = "Animate Rope"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animate_rope", path = "json/spells.json" },
]
[[sources]]
publication = "core-rulebook"
page = "242"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one rope-like object, length up to 50 ft. + 5 ft./level; see text" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Bard, Mesmerist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: one rope-like object, length up to 50 ft. + 5 ft./level; see text
:::

You can animate a nonliving rope-like object. The maximum length assumes a rope with a 1-inch
diameter. Reduce the maximum length by 50% for every additional inch of thickness, and increase it
by 50% for each reduction of the rope's diameter by half.

The possible commands are "coil" (form a neat, coiled stack), "coil and knot," "loop," "loop and
knot," "tie and knot," and the opposites of all of the above ("uncoil," and so forth). You can give
one command each round as a move action, as if directing an active spell.

The rope can enwrap only a creature or an object within 1 foot of it - it does not snake outward -
so it must be thrown near the intended target. Doing so requires a successful ranged touch attack
roll (range increment 10 feet). A typical 1-inch-diameter hemp rope has 2 hit points, AC 10, and
requires a DC 23 Strength check to burst it. The rope does not deal damage, but it can be used as a
trip line or to cause a single opponent that fails a Reflex saving throw to become entangled. A
creature capable of spellcasting that is bound by this spell must make a
[concentration](ref/rule/concentration) check with a DC of 15 + the spell's level to cast a spell.
An entangled creature can slip free with a DC 20 Escape Artist check.

The rope itself and any knots tied in it are not magical.

The spell cannot affect objects carried or worn by a creature.
