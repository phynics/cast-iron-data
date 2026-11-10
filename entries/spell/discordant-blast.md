+++
id = "ref/spell/discordant-blast"
kind = "spell"
title = "Discordant Blast"
aon = "SpellDisplay.aspx?ItemName=Discordant%20Blast"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "discordant_blast", path = "json/spells3.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "216"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["sonic"]
levels = [
  { class = "Bard", level = 4 },
  { class = "Skald", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "10 ft. or 30 ft."
effects = [
  { label = "Area", value = "see text" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Bard, Skald
Casting time: 1 standard action
Components: V, S
Range: 10 ft. or 30 ft.
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Area: see text
Descriptors: sonic
:::

You create a wave of thunder and force, either in a 10-foot-radius burst centered on you or in
30-foot cone-shaped burst. Creatures in the area take 3d6 points of sonic damage and are pushed away
as if bull rushed. Make a combat maneuver check and apply its results to each creature in the area.
Your CMB for this bull rush is equal to your caster level plus your Charisma modifier. This bull
rush does not provoke an attack of opportunity. A discordant blast cannot penetrate a
[silence](ref/spell/silence) spell (or any similar magical silence effect).
