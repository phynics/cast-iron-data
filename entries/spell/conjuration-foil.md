+++
id = "ref/spell/conjuration-foil"
kind = "spell"
title = "Conjuration Foil"
aon = "SpellDisplay.aspx?ItemName=Conjuration%20Foil"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "conjuration_foil", path = "json/spells12.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "207"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Magus", level = 3 },
  { class = "Medium", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 immediate action"
components = "S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "20-foot radius spread" },
]
duration = "1 round"
saving_throw = "Will partial (see text)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Magus, Summoner, Unchained Summoner\
4: Arcanist, Bard, Medium, Occultist, Psychic, Skald, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 immediate action
Components: S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round
Saving throw: Will partial (see text)
Spell resistance: yes (object)
Area: 20-foot radius spread
:::

All creatures in the area gain a +4 bonus on saving throws against teleportation effects. If any
creature would enter or depart the area via a summoning or teleportation effect, that creature takes
1d6 points of damage per spell level of the triggering effect (or half the HD of the originating
creature if the effect has no spell level) and arrives in a random similar location within the
triggering effect's range, rather than the intended destination.

A successful Will save halves the damage and negates the altered destination.
