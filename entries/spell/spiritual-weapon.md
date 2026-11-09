+++
id = "ref/spell/spiritual-weapon"
kind = "spell"
title = "Spiritual Weapon"
aon = "SpellDisplay.aspx?ItemName=Spiritual%20Weapon"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spiritual_weapon", path = "json/spells9.json" },
]
[[sources]]
publication = "core-rulebook"
page = "348"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "magic weapon of force" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Cleric, Inquisitor, Medium, Oracle, Shaman, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: yes
Effect: magic weapon of force
Descriptors: force
:::

A weapon made of force appears and attacks foes at a distance, as you direct it, dealing 1d8 force
damage per hit, + 1 point per three caster levels (maximum +5 at 15th level). The weapon takes the
shape of a weapon favored by your deity or a weapon with some spiritual significance or symbolism to
you (see below) and has the same threat range and critical multipliers as a real weapon of its form.
It strikes the opponent you designate, starting with one attack in the round the spell is cast and
continuing each round thereafter on your turn. It uses your base attack bonus (possibly allowing it
multiple attacks per round in subsequent rounds) plus your Wisdom modifier as its attack bonus. It
strikes as a spell, not as a weapon, so for example, it can damage creatures that have
[damage reduction](ref/rule/damage-reduction). As a force effect, it can strike incorporeal
creatures without the reduction in damage associated with incorporeality. The weapon always strikes
from your direction. It does not get a flanking bonus or help a combatant get one. Your feats or
combat actions do not affect the weapon. If the weapon goes beyond the spell range, if it goes out
of your sight, or if you are not directing it, the weapon returns to you and hovers.

Each round after the first, you can use a move action to redirect the weapon to a new target. If you
do not, the weapon continues to attack the previous round's target. On any round that the weapon
switches targets, it gets one attack. Subsequent rounds of attacking that target allow the weapon to
make multiple attacks if your base attack bonus would allow it to. Even if the spiritual weapon is a
ranged weapon, use the spell's range, not the weapon's normal range increment, and switching targets
still is a move action.

A spiritual weapon cannot be attacked or harmed by physical attacks, but
[dispel magic](ref/spell/dispel-magic), [disintegrate](ref/spell/disintegrate), a
[sphere of annihilation](ref/magic-artifact/sphere-of-annihilation), or a
[rod of cancellation](ref/magic-rod/rod-of-cancellation) affects it. A spiritual weapon's AC against
touch attacks is 12 (10 + size bonus for Tiny object).

If an attacked creature has [spell resistance](ref/rule/spell-resistance), you make a caster level
check (1d20 + caster level) against that spell resistance the first time the spiritual weapon
strikes it. If the weapon is successfully resisted, the spell is dispelled. If not, the weapon has
its normal full effect on that creature for the duration of the spell.

The weapon that you get is often a force replica of your deity's own personal weapon. A cleric
without a deity gets a weapon based on his alignment. A neutral cleric without a deity can create a
spiritual weapon of any alignment, provided he is acting at least generally in accord with that
alignment at the time. The weapons associated with each alignment are as follows: chaos (battleaxe),
evil (light flail), good (warhammer), law (longsword).
