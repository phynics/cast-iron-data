+++
id = "ref/spell/seeds-of-influence-greater"
kind = "spell"
title = "Greater Seeds of Influence"
aon = "SpellDisplay.aspx?ItemName=Seeds%20of%20Influence%2C%20Greater"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "seeds_of_influence_greater", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/seeds-of-influence" },
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

### Greater Seeds of Influence

This spell functions as [seeds of influence](ref/spell/seeds-of-influence), except that if the
target is protected by a spell that grants immunity, [spell resistance](ref/rule/spell-resistance),
or a saving throw bonus against a divination or mind-affecting spell you cast on the target, you can
attempt caster level checks to dispel each such effect before applying the effects of those
protections against the spell. The DC of the caster level check to dispel each effect is equal to
11 + the effect's caster level. Such spells cast on the target while greater seeds of influence is
active grant no protection against greater seeds of influence.
