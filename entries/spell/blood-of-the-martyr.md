+++
id = "ref/spell/blood-of-the-martyr"
kind = "spell"
title = "Blood of the Martyr"
source_ids = ["chronicle-of-the-righteous"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blood_of_the_martyr", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Cleric, Oracle, Warpriest\
3: Inquisitor
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: one living creature
:::

**Sources:** Chronicle of the Righteous pg 50

You cause the target to bleed from every orifice, and her organs and blood become suffused with
positive energy. If the subject fails her Fortitude save, she takes 1d6 points of bleed damage per 4
caster levels (to a maximum of 4d6 at 16th level) when you cast this spell. Any creature that takes
a full-round action to sup the blood of the bleeding subject heals a number of hit points equal to
twice as many as the subject lost that round due to the bleed effect. The subject must be willing or
helpless to sup her blood, which provokes attacks of opportunity. Only one creature can be healed in
this way per round. The subject can lick her own wounds in this way to regain half as many hit
points as she lost that round. If the bleeding effect is stopped or the spell's duration ends, the
subject's blood no longer heals those who drink it, though in the latter case the subject continues
to bleed until the bleeding is stopped via magical healing or a successful DC 15 Heal check.
