+++
id = "ref/spell/phobia"
kind = "spell"
title = "Phobia"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phobia", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "fear", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (a single white hair)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one intelligent creature" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Bard, Mesmerist, Skald\
6: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a single white hair)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: one intelligent creature
Subschool: Compulsion
Descriptors: emotion, fear, mind-affecting
:::

**Sources:** Horror Adventures pg 124

You instill the target with an intense, instinctual fear of a condition or circumstance, more
powerful than the phobia lesser [madness](ref/rule/madness). You can name an energy type (acid,
cold, electricity, fire, or sonic), a hazard (such as an avalanche or earthquake), or a single
creature of the animal type or all vermin (applying when the target sees a swarm or a single Small
or larger creature). Alternatively, you can name the following specific environments: darkness
(darker than dim light, and you can't apply this phobia to a creature with natural racial
[darkvision](ref/rule/darkvision), see in darkness,
[blindsight](ref/rule/blindsight-and-blindsense), or similar senses), enclosed spaces (places that
require the creature to squeeze), heights (10 times the target's height, and you can't apply this
phobia to creatures with a natural fly speed), or water (you can't apply this phobia to aquatic
creatures or creatures with a natural swim speed).

When the target takes damage of the energy type (for an energy type phobia), or perceives the
presence of the creature, environment, or hazard, it must attempt a DC 20 Will save. If it fails, it
becomes panicked, but even if it succeeds, it becomes shaken and feels intensely uncomfortable; a
creature shaken in this way does not need to roll further saving throws against its phobia until its
shaken condition ends, even if it continues to be exposed to its phobia.

A creature panicked by phobia can begin to act normally 1 minute after it ceases being able to
perceive its phobia or after taking the energy damage if the phobia is an energy type, though the
shaken condition ends immediately after the creature can no longer perceive its phobia.
[Break enchantment](ref/spell/break-enchantment), [heal](ref/spell/heal),
[limited wish](ref/spell/limited-wish), [miracle](ref/spell/miracle), or [wish](ref/spell/wish) can
remove a phobia spell.
