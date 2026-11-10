+++
id = "ref/spell/call-construct"
kind = "spell"
title = "Call Construct"
aon = "SpellDisplay.aspx?ItemName=Call%20Construct"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "call_construct", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/instant-summons" },
]
[[sources]]
publication = "ultimate-magic"
page = "210"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "10 minutes"
components = "V, S, M (a sapphire worth 1,000 or 5,000 gp; see text)"
range = "touch"
effects = [
  { label = "Target", value = "construct touched" },
]
duration = "permanent until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Occultist\
8: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Wizard
Casting time: 10 minutes
Components: V, S, M (a sapphire worth 1,000 or 5,000 gp; see text)
Range: touch
Duration: permanent until discharged
Saving throw: none
Spell resistance: no
Target: construct touched
Subschool: Teleportation
:::

This spell functions as [instant summons](ref/spell/instant-summons), except it can only summon a
construct you control. For constructs such as golems that are immune to magic, the value of the
specially inscribed sapphire must be at least 5,000 gp. For other constructs, a 1,000 gp sapphire
suffices.

If the construct is no longer under your control or destroyed, the spell fails, but you know roughly
where the construct or its remains are located.
