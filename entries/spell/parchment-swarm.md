+++
id = "ref/spell/parchment-swarm"
kind = "spell"
title = "Parchment Swarm"
aon = "SpellDisplay.aspx?ItemName=Parchment%20Swarm"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "parchment_swarm", path = "json/spells7.json" },
]
[[sources]]
publication = "occult-adventures"
page = "180"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Occultist", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "S, M (blank parchment or magic scroll; see text)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Reflex half, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Occultist\
5: Arcanist, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: S, M (blank parchment or magic scroll; see text)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Reflex half, see text
Spell resistance: yes
Target: one creature
:::

When you cast this spell, you quickly tear a parchment into shreds, releasing the flying fragments
to swarm around a target creature and deliver thousands of tiny paper cuts. Using normal parchment,
the spell deals 1d6 points of magical slashing damage per caster level (maximum 15d6).

If you use a magic scroll as the material component, choose one of the spells stored in the scroll.
If the spell is 1st level, you can choose to apply the effect of that spell to the parchment swarm's
target on a failed Reflex save (if the spell on the scroll has its own saving throw, the target then
attempts that save as normal). If the spell on the scroll is at least 2nd level, you can choose to
instead change parchment swarm to affect a 20-foot-radius spread instead of a single target.
