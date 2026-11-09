+++
id = "ref/spell/detect-thoughts"
kind = "spell"
title = "Detect Thoughts"
aon = "SpellDisplay.aspx?ItemName=Detect%20Thoughts"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_thoughts", path = "json/spells3.json" },
]
[[sources]]
publication = "core-rulebook"
page = "268"

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (a copper piece)"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped emanation" },
]
duration = "concentration, up to 1 min./level (D)"
saving_throw = "Will negates; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Psychic\
2: Alchemist, Arcanist, Bard, Inquisitor, Investigator, Medium, Mesmerist, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F/DF (a copper piece)
Range: 60 ft.
Duration: concentration, up to 1 min./level (D)
Saving throw: Will negates; see text
Spell resistance: no
Area: cone-shaped emanation
Descriptors: mind-affecting
:::

You detect surface thoughts. The amount of information revealed depends on how long you study a
particular area or subject.

_1st Round:_ Presence or absence of thoughts (from conscious creatures with Intelligence scores of 1
or higher).

_2nd Round:_ Number of thinking minds and the Intelligence score of each. If the highest
Intelligence is 26 or higher (and at least 10 points higher than your own Intelligence score), you
are stunned for 1 round and the spell ends. This spell does not let you determine the location of
the thinking minds if you can't see the creatures whose thoughts you are detecting.

_3rd Round:_ Surface thoughts of any mind in the area. A target's Will save prevents you from
reading its thoughts, and you must cast detect thoughts again to have another chance. Creatures of
animal intelligence (Intelligence 1 or 2) have simple, instinctual thoughts.

Each round, you can turn to detect thoughts in a new area. The spell can penetrate barriers, but 1
foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt blocks it.
