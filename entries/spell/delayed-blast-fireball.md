+++
id = "ref/spell/delayed-blast-fireball"
kind = "spell"
title = "Delayed Blast Fireball"
aon = "SpellDisplay.aspx?ItemName=Delayed%20Blast%20Fireball"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "delayed_blast_fireball", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/fireball" },
]
[[sources]]
publication = "core-rulebook"
page = "265"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a ball of bat guano and sulfur)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "20-ft.-radius spread" },
]
duration = "5 rounds or less; see text"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a ball of bat guano and sulfur)
Range: long (400 ft. + 40 ft./level)
Duration: 5 rounds or less; see text
Saving throw: Reflex half
Spell resistance: yes
Area: 20-ft.-radius spread
Descriptors: fire
:::

This spell functions like [fireball](ref/spell/fireball), except that it is more powerful and can
detonate up to 5 rounds after the spell is cast. The burst of flame deals 1d6 points of fire damage
per caster level (maximum 20d6). The glowing bead created by delayed blast fireball can detonate
immediately if you desire, or you can choose to delay the burst for as many as 5 rounds. You select
the amount of delay upon completing the spell, and that time cannot change once it has been set
unless someone touches the bead. If you choose a delay, the glowing bead sits at its destination
until it detonates. A creature can pick up and hurl the bead as a thrown weapon (range increment 10
feet). If a creature handles and moves the bead within 1 round of its detonation, there is a 25%
chance that the bead detonates while being handled.
