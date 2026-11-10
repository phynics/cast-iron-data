+++
id = "ref/spell/feast-on-fear"
kind = "spell"
title = "Feast on Fear"
aon = "SpellDisplay.aspx?ItemName=Feast%20on%20Fear"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "feast_on_fear", path = "json/spells4.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "181"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["emotion", "fear", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one or more living creatures (see text)" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Bard, Mesmerist, Skald\
5: Arcanist, Psychic, Shaman, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: yes
Targets: one or more living creatures (see text)
Descriptors: emotion, fear, mind-affecting
:::

Each round, as a standard action, you can target a single living creature of up to 9 HD and strike
it with terrifying waves of power. If the target fails its saving throw, it becomes panicked for 1d4
rounds, and you gain 5 temporary hit points (which disappear after 1 hour). After the panic ends,
the creature remains shaken for 10 minutes per caster level, and it automatically becomes panicked
again if it comes within sight of you during that time.

These temporary hit points stack if they are from different creatures.
