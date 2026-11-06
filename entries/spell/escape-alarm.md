+++
id = "ref/spell/escape-alarm"
kind = "spell"
title = "Escape Alarm"
source_ids = ["core-rulebook", "villain-codex", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "escape_alarm", path = "json/spells.json" },
]

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

## Alarm

**Sources:** PRPG Core Rulebook pg 240

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

### Escape Alarm

**Sources:** Villain Codex pg 45

You place a ward on an area that notifies you when a creature exits it. This functions as alarm,
except as noted. It alerts you when a creature leaves, rather than enters, the area, and you can't
select a password to bypass its effects. Instead, when you place an escape alarm, you can attune up
to one additional creature per caster level to the spell. You are automatically attuned to your own
escape alarm and don't count against the limit. Attuned creatures can enter and exit the spell's
area without triggering the alarm. If you select a mental alarm rather than an audible one, all
attuned creatures receive the mental alert when someone exits the warded area.

### Selective Alarm

**Sources:** Ultimate Intrigue pg 224

This spell functions as alarm, except that you can tweak the spell to be more discerning in what
types of creatures or objects trigger the alarm. Instead of being triggered whenever a creature of
Tiny size or larger enters the warded area, you can set whatever triggering conditions you wish, as
long as they are based on observable phenomenon. For example, you could cause the selective alarm to
trigger when creatures of a certain race (such as orcs, bugbears, or kobolds) enter the area, or
whenever a group of four or more creatures enters the area together, or when a metal object is
brought into the area. You can't choose triggering conditions that rely on unobservable information,
such as having it triggered when creatures of a certain alignment enter the area, nor could you have
the alarm be triggered by "something worth more than 5,000 gp" entering the area, or even "a weapon"
entering the area, because an item's value and classification as a weapon is subjective, and might
vary from one person to the next.
