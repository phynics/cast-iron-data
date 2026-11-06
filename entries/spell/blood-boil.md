+++
id = "ref/spell/blood-boil"
kind = "spell"
title = "Blood Boil"
source_ids = ["magical-marketplace"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blood_boil", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of mercury)"
range = "touch"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "3 rounds"
saving_throw = "Fortitude negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Arcanist, Magus, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of mercury)
Range: touch
Duration: 3 rounds
Saving throw: Fortitude negates (see text)
Spell resistance: yes
Target: one living creature
:::

**Sources:** Magical Marketplace pg 24

The temperature of the target creature's blood (or other similar body fluid) begins to rise over the
next 3 rounds during the caster's turn. Each round starting with the first, the target creature
attempts a new saving throw at the start of the caster's turn to resist that round's effect. A
successful save does not end the spell effect, but does prevent that round's effect. On the round
that this spell is cast, the target becomes fatigued. On the next round, as the blood temperature
begins to rise, the target's capillaries burst, dealing 1d6 points of Constitution damage to the
target. On the third and final round, the target's blood begins to boil; the spell deals 1d6 points
of damage per caster level (to a maximum of 15d6), and - if the target is still alive - the target
becomes exhausted rather than fatigued.
