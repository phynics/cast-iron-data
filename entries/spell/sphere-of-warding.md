+++
id = "ref/spell/sphere-of-warding"
kind = "spell"
title = "Sphere of Warding"
aon = "SpellDisplay.aspx?ItemName=Sphere%20of%20Warding"
source_ids = ["undead-slayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sphere_of_warding", path = "json/spells9.json" },
]
[[sources]]
publication = "undead-slayers-handbook"
page = "19"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Effect", value = "10-ft.-radius sphere emanating from point touched" },
]
duration = "1 hour/level"
saving_throw = "Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Inquisitor\
5: Cleric, Oracle, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 hour/level
Saving throw: Will negates (see text)
Spell resistance: yes
Effect: 10-ft.-radius sphere emanating from point touched
:::

You create a luminescent sphere of orbiting energy that harms incorporeal creatures and dispossesses
them of any stolen bodies. An incorporeal creature must succeed at a Will save to enter a space
overlapping with the sphere; failure means the creature cannot pass through the sphere, as though it
were a wall of force. If the incorporeal creature succeeds, it may pass through the sphere at will,
though if it ends its turn within the sphere, it takes a number of points of force damage equal to
1d6 + 1 per caster level (maximum +10).

If a creature possessing another creature's body (via either magic jar or a similar effect) enters a
sphere of warding, that creature is immediately ejected from its host body, the host's spirit
returns to its body if it's able, and the possession effect immediately ends. When ejected, the body
enters the sphere, while the possessing creature takes the appropriate amount of force damage (no
save) and is shunted to the exterior of the sphere.
