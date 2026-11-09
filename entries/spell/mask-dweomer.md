+++
id = "ref/spell/mask-dweomer"
kind = "spell"
title = "Mask Dweomer"
aon = "SpellDisplay.aspx?ItemName=Mask%20Dweomer"
source_ids = ["advanced-players-guide", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mask_dweomer", path = "json/spells6.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "232"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of gauze)"
range = "touch"
effects = [
  { label = "Target", value = "creature or object touched" },
]
duration = "1 day/level (D)"
saving_throw = "none, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Occultist, Psychic, Witch
Casting time: 1 standard action
Components: V, S, M (a piece of gauze)
Range: touch
Duration: 1 day/level (D)
Saving throw: none, see text
Spell resistance: no
Target: creature or object touched
Subschool: Glamer
Descriptors: glamer
:::

You mask and manipulate a spell's magic aura to make it harder to detect. Select one spell effect on
the target creature or object. You must have either cast this spell yourself or have perceived it by
means such as detect magic or arcane sight. Both the desired spell effect and mask dweomer are
hidden from detect magic, although more powerful spells (such as arcane sight) pierce the deception
if the caster succeeds on a Will save. Analyze dweomer automatically detects both mask dweomer and
any masked spell effects.
