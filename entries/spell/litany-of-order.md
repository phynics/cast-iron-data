+++
id = "ref/spell/litany-of-order"
kind = "spell"
title = "Litany of Order"
aon = "SpellDisplay.aspx?ItemName=Litany%20of%20Order"
source_ids = ["disciples-doctrine"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "litany_of_order", path = "json/spells6.json" },
]
[[sources]]
publication = "disciples-doctrine"
page = "13"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["language-dependant", "lawful"]
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
Descriptors: language-dependant, lawful
:::

By shouting a forceful litany of strictures, you make a chaotic creature more susceptible to the
attacks of lawful creatures. If the target is chaotic, it takes double the normal damage from
attacks made by creatures that have a lawful aura from a class feature or by creatures that have the
lawful subtype. If the target also has the chaotic subtype, when it is hit with attacks made by
creatures with a lawful aura, it is also sickened for 1 round. If this spell targets a nonchaotic
creature (or one that lacks the chaotic subtype), it has no effect and the spell is wasted. While
subject to this spell, the target cannot be the target of another spell that has the word "litany"
in the title.
