+++
id = "ref/spell/detect-anxieties"
kind = "spell"
title = "Detect Anxieties"
aon = "SpellDisplay.aspx?ItemName=Detect%20Anxieties"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_anxieties", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/detect-thoughts" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "211"

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

### Detect Anxieties

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
