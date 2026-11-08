+++
id = "ref/spell/selective-alarm"
kind = "spell"
title = "Selective Alarm"
source_ids = ["core-rulebook", "villain-codex", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "selective_alarm", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/alarm" },
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

### Selective Alarm

**Sources:** Ultimate Intrigue pg 224

This spell functions as [alarm](ref/spell/alarm), except that you can tweak the spell to be more
discerning in what types of creatures or objects trigger the alarm. Instead of being triggered
whenever a creature of Tiny size or larger enters the warded area, you can set whatever triggering
conditions you wish, as long as they are based on observable phenomenon. For example, you could
cause the selective alarm to trigger when creatures of a certain race (such as orcs, bugbears, or
kobolds) enter the area, or whenever a group of four or more creatures enters the area together, or
when a metal object is brought into the area. You can't choose triggering conditions that rely on
unobservable information, such as having it triggered when creatures of a certain alignment enter
the area, nor could you have the alarm be triggered by "something worth more than 5,000 gp" entering
the area, or even "a weapon" entering the area, because an item's value and classification as a
weapon is subjective, and might vary from one person to the next.
