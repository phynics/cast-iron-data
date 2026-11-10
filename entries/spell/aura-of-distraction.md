+++
id = "ref/spell/aura-of-distraction"
kind = "spell"
title = "Aura of Distraction"
aon = "SpellDisplay.aspx?ItemName=Aura%20of%20Distraction"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aura_of_distraction", path = "json/spells.json" },
]
[[sources]]
publication = "psychic-anthology"
page = "10"

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Area", value = "20-ft.-radius emanation centered on you" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level (D)
Saving throw: Will negates
Spell resistance: yes
Area: 20-ft.-radius emanation centered on you
Descriptors: mind-affecting
:::

You emit an aura of subsonic noise and mental imagery that makes concentrating difficult. Any
creature within the aura that fails its save takes a -5 penalty on
[concentration](ref/rule/concentration) checks. A creature must attempt the Will save upon entering
the area of the aura, and the penalty ends as soon as the creature leaves the aura. A creature that
succeeds at its save is immune to the effects of the aura for this casting of the spell, even if it
leaves and reenters the aura, but must attempt another Will save each additional time this spell is
cast. You are immune to your own aura of distraction.
