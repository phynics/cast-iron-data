+++
id = "ref/spell/divination"
kind = "spell"
title = "Divination"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "divination", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "10 minutes"
components = "V, S, M (incense and an appropriate offering worth 25 gp)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Medium\
4: Cleric, Inquisitor, Oracle, Psychic, Shaman, Spiritualist, Warpriest, Witch
Casting time: 10 minutes
Components: V, S, M (incense and an appropriate offering worth 25 gp)
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** PRPG Core Rulebook pg 273

Similar to augury but more powerful, a divination spell can provide you with a useful piece of
advice in reply to a question concerning a specific goal, event, or activity that is to occur within
1 week. The advice granted by the spell can be as simple as a short phrase, or it might take the
form of a cryptic rhyme or omen. If your party doesn't act on the information, the conditions may
change so that the information is no longer useful. The base chance for a correct divination is
70% + 1% per caster level, to a maximum of 90%. If the die roll fails, you know the spell failed,
unless specific magic yielding false information is at work.

As with augury, multiple divinations about the same topic by the same caster use the same dice
result as the first divination spell and yield the same answer each time.

### Prognostication

**Sources:** Ultimate Intrigue pg 223

You glimpse the future. Prognostication functions as divination except that the spell can see up to
a year and a day into the future. Because of the increased unpredictability of the distant future,
prognostication is significantly more cryptic than the already-cryptic divination spell.

### True Prognostication

**Sources:** Ultimate Intrigue pg 228

True prognostication functions as divination except that the spell can see up to 100 years into the
future. Because of the extreme unpredictability of the far-distant future, true prognostication is
incredibly cryptic when used to learn about events on such large a scale.
