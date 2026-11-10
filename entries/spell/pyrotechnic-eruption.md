+++
id = "ref/spell/pyrotechnic-eruption"
kind = "spell"
title = "Pyrotechnic Eruption"
aon = "SpellDisplay.aspx?ItemName=Pyrotechnic%20Eruption"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pyrotechnic_eruption", path = "json/spells15.json" },
]
[[sources]]
publication = "horror-adventures"
page = "125"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of coal)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "see text"
saving_throw = "Reflex half (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Bloodrager\
4: Arcanist, Magus, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a pinch of coal)
Range: medium (100 ft. + 10 ft./level)
Duration: see text
Saving throw: Reflex half (see text)
Spell resistance: yes
Target: one creature
Descriptors: fire
:::

The caster causes jets of flame to erupt from the ground and surround the target. The target takes
1d6 points of damage per caster level (maximum 15d6) unless it succeeds at a Reflex save for half
damage. The blaze surrounds the target for the duration of the spell, forcing the creature to
attempt a new save each round. Each round, the damage dealt is reduced to half as many d6; the spell
expires when it would deal no damage. If the target moves, the pyrotechnic eruption follows, even if
the target teleports.

Anyone attempting to touch the target takes damage, using the same amount of dice as the last time
the target attempted a save (Reflex half). A creature can take the place of the target by bull
rushing or grappling it and switching places. The new creature then automatically takes the current
round's damage with no saving throw and can begin to attempt Reflex saves starting on its next turn.
