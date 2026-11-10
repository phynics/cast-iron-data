+++
id = "ref/spell/shocking-image"
kind = "spell"
title = "Shocking Image"
aon = "SpellDisplay.aspx?ItemName=Shocking%20Image"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shocking_image", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/mirror-image" },
]
[[sources]]
publication = "ultimate-combat"
page = "243"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
descriptors = ["electricity"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "see text"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Arcanist, Bloodrager, Bard, Mesmerist, Occultist, Red Mantis Assassin, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: see text
Target: you
Subschool: Figment
Descriptors: electricity
:::

This spell works like [mirror image](ref/spell/mirror-image), except the illusory doubles it creates
discharge an electric shock when destroyed. An opponent that uses a melee attack to destroy one of
your images takes 2d6 points of electricity damage. You must overcome a target's
[spell resistance](ref/rule/spell-resistance) the first time you deal this electricity damage to it.
Failure renders the target immune to damage from this spell.
