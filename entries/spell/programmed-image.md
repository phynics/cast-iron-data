+++
id = "ref/spell/programmed-image"
kind = "spell"
title = "Programmed Image"
aon = "SpellDisplay.aspx?ItemName=Programmed%20Image"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "programmed_image", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/silent-image" },
]
[[sources]]
publication = "core-rulebook"
page = "327"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (fleece and jade dust worth 25 gp)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Effect", value = "visual figment that cannot extend beyond a 20-ft. cube + one 10-ft. cube/level (S)" },
]
duration = "permanent until triggered, then 1 round/level"
saving_throw = "Will disbelief (if interacted with)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 6: Arcanist, Bard, Mesmerist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (fleece and jade dust worth 25 gp)
Range: long (400 ft. + 40 ft./level)
Duration: permanent until triggered, then 1 round/level
Saving throw: Will disbelief (if interacted with)
Spell resistance: no
Effect: visual figment that cannot extend beyond a 20-ft. cube + one 10-ft. cube/level (S)
Subschool: Figment
:::

This spell functions like [silent image](ref/spell/silent-image), except that this spell's figment
activates when a specific condition occurs. The figment includes visual, auditory, olfactory, and
thermal elements, including intelligible speech.

You set the triggering condition (which may be a special word) when casting the spell. The event
that triggers the illusion can be as general or as specific and detailed as desired but must be
based on an audible, tactile, olfactory, or visual trigger. The trigger cannot be based on some
quality not normally obvious to the senses, such as alignment. See magic mouth for more details
about such triggers.
