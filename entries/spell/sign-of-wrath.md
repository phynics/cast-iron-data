+++
id = "ref/spell/sign-of-wrath"
kind = "spell"
title = "Sign of Wrath"
source_ids = ["rise-of-the-runelords-anniversary-edition", "pathfinder-5-sins-of-the-saviors"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sign_of_wrath", path = "json/spells9.json" },
]
[[sources]]
publication = "rise-of-the-runelords-anniversary-edition"
page = "419"
[[sources]]
publication = "pathfinder-5-sins-of-the-saviors"
page = "63"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, F (a gem worth 1,000 gp inscribed with the Thassilonian symbol of wrath)"
range = "personal"
effects = [
  { label = "Area", value = "25-ft.-radius burst centered on you" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, F (a gem worth 1,000 gp inscribed with the Thassilonian symbol of wrath)
Range: personal
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: 25-ft.-radius burst centered on you
Descriptors: force
:::

A giant, glowing symbol of wrath appears below you, forcibly repulsing all nearby creatures. All
creatures within the area of effect take 1d6 points of force damage per caster level (maximum 15d6)
and are subjected to a bull rush that attempts to push them directly away from you. The blast's bull
rush effect has a CMB bonus equal to your caster level + your Intelligence, Wisdom, or Charisma
modifier (whichever is highest). You are unaffected by both the spell's damage and its bull rush
effect, and may select up to one creature per 4 caster levels to also be ignored by the spells
effects.
