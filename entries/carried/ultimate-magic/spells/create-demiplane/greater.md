+++
id = "ref/carried/ultimate-magic/spells/create-demiplane/greater"
kind = "spell"
title = "Create Demiplane, Greater"
source_ids = ["ultimate-magic"]
section = ["Spells", "Create Demiplane"]
tags = ["conjuration", "creation"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Magic/Spells/Create Demiplane/Greater", path = "ultimate_magic/spell/create_demiplane_greater.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["creation"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Warpriest", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "6 hours"
components = "V, S, F (a forked metal rod worth at least 500 gp)"
range = "0 ft."
effects = [
  { label = "Effect", value = "extradimensional demiplane, up to 20 10-ft. cubes/level (S)" },
]
duration = "1 day/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
School: conjuration (creation)
Level: 9: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting Time: 6 hours
Components: V, S, F (a forked metal rod worth at least 500 gp)
Range: 0 ft.
Effect: extradimensional demiplane, up to 20 10-ft. cubes/level (S)
Duration: 1 day/level
Saving Throw: none
Spell Resistance: no
:::

_As create demiplane, but larger and with more planar traits._

This spell functions as _[create demiplane](ref/spell/create-demiplane)_, except the area is larger
and you can add more features to the plane. You can use this spell to expand a demiplane you created
with _[lesser create demiplane](ref/spell/create-demiplane-lesser)_ or
_[create demiplane](ref/spell/create-demiplane)_ (you do not need to create an entirely new plane
using this spell), in which case it has a duration of 1 day/level. Alternatively, when cast within
your demiplane, you may add to your demiplane (or remove from it) one of the following features (or
any of the features described in _[create demiplane](ref/spell/create-demiplane)_) with each casting
of the spell, in which case it has an instantaneous duration.

_Energy_: Your plane gains the (minor) negative- or positive-dominant energy trait (see Elemental
and Energy Traits). A plane cannot have both the negative-dominant and positive-dominant energy
traits.

_Magic_: Your plane gains the dead magic, enhanced magic, impeded magic, or wild magic planar trait
(see Magic Traits, _GameMastery Guide_ 187). If you selected dead magic, you are trapped within your
plane unless it has a permanent planar portal (such as the portal feature, below). If you selected
enhanced or impeded magic, choose one type of magic to be enhanced or impeded, such as “effects with
the fire descriptor or that manipulate fire” or “death spells and spells from the Death or Repose
domains.” A plane cannot be enhanced and impeded for the same kinds of spells.

_Morphic_: You may use _[move earth](ref/spell/move-earth)_ at will in your demiplane at one-tenth
of the spell's normal casting time, and can reshape normal plants in the same manner (such as by
twisting trees into a fence or humanlike shapes). You are even able to affect rock formations with
this ability, though the casting time for this is only half normal.

_Portal_: Your demiplane gains a permanent _[gate](ref/spell/gate)_ to one location on another
plane, which can only be used for planar travel. This location must be very familiar to you. This
_[gate](ref/spell/gate)_ is always open and usable from both sides, but you can secure it using
normal means (such as by building a door around it).

_Time_: By default, time passes at the normal rate in your demiplane. By selecting this feature, you
may make your plane have the erratic time, flowing time (half or double normal time), or timeless
trait (see Time).

You can make this spell permanent with the _[permanency](ref/spell/permanency)_ spell, at a cost of
22,500 gp. If you have cast _create greater demiplane_ multiple times to enlarge the demiplane, each
casting's area requires its own _[permanency](ref/spell/permanency)_ spell.
