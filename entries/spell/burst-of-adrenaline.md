+++
id = "ref/spell/burst-of-adrenaline"
kind = "spell"
title = "Burst of Adrenaline"
aon = "SpellDisplay.aspx?ItemName=Burst%20of%20Adrenaline"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burst_of_adrenaline", path = "json/spells2.json" },
]
[[sources]]
publication = "occult-adventures"
page = "160"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Spiritualist", level = 1 },
]
casting_time = "1 immediate action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Mesmerist, Psychic, Spiritualist
Casting time: 1 immediate action
Components: V, S
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
:::

You draw upon your body's inner reserves of strength, leaving you winded. When you are about to make
a d20 roll based on Strength, Dexterity, or Constitution, you can cast this spell to gain a +8
enhancement bonus to Strength, Dexterity, or Constitution for that roll, but you are fatigued for 1
round afterward.
