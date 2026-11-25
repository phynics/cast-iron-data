+++
id = "ref/spell/geas-quest"
kind = "spell"
title = "Geas/Quest"
aon = "SpellDisplay.aspx?ItemName=Geas%2FQuest"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "geas_quest", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/geas-lesser" },
]
[[sources]]
publication = "core-rulebook"
page = "288"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["compulsion"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 5 },
  { class = "Mesmerist", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "10 minutes"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 day/level or until discharged (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Inquisitor\
6: Arcanist, Bard, Cleric, Mesmerist, Oracle, Psychic, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 10 minutes
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 day/level or until discharged (D)
Saving throw: none
Spell resistance: yes
Target: one living creature
Subschool: compulsion
Descriptors: language-dependant, mind-affecting
:::

### Geas/Quest

This spell functions similarly to [lesser geas](ref/spell/geas-lesser), except that it affects a
creature of any HD and allows no saving throw.

If the subject is prevented from obeying the geas/quest for 24 hours, it takes a -3 penalty to each
of its ability scores. Each day, another -3 penalty accumulates, up to a total of -12. No ability
score can be reduced to less than 1 by this effect. The ability score penalties are removed 24 hours
after the subject resumes obeying the geas/quest.

A [remove curse](ref/spell/remove-curse) spell ends a geas/quest spell only if its caster level is
at least two higher than your caster level. [Break enchantment](ref/spell/break-enchantment) does
not end a geas/quest, but [limited wish](ref/spell/limited-wish), [miracle](ref/spell/miracle), and
[wish](ref/spell/wish) do.

Bards, sorcerers, and wizards usually refer to this spell as geas, while clerics call the same spell
quest.
