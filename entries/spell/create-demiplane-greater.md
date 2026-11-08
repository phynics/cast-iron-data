+++
id = "ref/spell/create-demiplane-greater"
kind = "spell"
title = "Greater Create Demiplane"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "create_demiplane_greater", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/create-demiplane" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "6 hours"
components = "V, S, F (a forked metal rod worth at least 500 gp)"
range = "0 ft."
effects = [
  { label = "Effect", value = "extradimensional demiplane, up to 20 10-ft. cubes/level (S)" },
]
duration = "1 day/level or instantaneous (see text)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 9: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Witch, Wizard
Casting time: 6 hours
Components: V, S, F (a forked metal rod worth at least 500 gp)
Range: 0 ft.
Effect: extradimensional demiplane, up to 20 10-ft. cubes/level (S)
Duration: 1 day/level or instantaneous (see text)
Saving throw: none
Spell resistance: no
Subschool: Creation
:::

### Greater Create Demiplane

**Sources:** Ultimate Magic pg 213

This spell functions as [create demiplane](ref/spell/create-demiplane), except the area is larger
and you can add more features to the plane. You can use this spell to expand a demiplane you created
with lesser create demiplane or create demiplane (you do not need to create an entirely new plane
using this spell), in which case it has a duration of 1 day/level. Alternatively, when cast within
your demiplane, you may add to your demiplane (or remove from it) one of the following features (or
any of the features described in create demiplane) with each casting of the spell, in which case it
has an instantaneous duration.

**Energy:** Your plane gains the (minor) negative- or positive-dominant energy trait (see Elemental
and Energy Traits). A plane cannot have both the negative-dominant and positive-dominant energy
traits.

**Magic:** Your plane gains the dead magic, enhanced magic, impeded magic, or wild magic planar
trait (see [Magic Traits](ref/rule/magic-traits)). If you selected dead magic, you are trapped
within your plane unless it has a permanent planar portal (such as the portal feature, below). If
you selected enhanced or impeded magic, choose one type of magic to be enhanced or impeded, such as
"effects with the fire descriptor or that manipulate fire" or "death spells and spells from the
Death or Repose domains." A plane cannot be enhanced and impeded for the same kinds of spells.

**Morphic:** You may use move earth at will in your demiplane at one-tenth of the spell's normal
casting time, and can reshape normal plants in the same manner (such as by twisting trees into a
fence or human-like shapes). You are even able to affect rock formations with this ability, though
the casting time for this is only half normal.

**Portal:** Your demiplane gains a permanent gate to one location on another plane, which can only
be used for planar travel. This location must be very familiar to you. This gate is always open and
usable from both sides, but you can secure it using normal means (such as by building a door around
it).

**Time:** By default, time passes at the normal rate in your demiplane. By selecting this feature,
you may make your plane have the erratic time, flowing time (half or double normal time), or
timeless trait (see [Time Traits](ref/rule/time-traits)).

You can make this spell permanent with the [permanency](ref/spell/permanency) spell, at a cost of
22,500 gp. If you have cast create greater demiplane multiple times to enlarge the demiplane, each
casting's area requires its own permanency spell.
