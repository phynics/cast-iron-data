+++
id = "ref/spell/mages-sword"
kind = "spell"
title = "Mage's Sword"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mages_sword", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, F (a miniature platinum sword worth 250 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one sword" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 7: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a miniature platinum sword worth 250 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: yes
Effect: one sword
Descriptors: force
:::

**Sources:** PRPG Core Rulebook pg 307

This spell brings into being a shimmering, sword-like plane of force. The sword strikes at any
opponent within its range, as you desire, starting in the round that you cast the spell. The sword
attacks its designated target once each round on your turn. Its attack bonus is equal to your caster
level + your Intelligence bonus or your Charisma bonus (for wizards or sorcerers, respectively) with
an additional +3 enhancement bonus. As a force effect, it can strike ethereal and incorporeal
creatures. It deals 4d6+3 points of force damage, with a threat range of 19-20 and a critical
multiplier of ×2.

The sword always strikes from your direction. It does not get a bonus for flanking or help a
combatant get one. If the sword goes beyond the spell range from you, goes out of your sight, or you
are not directing it, it returns to you and hovers.

Each round after the first, you can use a standard action to switch the sword to a new target. If
you do not, the sword continues to attack the previous round's target.

The sword cannot be attacked or harmed by physical attacks, but
[dispel magic](ref/spell/dispel-magic), [disintegrate](ref/spell/disintegrate), a
[sphere of annihilation](ref/magic-artifact/sphere-of-annihilation), or a
[rod of cancellation](ref/magic-rod/rod-of-cancellation) affects it. The sword's AC is 13 (10, +0
size bonus for Medium object, +3 deflection bonus).

If an attacked creature has [spell resistance](ref/rule/spell-resistance), the resistance is checked
the first time mage's sword strikes it. If the sword is successfully resisted, the spell is
dispelled. If not, the sword has its normal full effect on that creature for the duration of the
spell.
