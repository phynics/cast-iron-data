+++
id = "ref/spell/seeds-of-influence"
kind = "spell"
title = "Seeds of Influence"
aon = "SpellDisplay.aspx?ItemName=Seeds%20of%20Influence"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "seeds_of_influence", path = "json/spells15.json" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "62"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "S, M (a rose)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Medium, Mesmerist, Skald\
4: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: S, M (a rose)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level (D)
Saving throw: Will negates
Spell resistance: yes
Targets: one creature
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

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
