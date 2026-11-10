+++
id = "ref/spell/transfer-tattoo"
kind = "spell"
title = "Transfer Tattoo"
aon = "SpellDisplay.aspx?ItemName=Transfer%20Tattoo"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "transfer_tattoo", path = "json/spells10.json" },
]
[[sources]]
publication = "inner-sea-magic"
page = "62"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (tattooing needle)"
range = "touch"
effects = [
  { label = "Target", value = "one magic tattoo" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Bard, Red Mantis Assassin, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (tattooing needle)
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Target: one magic tattoo
:::

With this spell, you can transfer one magic tattoo from one creature to another. A target that isn't
willing to have his tattoo removed or to receive the transferred tattoo can resist this spell with a
Fortitude save - if successful, the transfer fails and the caster of this spell is staggered for 1
round by the backlash of magical energy. A tattoo can be transferred from a dead creature in this
manner to a living host, provided the body has been dead no longer than one hour per caster level.
