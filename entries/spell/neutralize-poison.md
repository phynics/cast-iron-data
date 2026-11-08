+++
id = "ref/spell/neutralize-poison"
kind = "spell"
title = "Neutralize Poison"
source_ids = ["core-rulebook", "dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "neutralize_poison", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Adept", level = 3 },
  { class = "Alchemist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (charcoal)"
range = "touch"
effects = [
  { label = "Target", value = "creature or object of up to 1 cu. ft./level touched" },
]
duration = "instantaneous or 10 min./level; see text"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Adept, Druid, Hunter, Ranger\
4: Alchemist, Bard, Cleric, Inquisitor, Investigator, Oracle, Paladin, Shaman, Skald, Spiritualist, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, M/DF (charcoal)
Range: touch
Duration: instantaneous or 10 min./level; see text
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: creature or object of up to 1 cu. ft./level touched
Subschool: Healing
:::

**Sources:** PRPG Core Rulebook pg 316

You detoxify any sort of venom in the creature or object touched. If the target is a creature, you
must make a caster level check (1d20 + caster level) against the DC of each poison affecting the
target. Success means that the poison is neutralized. A cured creature suffers no additional effects
from the poison, and any temporary effects are ended, but the spell does not reverse instantaneous
effects, such as hit point damage, temporary ability damage, or effects that don't go away on their
own.

This spell can instead neutralize the poison in a poisonous creature or object for 10 minutes per
level, at the caster's option. If cast on a creature, the creature receives a Will save to negate
the effect.
