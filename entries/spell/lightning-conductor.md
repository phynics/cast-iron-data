+++
id = "ref/spell/lightning-conductor"
kind = "spell"
title = "Lightning Conductor"
source_ids = ["elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lightning_conductor", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["air"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 2 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a miniature metal rod)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Bloodrager\
3: Arcanist, Druid, Hunter, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a miniature metal rod)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: air
:::

**Sources:** Elemental Master's Handbook pg 18

You become capable of absorbing electricity with your body. For the duration, you absorb all
electricity damage dealt to you until you have stored a total of 18 points of damage. Any excess
damage affects you as normally. The energy remains stored until it is expended or the spell expires.

If you have at least 6 points of damage stored, you can expend all the energy stored in you as a
swift action, charging your hand or a metal weapon in your hand. As a standard action while your
hand is charged, you can make a melee touch attack that doesn't provoke attacks of opportunity, or
you can shoot the energy as a ray with a range of 30 feet. If the attack hits, you deal 1d6 points
of electricity damage for every 6 points stored and the energy is expended (any remaining points are
wasted). A weapon charged with this energy deals the damage as extra damage the first time you score
a hit with the weapon. If your hand or weapon is still charged at the end of your turn, or if the
charged weapon leaves your hand before the end of the turn, the energy dissipates harmlessly.

Once you have spent the absorbed energy, or if the absorbed energy dissipates, you can absorb more
electricity damage. The maximum amount of damage you can store in your body at a time increases by 6
points for every 2 levels beyond 5th (to a maximum of 60 points of damage at 19th level).

If you are immune to electricity or have any amount of electricity resistance, you cannot absorb or
expend energy with this spell.
