+++
id = "ref/spell/hydraulic-torrent"
kind = "spell"
title = "Hydraulic Torrent"
source_ids = ["advanced-players-guide", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hydraulic_torrent", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["water"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "60 ft."
effects = [
  { label = "Area", value = "60-ft. line" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Bloodrager, Druid, Hunter, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: 60 ft.
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Area: 60-ft. line
Descriptors: water
:::

**Sources:** Advanced Player's Guide pg 229

You call forth a powerful stream of water that batters all creatures and obstacles in its path until
it strikes something it cannot push past. Against creatures and moveable objects this stream acts as
a bull rush. You can bull rush creatures of any size, not just those one size larger than your own.
Make a combat maneuver check and apply its results to each creature within the area. Your CMB for
this bull rush is equal to your caster level plus your Intelligence, Wisdom, or Charisma modifier,
whichever is highest. This bull rush does not provoke an attack of opportunity.

Against immovable objects this stream instead allows you to make a Strength check to destroy the
target. When attempting to break an object, the stream has an effective Strength equal to your
caster level plus the ability score modifier as above. The Break DC depends on the object you're
trying to break-see Breaking Items.

Hydraulic torrent extinguishes any normal fires it encounters along its path. Magical fires are
unaffected.

### Mythic Hydraulic Torrent

**Sources:** Mythic Adventures pg 98\
The water is boiling hot or freezing cold, dealing 1d6 points of fire or cold damage per 2 caster
levels. Add your tier to your CMB for the spell and on the Strength check to destroy immovable
targets.

_Augmented (3rd):_ If you expend two uses of mythic power, the spell can extinguish magical fires as
if using a targeted [dispel magic](ref/spell/dispel-magic). Freezing cold water hardens into ice on
the ground, lasting as long as prevailing conditions allow. Boiling hot water turns into steam,
creating an area of concealing mist (equivalent to obscuring mist) that fills the affected squares
and all squares adjacent to the line of the spell.
