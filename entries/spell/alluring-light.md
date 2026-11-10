+++
id = "ref/spell/alluring-light"
kind = "spell"
title = "Alluring Light"
aon = "SpellDisplay.aspx?ItemName=Alluring%20Light"
source_ids = ["pathfinder-134-it-came-from-hollow-mountain"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "alluring_light", path = "json/spells.json" },
]
[[sources]]
publication = "pathfinder-134-it-came-from-hollow-mountain"
page = "72"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
levels = [
  { class = "Bard", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "30 ft."
effects = [
  { label = "Area", value = "30-ft.-radius emanation centered on you" },
]
duration = "instantaneous"
saving_throw = "Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Bard, Skald, Witch
Casting time: 1 standard action
Components: V, S
Range: 30 ft.
Duration: instantaneous
Saving throw: Will negates (see text)
Spell resistance: yes
Area: 30-ft.-radius emanation centered on you
Subschool: Compulsion
:::

You glow with a soft radiance that calls out to all who see it. Each enemy that fails its save is
drawn to you and must use its move action to approach you at the beginning of each of its turns for
1 round per caster level. An affected target must move toward you in the most direct path it can,
though it can step around obstacles or other creatures. This spell can't force a creature to walk
into an area that might obviously harm or kill it (such as into a pit, over a patch of floor studded
with [caltrops](ref/eq-misc/caltrops), or through a [wall of fire](ref/spell/wall-of-fire)). An
affected creature that loses sight of you is not compelled to move toward you, although if it later
regains vision of you while still affected by this spell, it must again move toward you. Any hostile
action against an affected creature (such an attack of opportunity due to its movement) cancels the
spell's effect against that creature. Your initial flash of light also increases the light level
within the spell's area by one step, up to normal light (darkness becomes dim light, and dim light
becomes normal light) for 1 round per caster level.
