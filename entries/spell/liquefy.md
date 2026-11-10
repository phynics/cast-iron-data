+++
id = "ref/spell/liquefy"
kind = "spell"
title = "Liquefy"
aon = "SpellDisplay.aspx?ItemName=Liquefy"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "liquefy", path = "json/spells6.json" },
]
[[sources]]
publication = "arcane-anthology"
page = "21"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Investigator", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a specially prepared glass bottle)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "1 object weighing up to 1 pound/level" },
]
duration = "1 round/level (D)"
saving_throw = "Fortitude negates (object)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Bard, Investigator, Skald\
4: Arcanist, Druid, Hunter, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a specially prepared glass bottle)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Fortitude negates (object)
Spell resistance: no
Target: 1 object weighing up to 1 pound/level
:::

The object you target becomes a liquid version of itself and drips or runs like a thin oil until it
pools on any flat surface. If the item has magical or alchemical properties, they become inert for
the duration of the spell. If you are holding the item when you cast this spell, you can drain it
into the bottle used as focus for the spell. Items with hit point damage or the broken condition
regain 5 hit points/caster level if drained into a bottle in this way. The duration of temporary
effects (such as applied poison or greater magic weapon) passes normally and may expire while the
object is in liquid form. The liquid is clearly unsafe to drink, but if, for some reason, a creature
does drink the liquid and the spell ends, the creature takes 3d6 points of damage, and brings up the
solid version of the item as a standard action in a coughing fit.

Any spell or effect that would disperse or dilute an object affected by liquefy forces the object to
attempt a Fortitude save (using the effect's DC, or DC 15 for effects with no saving throws of their
own, such as pouring a liquefied object into a stream). A failed save causes the object to gain the
broken condition. If the item is already broken, it is instead destroyed on a failed save. Liquefy
has no effect on artifacts, constructs, or intelligent magic items.
