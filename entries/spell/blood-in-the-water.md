+++
id = "ref/spell/blood-in-the-water"
kind = "spell"
title = "Blood in the Water"
aon = "SpellDisplay.aspx?ItemName=Blood%20in%20the%20Water"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blood_in_the_water", path = "json/spells2.json" },
]
[[sources]]
publication = "monster-codex"
page = "189"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["emotion"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "20 ft."
effects = [
  { label = "Area", value = "20-ft.-radius emanation centered on you" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Arcanist, Cleric, Mesmerist, Oracle, Psychic, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, DF
Range: 20 ft.
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Area: 20-ft.-radius emanation centered on you
Descriptors: emotion
:::

As part of the casting of this spell, you must deal 1 point of piercing or slashing damage to
yourself to release your blood. This causes you to take 1 point of bleed damage. While the spell is
in effect, all sharks, feeders in the depths, and creatures with the blood frenzy ability in the
area gain a +2 bonus to Strength and Constitution and take a -2 penalty to AC. This is treated as
blood frenzy for the purposes of other feats and effects, and doesn't stack with the effects of
actual blood frenzy. If you cease bleeding, the spell immediately ends.
