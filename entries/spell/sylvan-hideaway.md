+++
id = "ref/spell/sylvan-hideaway"
kind = "spell"
title = "Sylvan Hideaway"
aon = "SpellDisplay.aspx?ItemName=Sylvan%20Hideaway"
source_ids = ["pathfinder-116-fangs-of-war"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sylvan_hideaway", path = "json/spells10.json" },
]
[[sources]]
publication = "pathfinder-116-fangs-of-war"
page = "67"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (one pound of unworked stone or wood)"
range = "touch"
effects = [
  { label = "Target", value = "one 5-foot square of touched earth" },
]
duration = "2 hours/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Druid, Hunter, Ranger, Shaman
Casting time: 1 standard action
Components: V, S, M (one pound of unworked stone or wood)
Range: touch
Duration: 2 hours/level (D)
Saving throw: none
Spell resistance: no
Target: one 5-foot square of touched earth
Subschool: Creation
:::

When this spell is cast on a natural, unworked surface, it creates an extradimensional underground
space large enough to comfortably hold two creatures of any size per caster level (maximum 12). The
room is sealed by a 5-foot-square camouflaged trap door that can be locked from within. (This trap
door has [hardness](ref/umr/hardness) 10 and 20 hit points per caster level; the Perception DC to
see the hidden trap door equals the spell's save DC.) The door and room are made of the same
material of the material component used to cast the spell. You can choose the shape and
configuration of the room when you create it; however, any furnishings (tables, beds, etc.) in the
room are made of the same material as the room and cannot be moved once created. When the spell
ends, anything inside the space is ejected to the surface in the nearest available square.
