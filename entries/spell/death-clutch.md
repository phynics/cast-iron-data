+++
id = "ref/spell/death-clutch"
kind = "spell"
title = "Death Clutch"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "death_clutch", path = "json/spells3.json" },
]
[[sources]]
publication = "horror-adventures"
page = "115"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death", "evil"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Druid", level = 9 },
  { class = "Oracle", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 8: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Witch, Wizard\
9: Druid
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude partial (see text)
Spell resistance: yes
Target: one living creature
Descriptors: death, evil
:::

Chanting an unholy litany, you reach out with a grasping motion toward your target and cause its
heart to leap out of its chest and into your hand. A target with 200 or fewer hit points remaining
that fails its saving throw is instantly reduced to a number of negative hit points equal to your
caster level or its Constitution score - 1, whichever is less negative. The creature is staggered
until the beginning of your next turn, at which point it dies. If the affected creature receives a
regenerate spell before the beginning of your next turn, the creature gains the normal benefits of
that spell and, thanks to its heart's regeneration, it doesn't immediately die when your next turn
begins. If a creature that dies from death clutch is brought back from the dead by a breath of life
or raise dead spell, it must also be targeted with regenerate on the following round to restore its
missing heart or be unable to return to life.

A target with 201 or more hit points that fails its saving throw manages to keep its heart from
leaping out of its chest, but it is still staggered for 1 minute and takes 1d4 points of
Constitution drain and 1d4 points of Constitution bleed.

Regardless of its current hit points, if the target succeeds at its Fortitude save, it is still
staggered until the beginning of your next turn as it feels its heart wrenching within its chest.
