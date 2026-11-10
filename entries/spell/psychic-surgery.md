+++
id = "ref/spell/psychic-surgery"
kind = "spell"
title = "Psychic Surgery"
aon = "SpellDisplay.aspx?ItemName=Psychic%20Surgery"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychic_surgery", path = "json/spells15.json" },
]
[[sources]]
publication = "occult-adventures"
page = "183"

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["mind-affecting"]
levels = [
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 6 },
]
casting_time = "10 minutes"
components = "V, M (diamond dust worth 250 gp)"
range = "touch"
effects = [
  { label = "Target", value = "one willing and living creature" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Mesmerist\
6: Psychic
Casting time: 10 minutes
Components: V, M (diamond dust worth 250 gp)
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: one willing and living creature
Descriptors: mind-affecting
:::

Psychic surgery cures the target of all Intelligence, Wisdom, and Charisma damage and restores all
points permanently drained from the target's Intelligence, Wisdom, and Charisma scores. It also
eliminates all ongoing insanity, confusion, and fear effects. Psychic surgery can also remove other
mental afflictions, including enchantment spells and abilities, and even instantaneous effects, but
in this case, if [dispel magic](ref/spell/dispel-magic) couldn't remove the effect, psychic surgery
works only if the spell level or equivalent spell level of the effect was 6th level or lower.
Psychic surgery removes all effects magically altering the target's memory, even instantaneous
effects, and it can restore a memory to perfect clarity like the second use of
[modify memory](ref/spell/modify-memory).
