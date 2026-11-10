+++
id = "ref/spell/zone-of-silence"
kind = "spell"
title = "Zone of Silence"
aon = "SpellDisplay.aspx?ItemName=Zone%20of%20Silence"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "zone_of_silence", path = "json/spells16.json" },
]
[[sources]]
publication = "core-rulebook"
page = "371"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Bard", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Skald", level = 4 },
]
casting_time = "1 round"
components = "V, S"
range = "personal"
effects = [
  { label = "Area", value = "5-ft.-radius emanation centered on you" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Bard, Mesmerist, Skald
Casting time: 1 round
Components: V, S
Range: personal
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Area: 5-ft.-radius emanation centered on you
Subschool: Glamer
Descriptors: glamer
:::

By casting zone of silence, you manipulate sound waves in your immediate vicinity so that you and
those within the spell's area can converse normally, yet no one outside can hear your voices or any
other noises from within, including language-dependent or sonic spell effects. This effect is
centered on you and moves with you. Anyone who enters the zone immediately becomes subject to its
effects, but those who leave are no longer affected. Note, however, that a successful DC 20
Linguistics check to read lips can still reveal what's said inside a zone of silence.
