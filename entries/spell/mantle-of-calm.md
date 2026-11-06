+++
id = "ref/spell/mantle-of-calm"
kind = "spell"
title = "Mantle of Calm"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mantle_of_calm", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Mesmerist", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "none and Will negates (see text)"
spell_resistance = "no and yes (see text)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Mesmerist\
3: Cleric, Inquisitor, Oracle, Paladin, Psychic, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 1 round/level (D)
Saving throw: none and Will negates (see text)
Spell resistance: no and yes (see text)
Target: you
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

**Sources:** Advanced Class Guide pg 186

You surround yourself with a mantle of calm serenity. You take a -2 penalty on attack rolls, and
opponents gain a +2 bonus on saving throws against spells you cast. Any creature affected by a rage
effect (barbarian's rage, bloodrager's bloodrage, blood rage monster ability, rage spell, skald's
inspired rage raging song, and so on) that strikes you with a melee attack must attempt at a Will
saving throw, without the rage effect's bonus to Will; failure means the rage effect ends (as if it
were dispelled or the creature voluntarily ended it, as appropriate).

If you become affected by a rage effect while this spell is active, this spell immediately ends. If
your rage effect comes from a skald's raging song, then it ends only for you, and you cannot
re-accept the effects of the song.
