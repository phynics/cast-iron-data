+++
id = "ref/spell/plundered-power"
kind = "spell"
title = "Plundered Power"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "plundered_power", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Druid", level = 7 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 6 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "10 minutes"
components = "V, S, M (crushed rubies worth 2,500 gp and a major organ from the sacrificed target, see text)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 day/level"
saving_throw = "Will negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Occultist, Summoner, Unchained Summoner\
7: Arcanist, Cleric, Druid, Oracle, Shaman, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (crushed rubies worth 2,500 gp and a major organ from the sacrificed target, see text)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 day/level
Saving throw: Will negates
Spell resistance: no
Target: one creature
Descriptors: evil
:::

**Sources:** Horror Adventures pg 124

You must sacrifice a creature just as you finish casting this spell. When the sacrifice dies, its
blood or ichor pools and hardens into a single red bloodstone. This bloodstone contains the essence
and spirit of the sacrificed creature, allowing anyone holding the stone to activate the creature's
highest-level activated racial [spell-like ability](ref/umr/spell-like-abilities), taking the
actions necessary to activate the stored spell-like ability. Any creature who holds the stone can
activate it, but the stone can be used only once per day (or the frequency of the creature's
spell-like ability, whichever is less). If a creature has several racial spell-like abilities of the
same spell level, choose randomly from among them to determine which one is stored in the
bloodstone. The bloodstone can only store racial spell-like abilities that emulate a spell,
including altered spells, like invisibility (self only), but not unique spell-like abilities
possessed by the creature. Abilities with altered effects are still altered, so a creature
activating the bloodstone for [greater teleport](ref/spell/teleport-greater) (self only) would
affect only itself and a bloodstone storing [summon monster II](ref/spell/summon-monster-2) (Small
fire elemental only) would still only be able to summon a Small fire elemental. Additionally, the
bloodstone can't store spell-like abilities that duplicate spells with expensive components costing
more than 250 gp.

The save DC, caster level, and other attributes of this ability remain the same as when the creature
was still alive, though the creature who activates the bloodstone can choose the targets, area, or
shape of the spell, and make other decisions, such as controlling the target of dominate person. The
bloodstone can take any actions necessary to manipulate aspects of the spell, concentrating on the
spell, redirecting the spell, and so on, up to a full normal round's worth of actions.

If the sacrificed creature doesn't die during the casting of the spell (for instance if it was
merely a summoned creature) or is brought back to life before the spell's duration expires, the
bloodstone loses its magical power. The fragment of the creature's spirit trapped in the bloodstone
does not hinder attempts to restore the creature to life.
