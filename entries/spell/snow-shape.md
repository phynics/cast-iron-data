+++
id = "ref/spell/snow-shape"
kind = "spell"
title = "Snow Shape"
source_ids = ["humans-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "snow_shape", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["water"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a miniature shovel)"
range = "touch"
effects = [
  { label = "Target", value = "snow or snow-sculpted object touched, up to 5 cubic ft. + 1 cubic ft./level" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Druid, Hunter\
2: Arcanist, Cleric, Oracle, Red Mantis Assassin, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a miniature shovel)
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: snow or snow-sculpted object touched, up to 5 cubic ft. + 1 cubic ft./level
Descriptors: water
:::

**Sources:** Humans of Golarion pg 29

In frozen northern lands, where the earth may be hidden beneath heavy drifts of snow, Ulfen druids
developed a variation of stone shape that other spellcasters have since learned.

You can form a mass of snow into any shape that suits your purpose, as per the spell stone shape.
While it's possible to make crude objects with snow shape, most fine details aren't possible.
However, a successful Craft (weapons) check allows you to create a bladed weapon from the snow. The
DC of this check is equal to the DC listed with the Craft (weapons) skill. You must be the one to
make the Craft check and must do so at the time of casting this spell. A failed check means that the
spell is cast normally but the weapon created is malformed and useless. This spell can only be used
to craft weapons and not more precise tools or elaborate armors.

Once you create the item with this spell, it solidifies into super-hard ice, gaining a
[hardness](ref/umr/hardness) of 5 and 10 hit points per inch of thickness. This weapon takes double
damage from fire. Anyone using an ice weapon takes a -2 penalty on attacks due to the slippery,
unwieldy nature of the weapon, but the weapon deals 1 point of cold damage in addition to its normal
damage. A weapon created by this spell lasts for 24 hours before melting into uselessness.
