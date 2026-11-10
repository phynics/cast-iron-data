+++
id = "ref/spell/nondetection-lesser"
kind = "spell"
title = "Lesser Nondetection"
aon = "SpellDisplay.aspx?ItemName=Nondetection%2C%20Lesser"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nondetection_lesser", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/nondetection" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "25"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Ranger", level = 3 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of mercury)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Alchemist, Antipaladin, Arcanist, Inquisitor, Investigator, Sorcerer, Summoner, Unchained Summoner, Wizard\
3: Ranger
Casting time: 1 standard action
Components: V, S, M (a drop of mercury)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: creature touched
:::

This spell functions like [nondetection](ref/spell/nondetection), except it blocks the effects of
only divination spells and effects that target an area, rather than you or an object in your
possession specifically. For example, lesser nondetection doesn't ward you against a spellcaster who
is attempting to scry on you with the scrying spell or find an object in your possession with locate
object, but it does protect you against effects that target an area you happen to be in, such as
detect spells or clairaudience/clairvoyance.
