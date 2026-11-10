+++
id = "ref/spell/vacuous-vessel"
kind = "spell"
title = "Vacuous Vessel"
aon = "SpellDisplay.aspx?ItemName=Vacuous%20Vessel"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vacuous_vessel", path = "json/spells11.json" },
]
[[sources]]
publication = "black-markets"
page = "27"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 0 },
  { class = "Bard", level = 0 },
  { class = "Skald", level = 0 },
  { class = "Sorcerer", level = 0 },
  { class = "Wizard", level = 0 },
]
casting_time = "1 swift action"
components = "V"
range = "touch"
effects = [
  { label = "Target", value = "container touched" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates, see text"
spell_resistance = "yes, see text"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 0: Arcanist, Bard, Skald, Sorcerer, Wizard
Casting time: 1 swift action
Components: V
Range: touch
Duration: 1 round/level (D)
Saving throw: Will negates, see text
Spell resistance: yes, see text
Target: container touched
Subschool: Glamer
Descriptors: glamer
:::

This spell makes a single bag, chest, sack, or other container look and feel empty. The container
must be no larger than 1 cubic foot per caster level or the spell fails. Anyone peering into or
reaching into the container must succeed at a Will save or perceive the container as being
completely empty. All items within the container when the spell was cast are still present, but they
can't be noticed unless removed from the bag - such as by someone who can perceive them, or who
upends the container.

Casting vacuous vessel on another container or placing a new item in the existing container
immediately dismisses the currently active spell.
