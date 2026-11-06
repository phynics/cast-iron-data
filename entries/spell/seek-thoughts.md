+++
id = "ref/spell/seek-thoughts"
kind = "spell"
title = "Seek Thoughts"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "seek_thoughts", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a handful of copper coins)"
range = "40 ft."
effects = [
  { label = "Area", value = "40-ft.-radius emanation centered on you" },
]
duration = "concentration, up to 1 minute/level"
saving_throw = "Will negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Medium, Psychic\
3: Alchemist, Arcanist, Bard, Inquisitor, Investigator, Mesmerist, Occultist, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a handful of copper coins)
Range: 40 ft.
Duration: concentration, up to 1 minute/level
Saving throw: Will negates
Spell resistance: no
Area: 40-ft.-radius emanation centered on you
Descriptors: mind-affecting
:::

**Sources:** Advanced Player's Guide pg 242

Similar to detect thoughts, seek thoughts allows you to sift through the surface thoughts of those
around you. You may scan for either the answer to a simple question (such as "Where is the hidden
lair of the wererats"?) or for information on a general topic (such as the beliefs of an evil cult).
You detect the number of creatures who are thinking about this question or topic within range, as
well as their location if they are visible to you. Seek thoughts does not let you read actual
surface thoughts, only if a given creature is thinking about the topic you are concentrating on. A
successful Will save prevents you from sensing a creature's thoughts for the duration of the spell.

You can maintain concentration on seek thoughts while you engage in normal conversation, allowing
you to ask leading questions about topics of interest. A creature conversing with you while you
concentrate can notice that you are distracted with a successful DC 25 Sense Motive check.
