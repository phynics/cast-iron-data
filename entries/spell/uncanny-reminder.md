+++
id = "ref/spell/uncanny-reminder"
kind = "spell"
title = "Uncanny Reminder"
aon = "SpellDisplay.aspx?ItemName=Uncanny%20Reminder"
source_ids = ["chronicle-of-legends"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "uncanny_reminder", path = "json/spells11.json" },
]
[[sources]]
publication = "chronicle-of-legends"
page = "14"

[fields]
kind = "spell"
school = "conjuration"
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Summoner", level = 6 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 round"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Mesmerist, Summoner, Unchained Summoner\
8: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 round
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
:::

This spell creates an animated replica of the target drawn from the target's subconscious. This
living memory is an animated form of the target's negative thoughts and emotions and is intent on
destroying the target entirely. The living memory appears to be an exact replica of the target
creature, but upon inspection it is obviously a construct. It uses the statistics of a
[clockwork angel](ref/monster/clockwork-clockwork-angel) except that it has an Intelligence of 10
and does not have the clockwork trait, the enhance weapon ability, or vulnerability to electricity.
If the living memory is destroyed, it vanishes entirely, including any replicas of equipment.

You do not control the living memory. The living memory constantly attacks the target. The nature of
the living memory causes the target to become unsettled. Roll on the following table to determine
how the target acts while the living memory is in sight. If the result offers a saving throw, the DC
is equal to that of this spell. The result remains in effect for as long as the living memory is in
sight. If the target loses sight of the living memory and then sees it again, roll on the chart
again. d% Behavior

|d%|Behavior|
| --- | --- |
|01-20|Target is unaffected|
|21-35|Target takes a -2 penalty on attack rolls|
|36-50|Target takes a -2 penalty on saving throws|
|51-65|Target takes a -4 penalty on ability checks, attack rolls, saving throws, skill checks, and weapon damage rolls|
|66-75|Target is staggered (Fortitude negates)|
|76-85|Target is fascinated by the living memory (Will negates)|
|86-95|Target is frightened by the living memory (Will negates)|
|96-100|Target is nauseated (Fortitude negates)|
