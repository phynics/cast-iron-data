+++
id = "ref/spell/seeds-of-influence-greater"
kind = "spell"
title = "Greater Seeds of Influence"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "seeds_of_influence_greater", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/seeds-of-influence" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 5 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 7 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "S, M (a rose)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature" },
]
duration = "1 day/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Medium\
5: Bard, Mesmerist, Skald\
7: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: S, M (a rose)
Range: close (25 ft. + 5 ft./2 levels)
Targets: one creature
Duration: 1 day/level (D)
Saving throw: Will negates
Spell resistance: yes
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

## Seeds of Influence

**Sources:** Inner Sea Intrigue pg 62

You leave a magical trace in the mind of a creature with an attitude of at least indifferent toward
you. The target takes a cumulative -2 penalty on its Will save to negate the spell for each step by
which its attitude is better than indifferent.

The target takes a -2 penalty on saving throws against divination spells you cast. You can target
that creature with mind-affecting spells of a spell level lower than seeds of influence as if those
spells were modified by [Enlarge Spell](ref/feat/enlarge-spell) (the modified spell doesn't take
longer to cast and doesn't use a higher-level spell slot). Whenever the target succeeds at a saving
throw against a divination or mind-affecting spell you cast, seeds of influence ends for that
target. A creature can be subject to only one seeds of influence spell at a time; later castings of
seeds of influence remove any previous casting.

### Greater Seeds of Influence

**Sources:** Inner Sea Intrigue pg 62

This spell functions as [seeds of influence](ref/spell/seeds-of-influence), except that if the
target is protected by a spell that grants immunity, [spell resistance](ref/rule/spell-resistance),
or a saving throw bonus against a divination or mind-affecting spell you cast on the target, you can
attempt caster level checks to dispel each such effect before applying the effects of those
protections against the spell. The DC of the caster level check to dispel each effect is equal to
11 + the effect's caster level. Such spells cast on the target while greater seeds of influence is
active grant no protection against greater seeds of influence.
