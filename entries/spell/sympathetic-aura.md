+++
id = "ref/spell/sympathetic-aura"
kind = "spell"
title = "Sympathetic Aura"
aon = "SpellDisplay.aspx?ItemName=Sympathetic%20Aura"
source_ids = ["core-rulebook", "ultimate-intrigue", "adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sympathetic_aura", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/magic-aura" },
]
[[sources]]
publication = "adventurers-guide"
page = "37"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, F (a small square of silk that must be passed over the object that receives the aura)"
range = "touch"
effects = [
  { label = "Target", value = "one touched object weighing up to 5 lbs./level" },
]
duration = "1 day/level (D)"
saving_throw = "none; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Arcanist, Bard, Mesmerist, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a small square of silk that must be passed over the object that receives the aura)
Range: touch
Duration: 1 day/level (D)
Saving throw: none; see text
Spell resistance: no
Target: one touched object weighing up to 5 lbs./level
Subschool: Glamer
Descriptors: glamer
:::

### Sympathetic Aura

This spell functions like [magic aura](ref/spell/magic-aura), except it extends its altered aura to
similar items in a 5-foot radius. For this purpose, similar items must be alike in approximate
shape, composition, and function, so a potion of cure light wounds targeted by this spell to appear
nonmagical would also obscure the auras of nearby potions, elixirs, and oils, as well as flasks.
Items other than the targeted item retain their altered aura for 1 round per caster level after
being removed from the spell's area.
