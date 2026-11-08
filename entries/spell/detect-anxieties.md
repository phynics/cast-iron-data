+++
id = "ref/spell/detect-anxieties"
kind = "spell"
title = "Detect Anxieties"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_anxieties", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/detect-thoughts" },
]

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

## Detect Thoughts

**Sources:** PRPG Core Rulebook pg 268

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

### Detect Anxieties

**Sources:** Ultimate Intrigue pg 211

This spell functions as [detect thoughts](ref/spell/detect-thoughts) except that you sense
significant anxieties of creatures with an Intelligence score of 1 or higher, regardless of whether
they are conscious or not.

Instead of Intelligence, the second round of concentration reveals each mind's Wisdom score and
current degree of fear (shaken, frightened, panicked, cowering, or paralyzed with fear). If the
highest Wisdom score is 26 or higher (and at least 10 points higher than your own Wisdom score), you
are stunned for 1 round and the spell ends.

Instead of surface thoughts, the third round of concentration reveals the most pressing current
anxiety of any mind in the area (Will negates).

Presenting a creature with the threat of its anxiety grants you a +2 bonus (or higher, at the GM's
discretion) on checks to Intimidate that creature.

### Detect Desires

**Sources:** Ultimate Intrigue pg 211

This spell functions as per detect thoughts, except you sense significant desires of creatures with
an Intelligence score of 1 or higher, regardless of whether they are conscious or not.

Instead of Intelligence, the second round of concentration reveals each mind's Charisma score. If
the highest Charisma score is 26 or higher (and at least 10 points higher than your own Charisma
score), you are stunned for 1 round and the spell ends. Instead of surface thoughts, the third round
of concentration reveals the most pressing current desire of any mind in the area (Will negates).

Presenting a creature with an opportunity to fulfill a significant desire grants you a +2
circumstance bonus (or higher, at the GM's discretion) on Diplomacy checks to influence it.
