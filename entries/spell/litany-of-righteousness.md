+++
id = "ref/spell/litany-of-righteousness"
kind = "spell"
title = "Litany of Righteousness"
aon = "SpellDisplay.aspx?ItemName=Litany%20of%20Righteousness"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "litany_of_righteousness", path = "json/spells6.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "235"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["good", "language-dependant"]
levels = [
  { class = "Inquisitor", level = 3 },
  { class = "Paladin", level = 2 },
]
casting_time = "1 swift action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Paladin\
3: Inquisitor
Casting time: 1 swift action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: good, language-dependant
:::

Calling down a litany of anathema, you make an evil more susceptible to the attacks of good
creatures. If the target is evil, it takes double damage from attacks made by creatures with a good
aura (from a class feature or as a creature with the good subtype). If the target also has the evil
subtype; when it is hit with attacks made by creatures with a good aura, it is also dazzled for 1d4
rounds. If this spell targets a nonevil creature (or one that lacks the evil subtype), it has no
effect, and the spell is wasted.

While subject to this spell, the target cannot be the target of another spell that has the word
"litany" in the title.
