+++
id = "ref/spell/antitech-field"
kind = "spell"
title = "Antitech Field"
aon = "SpellDisplay.aspx?ItemName=Antitech%20Field"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "antitech_field", path = "json/spells.json" },
]
[[sources]]
publication = "technology-guide"
page = "8"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (pinch of rust)"
range = "10 ft."
effects = [
  { label = "Target", value = "10-ft.-radius emanation centered on you" },
]
duration = "1 minute/level (D)"
saving_throw = "Fortitude partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 6: Druid, Hunter\
7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (pinch of rust)
Range: 10 ft.
Duration: 1 minute/level (D)
Saving throw: Fortitude partial (see text)
Spell resistance: yes
Target: 10-ft.-radius emanation centered on you
:::

You bring into being a mobile, hemispherical energy field that prevents technological objects,
signals, and creatures from entering.

An antitech field suppresses any technological effect used within, brought into, or deployed into
the area, but does not negate it. Time spent within an antitech field counts against the suppressed
effect's duration.

Robots and other technological constructs that come in contact with an antitech field must attempt a
Fortitude saving throw each round they remain in the field. Failure indicates a creature can take no
actions that round and is considered to be helpless. Success indicates a creature can take either
one move action or one standard action that round. Partially technological creatures like androids
or cyborgs are merely staggered if they fail this saving throw. Note that cybernetic equipment does
not function in an antitech field, and all benefits granted by such gear are suppressed.

Non-technological creatures can enter the area, as can low-tech missiles like sling stones and
arrows. High-tech missiles such as bullets and missiles immediately halt upon contacting the field,
and either drop to the ground harmlessly or detonate. An antitech field doesn't stop rays created by
magical sources, but does stop rays fired from beam weapons such as lasers. The antitech field does
not offer any protection against explosions caused by technological explosives detonating against
it-thus, creatures within the field could still take damage from a rocket that explodes against it.

If a creature is larger than the area enclosed by the barrier, any part of the creature that lies
outside the barrier is unaffected by the field.

This spell can be used only defensively, not aggressively. Forcing an abjuration barrier against
creatures that the spell keeps at bay collapses the barrier.
