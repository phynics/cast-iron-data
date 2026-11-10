+++
id = "ref/spell/magic-circle-against-law"
kind = "spell"
title = "Magic Circle Against Law"
aon = "SpellDisplay.aspx?ItemName=Magic%20Circle%20against%20Law"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_circle_against_law", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/magic-circle-against-evil" },
]
[[sources]]
publication = "core-rulebook"
page = "308"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["good"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a 3-ft.-diameter circle of powdered silver)"
range = "touch"
effects = [
  { label = "Area", value = "10-ft.-radius emanation from touched creature" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no; see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Arcanist, Cleric, Inquisitor, Medium, Occultist, Oracle, Paladin, Shaman, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a 3-ft.-diameter circle of powdered silver)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: no; see text
Area: 10-ft.-radius emanation from touched creature
Descriptors: good
:::

### Magic Circle Against Law

This spell functions like _[magic circle against evil](ref/spell/magic-circle-against-evil),_ except
that it is similar to [protection from law](ref/spell/protection-from-law) instead of
_[protection from evil](ref/spell/protection-from-evil),_ and it can imprison a nonchaotic called
creature.
