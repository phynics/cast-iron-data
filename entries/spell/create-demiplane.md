+++
id = "ref/spell/create-demiplane"
kind = "spell"
title = "Create Demiplane"
aon = "SpellDisplay.aspx?ItemName=Create%20Demiplane"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "create_demiplane", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/create-demiplane-lesser" },
]
[[sources]]
publication = "ultimate-magic"
page = "213"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Occultist", level = 5 },
  { class = "Oracle", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "2 hours"
components = "V, S, F (a forked metal rod worth at least 500 gp)"
range = "0 ft."
effects = [
  { label = "Effect", value = "extradimensional demiplane, up to three 10-ft. cubes/level (S)" },
]
duration = "1 day/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Occultist, Summoner\
6: Unchained Summoner\
7: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Witch, Wizard
Casting time: 2 hours
Components: V, S, F (a forked metal rod worth at least 500 gp)
Range: 0 ft.
Duration: 1 day/level
Saving throw: none
Spell resistance: no
Effect: extradimensional demiplane, up to three 10-ft. cubes/level (S)
Subschool: Creation
:::

### Create Demiplane

This spell functions as [create lesser demiplane](ref/spell/create-demiplane-lesser), except the
area is larger and you can add more features to the plane. You can use this spell to expand a
demiplane you created with create lesser demiplane (you do not need to create an entirely new plane
using this spell), in which case it has a duration of 1 day/level. Alternatively, when cast within
your demiplane, you may add (or remove) one of the following features to your demiplane with each
casting of the spell, in which case it has an instantaneous duration.

**Alignment:** Your plane gains the (mildly) chaos-, good-, evil-, law-, or neutral-aligned
alignment trait (see [Alignment Traits](ref/rule/alignment-traits)). You cannot give your demiplane
an alignment trait for an alignment you do not have.

**Bountiful:** Your demiplane gains a thriving natural ecology, with streams, ponds, waterfalls, and
plants. The demiplane provides enough plant-based food (nuts, grains, fruit, fungi, and so on) to
support one Medium creature for every 10-foot cube of the demiplane. The demiplane does not have any
animals unless you transport them there, but the ecology can sustain itself for as long as the
demiplane exists without requiring watering, gardening, pollination, and so on, and dead organic
material decays and returns to the soil in the normal manner. If your demiplane has ambient light,
these plants are normal, familiar surface plants; if it is a realm of twilight or darkness, these
plants are fungi and other plants adapted to near-darkness or underground locations.

**Elemental:** Your plane gains the air-, earth-, fire-, or water-elemental dominant trait (see
[Elemental and Energy Traits](ref/rule/elemental-and-energy-traits)).

**Gravity:** By default a demiplane's gravity is normal and oriented in one direction, like what
most creatures are used to on the Material Plane. By selecting this feature, the plane's gravity is
heavy, light, none, objectively directional, or subjectively directional (see
[Gravity](ref/rule/gravity-traits)).

**Seasonal:** The demiplane has a seasonal cycle and a light cycle, usually similar to those of a
land on the Material Plane, but customizable as you see fit (for example, your demiplane could
always be winter, day and night could alternate every 4 hours, and so on).

**Shape:** By default, the demiplane has a fixed shape and borders. By selecting this feature, you
may make your plane self-contained so it loops upon itself when a creature reaches one edge (see
[Shape and Size](ref/rule/shape-and-size-traits)). You may designate areas or locations on the edges
of your plane where this occurs (such as a pair of secret doors or a path in the woods) or apply it
to the entire plane.

**Structure:** Your demiplane has a specific, linked physical structure, such as a giant tree,
floating castle, labyrinth, mountain, and so on. (This option exists so you can pick a theme for
your plane without having to worry about the small details of determining what spells you need for
every hill, hole, wall, floor, and corner).

You can make this spell permanent with the [permanency](ref/spell/permanency) spell, at a cost of
20,000 gp. If you have cast create demiplane multiple times to enlarge the demiplane, each casting's
area requires its own permanency spell.
