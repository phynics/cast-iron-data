+++
id = "ref/spell/withdraw-affliction"
kind = "spell"
title = "Withdraw Affliction"
aon = "SpellDisplay.aspx?ItemName=Withdraw%20Affliction"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "withdraw_affliction", path = "json/spells16.json" },
]
[[sources]]
publication = "occult-adventures"
page = "191"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Psychic", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Spiritualist", level = 5 },
  { class = "Witch", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one afflicted creature" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Spiritualist\
6: Psychic, Shaman\
7: Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Target: one afflicted creature
:::

You push your hand into the subject, then withdraw an affliction from the body of the sufferer as a
tangible object. This extraction appears as a slimy mass of flesh. The target creature is cured as
if affected by [remove disease](ref/spell/remove-disease), [remove curse](ref/spell/remove-curse),
or [neutralize poison](ref/spell/neutralize-poison).

In addition, this slimy mass allows you to deliver the affliction to another as a touch attack, as
if holding the charge for a touch spell. It has the same effect as the original affliction, with the
same saving throw and DC.
