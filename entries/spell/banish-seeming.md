+++
id = "ref/spell/banish-seeming"
kind = "spell"
title = "Banish Seeming"
aon = "SpellDisplay.aspx?ItemName=Banish%20Seeming"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "banish_seeming", path = "json/spells12.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "204"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Inquisitor", level = 3 },
  { class = "Psychic", level = 5 },
  { class = "Witch", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a cold iron nail)"
range = "touch"
effects = [
  { label = "Target", value = "one creature or object" },
]
duration = "instantaneous and 1 round/level; see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Inquisitor\
5: Psychic, Witch
Casting time: 1 standard action
Components: V, S, M (a cold iron nail)
Range: touch
Duration: instantaneous and 1 round/level; see text
Saving throw: none
Spell resistance: no
Target: one creature or object
:::

With a melee touch attack you can dispel an illusion or return a creature to its natural form. This
functions as [dispel magic](ref/spell/dispel-magic) directed at the effect in question, except you
receive a +2 enhancement bonus on your dispel check and you can only dispel illusions or changes in
form created by supernatural effects or spells. If multiple effects are changing the creature's
appearance, you can dispel one such effect for every four caster levels you possess, starting with
the highest caster level spells and proceeding to spells with lower caster levels. The caster level
for supernatural abilities such as change shape is equal to the target creature's Hit Dice. A
creature returned to its natural form by banish seeming is prevented from changing its form again
for a number of rounds equal to your caster level.

Banish seeming has no effect on nonmagical means of changing appearance, such as that provided by a
disguise or extraordinary ability.
