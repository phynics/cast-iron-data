+++
id = "ref/spell/analyze-dweomer"
kind = "spell"
title = "Analyze Dweomer"
aon = "SpellDisplay.aspx?ItemName=Analyze%20Dweomer"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "analyze_dweomer", path = "json/spells.json" },
]
[[sources]]
publication = "core-rulebook"
page = "240"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 6 },
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Investigator", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, F (a ruby and gold lens worth 1,500 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one object or creature per caster level" },
]
duration = "1 round/level (D)"
saving_throw = "none or Will negates; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 6: Alchemist, Arcanist, Bard, Investigator, Occultist, Psychic, Skald, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a ruby and gold lens worth 1,500 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none or Will negates; see text
Spell resistance: no
Targets: one object or creature per caster level
:::

You can observe magical auras. Each round, you may examine a single creature or object that you can
see as a free action. In the case of a magic item, you learn its functions (including any curse
effects), how to activate its functions (if appropriate), and how many charges are left (if it uses
charges). In the case of an object or creature with active spells cast upon it, you learn each
spell, its effect, and its caster level.

An attended object may attempt a Will save to resist this effect if its holder so desires. If the
save succeeds, you learn nothing about the object except what you can discern by looking at it. An
object that makes its save cannot be affected by any other analyze dweomer spells for 24 hours.

Analyze dweomer does not function when used on an artifact.
