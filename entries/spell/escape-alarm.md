+++
id = "ref/spell/escape-alarm"
kind = "spell"
title = "Escape Alarm"
source_ids = ["core-rulebook", "villain-codex", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "escape_alarm", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/alarm" },
]
[[sources]]
publication = "villain-codex"
page = "45"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (a tiny bell and a piece of very fine silver wire)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "20-ft.-radius emanation centered on a point in space" },
]
duration = "2 hours/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Arcanist, Bard, Hunter, Inquisitor, Occultist, Psychic, Ranger, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, F/DF (a tiny bell and a piece of very fine silver wire)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 2 hours/level
Saving throw: none
Spell resistance: no
Area: 20-ft.-radius emanation centered on a point in space
:::

### Escape Alarm

You place a ward on an area that notifies you when a creature exits it. This functions as
[alarm](ref/spell/alarm), except as noted. It alerts you when a creature leaves, rather than enters,
the area, and you can't select a password to bypass its effects. Instead, when you place an escape
alarm, you can attune up to one additional creature per caster level to the spell. You are
automatically attuned to your own escape alarm and don't count against the limit. Attuned creatures
can enter and exit the spell's area without triggering the alarm. If you select a mental alarm
rather than an audible one, all attuned creatures receive the mental alert when someone exits the
warded area.
