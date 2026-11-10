+++
id = "ref/spell/alarm"
kind = "spell"
title = "Alarm"
aon = "SpellDisplay.aspx?ItemName=Alarm"
source_ids = ["core-rulebook", "villain-codex", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "alarm", path = "json/spells.json" },
]
[[sources]]
publication = "core-rulebook"
page = "240"

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

Alarm creates a subtle ward on an area you select. Once the spell effect is in place, it thereafter
sounds a mental or audible alarm each time a creature of Tiny or larger size enters the warded area
or touches it. A creature that speaks the password (determined by you at the time of casting) does
not set off the alarm. You decide at the time of casting whether the alarm will be mental or audible
in nature.

_Mental Alarm:_ A mental alarm alerts you (and only you) so long as you remain within 1 mile of the
warded area. You note a single mental "ping" that awakens you from normal sleep but does not
otherwise disturb concentration. A silence spell has no effect on a mental alarm.

_Audible Alarm:_ An audible alarm produces the sound of a hand bell, and anyone within 60 feet of
the warded area can hear it clearly. Reduce the distance by 10 feet for each interposing closed door
and by 20 feet for each substantial interposing wall.

In quiet conditions, the ringing can be heard faintly as far as 180 feet away. The sound lasts for 1
round. Creatures within a silence spell cannot hear the ringing.

Ethereal or astral creatures do not trigger the alarm.

Alarm can be made permanent with a [permanency](ref/spell/permanency) spell.
