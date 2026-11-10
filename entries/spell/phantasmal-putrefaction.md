+++
id = "ref/spell/phantasmal-putrefaction"
kind = "spell"
title = "Phantasmal Putrefaction"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phantasmal_putrefaction", path = "json/spells7.json" },
]
[[sources]]
publication = "horror-adventures"
page = "124"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["fear", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be omore than 30 ft. apart" },
]
duration = "1 round/level (D)"
saving_throw = "Will disbelief, then Fortitude partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Medium\
5: Mesmerist\
6: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: Will disbelief, then Fortitude partial (see text)
Spell resistance: yes
Target: one creature/level, no two of which can be omore than 30 ft. apart
Subschool: Phantasm
Descriptors: fear, mind-affecting
:::

You implant within the minds of your targets the illusion that their skin is rotting away, large
rents are appearing all over their bodies, and their internal organs are spilling out into a putrid
half-liquid mass at their feet. Those who fail to disbelieve phantasmal putrefaction immediately
take 1d4 points of Wisdom damage. This damage occurs only once. Each round at the beginning of its
turn, an affected target receives another Will save to disbelieve the effect, and targets that fail
must succeed at a Fortitude save or faint, falling asleep as per [sleep](ref/spell/sleep) (except
that it isn't a magical sleep effect). Waking up doesn't end the spell for a target; it must
continue to attempt Will saves to disbelieve and Fortitude saves to avoid fainting each round until
the spell ends or the target successfully disbelieves.

Targets of the spell perceive everyone else around them to be rotting away, but other creatures see
no visible effect of the spell, so they, in addition to those who disbelieve, can communicate the
nature of the illusion to allies, providing those allies with a +4 bonus on the saving throw to
disbelieve.

If your campaign uses [the sanity system](ref/rule/sanity), a creature takes 1d8 points of sanity
damage instead of Wisdom damage.
