+++
id = "ref/spell/invisibility-bubble-giant"
kind = "spell"
title = "Giant Invisibility Bubble"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invisibility_bubble_giant", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/invisibility-bubble" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (needle from a sea urchin)"
range = "touch"
effects = [
  { label = "Area", value = "touched creature's space, up to one 5-foot-cube" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Alchemist, Antipaladin, Arcanist, Bard, Inquisitor, Investigator, Magus, Medium, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (needle from a sea urchin)
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Area: touched creature's space, up to one 5-foot-cube
Subschool: Glamer
Descriptors: glamer
:::

## Invisibility Bubble

**Sources:** Aquatic Adventures pg 60

A glamered bubble surrounds the target's space, rendering her completely invisible underwater by
hiding both the target and any water she displaces. Because of the bubble's size limit, this spell
works only on Medium or smaller targets. Other objects and creatures within the bubble's space are
also invisible while they stay in the space, which could reveal the spell's existence to a canny
observer who notices fish disappearing into the bubble and reappearing on the other side. Creatures
inside the bubble can see each other, which allows foes who can pinpoint the bubble's location (such
as dragons) to stick their heads into the bubble in order to see the target. Any creature on the
inside of the bubble that takes any action that would break invisibility pops the bubble and ends
the spell early. On land, the bubble is clearly visible, acting much as invisibility does in the
water. Unlike with invisibility, the inside of the bubble blocks light from escaping the bubble,
meaning that light sources inside the bubble don't illuminate past its edges, but also don't reveal
a telltale glow.

### Giant Invisibility Bubble

**Sources:** Aquatic Adventures pg 60

This functions as per [invisibility bubble](ref/spell/invisibility-bubble), but the bubble is
larger, which allows you to target a creature of up to size Gargantuan, or allows more creatures
into the bubble.

### Mass Invisibility Bubble

**Sources:** Aquatic Adventures pg 60

This functions as per invisibility bubble, but the spell affects the areas of each target creature,
regardless of the creature's size. The effect moves with the group and is broken when anyone in the
group attacks. Individuals in separate bubbles can't see each other. The spell is broken for any
individual who moves more than 180 feet from the nearest member of the group. If only two
individuals are affected, the one moving away from the other one loses its invisibility. If both are
moving away from each other simultaneously, they both become visible when the distance between them
exceeds 180 feet.
