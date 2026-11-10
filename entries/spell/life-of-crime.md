+++
id = "ref/spell/life-of-crime"
kind = "spell"
title = "Life of Crime"
aon = "SpellDisplay.aspx?ItemName=Life%20of%20Crime"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "life_of_crime", path = "json/spells6.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "218"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["curse", "mind-affecting"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 8 },
  { class = "Bard", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 8 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, M (a black mask)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Antipaladin\
6: Bard, Mesmerist, Skald\
8: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a black mask)
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: curse, mind-affecting
:::

You unleash the basest instincts of iniquity in the target and cause them to become his overriding
reason for being. The target neither gains nor provides benefit from teamwork feats or the aid
another action and can't willingly accept harmless magical effects from others.

The target moves by Stealth whenever possible, and lies and deceives others instinctively to further
its personal agenda. In addition, when the target is conscious, it must succeed at a Will save
against the spell's save DC each hour (or each round during combat or a similarly stressful
situation) or behave as if affected by a crime wave spell for 1 round.

Life of crime is particularly difficult to remove. Only a [remove curse](ref/spell/remove-curse)
with a higher caster level than life of crime's caster level, or a
[limited wish](ref/spell/limited-wish), [wish](ref/spell/wish), or [miracle](ref/spell/miracle) can
remove its effects.
