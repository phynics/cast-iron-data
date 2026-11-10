+++
id = "ref/spell/freezing-sphere"
kind = "spell"
title = "Freezing Sphere"
aon = "SpellDisplay.aspx?ItemName=Freezing%20Sphere"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "freezing_sphere", path = "json/spells13.json" },
]
[[sources]]
publication = "core-rulebook"
page = "287"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, F (a small crystal sphere)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Effect", value = "see text" },
]
duration = "instantaneous or 1 round/level; see text"
saving_throw = "Reflex half; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Arcanist, Magus, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a small crystal sphere)
Range: long (400 ft. + 40 ft./level)
Duration: instantaneous or 1 round/level; see text
Saving throw: Reflex half; see text
Spell resistance: yes
Effect: see text
Descriptors: cold
:::

Freezing sphere creates a frigid globe of cold energy that streaks from your fingertips to the
location you select, where it explodes in a 40-foot-radius burst, dealing 1d6 points of cold damage
per caster level (maximum 15d6) to each creature in the area. A creature of the water subtype
instead takes 1d8 points of cold damage per caster level (maximum 15d8) and is staggered for 1d4
rounds.

If the freezing sphere strikes a body of water or a liquid that is principally water (not including
water-based creatures), it freezes the liquid to a depth of 6 inches in a 40-foot radius. This ice
lasts for 1 round per caster level. Creatures that were swimming on the surface of a targeted body
of water become trapped in the ice. Attempting to break free is a full-round action. A trapped
creature must make a DC 25 Strength check or a DC 25 Escape Artist check to do so.

You can refrain from firing the globe after completing the spell, if you wish. Treat this as a touch
spell for which you are holding the charge. You can hold the charge for as long as 1 round per
level, at the end of which time the freezing sphere bursts centered on you (and you receive no
saving throw to resist its effect). Firing the globe in a later round is a standard action.
