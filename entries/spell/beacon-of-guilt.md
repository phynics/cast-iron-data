+++
id = "ref/spell/beacon-of-guilt"
kind = "spell"
title = "Beacon of Guilt"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "beacon_of_guilt", path = "json/spells12.json" },
]
[[sources]]
publication = "villain-codex"
page = "44"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["curse"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one object" },
]
duration = "24 hours or until discharged, then instantaneous"
saving_throw = "Will negates (object); see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Bard, Inquisitor, Occultist, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 24 hours or until discharged, then instantaneous
Saving throw: Will negates (object); see text
Spell resistance: yes
Target: one object
Descriptors: curse
:::

You place an invisible ward upon an object that is triggered the first time a creature tries to move
the object from its current location. The next creature to touch the object is cursed to become
obvious to everyone around it. The creature must succeed at a Will save or be surrounded in an aura
of twinkling red light that functions as [faerie fire](ref/spell/faerie-fire)
([spell resistance](ref/rule/spell-resistance) applies). The curse bestowed by this spell cannot be
dispelled, but a [break enchantment](ref/spell/break-enchantment),
[limited wish](ref/spell/limited-wish), [miracle](ref/spell/miracle),
[remove curse](ref/spell/remove-curse), or [wish](ref/spell/wish) spell can remove it.
