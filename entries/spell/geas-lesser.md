+++
id = "ref/spell/geas-lesser"
kind = "spell"
title = "Lesser Geas"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "geas_lesser", path = "json/spells13.json" },
]
[[sources]]
publication = "core-rulebook"
page = "288"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["curse", "language-dependant", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Inquisitor", level = 4 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 round"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature with 7 HD or less" },
]
duration = "1 day/level or until discharged (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Mesmerist, Skald\
4: Arcanist, Inquisitor, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Target: one living creature with 7 HD or less
Duration: 1 day/level or until discharged (D)
Saving throw: Will negates
Spell resistance: yes
Subschool: Compulsion
Descriptors: curse, language-dependant, mind-affecting
:::

A lesser geas places a magical command on a creature to carry out some service or to refrain from
some action or course of activity, as desired by you. The creature must have 7 or fewer HD and be
able to understand you. While a geas cannot compel a creature to kill itself or perform acts that
would result in certain death, it can cause almost any other course of activity.

The geased creature must follow the given instructions until the geas is completed, no matter how
long it takes.

If the instructions involve some open-ended task that the recipient cannot complete through his own
actions, the spell remains in effect for a maximum of 1 day per caster level. A clever recipient can
subvert some instructions.

If the subject is prevented from obeying the lesser geas for 24 hours, it takes a -2 penalty to each
of its ability scores. Each day, another -2 penalty accumulates, up to a total of -8. No ability
score can be reduced to less than 1 by this effect. The ability score penalties are removed 24 hours
after the subject resumes obeying the lesser geas.

A lesser geas (and all ability score penalties) can be ended by
[break enchantment](ref/spell/break-enchantment), [limited wish](ref/spell/limited-wish),
[remove curse](ref/spell/remove-curse), [miracle](ref/spell/miracle), or [wish](ref/spell/wish).
[Dispel magic](ref/spell/dispel-magic) does not affect a lesser geas.
