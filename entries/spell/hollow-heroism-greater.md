+++
id = "ref/spell/hollow-heroism-greater"
kind = "spell"
title = "Greater Hollow Heroism"
source_ids = ["core-rulebook", "mythic-adventures", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hollow_heroism_greater", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 6 },
  { class = "Psychic", level = 7 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Bard, Skald\
7: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Target: creature touched
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Subschool: Compulsion
Descriptors: mind-affecting
:::

## Heroism

**Sources:** PRPG Core Rulebook pg 295

This spell imbues a single creature with great bravery and morale in battle. The target gains a +2
morale bonus on attack rolls, saves, and skill checks.

### Mythic Heroism

**Sources:** Mythic Adventures pg 98

The morale bonus increases to +4 and applies on all checks, attack rolls, saves, and weapon damage
rolls. Allies adjacent to the target gain a +4 morale bonus on saves against fear effects.

_Augmented (3rd):_ If you expend two uses of mythic power, the target can attempt one additional
attack per round when taking a full attack action (as if using a haste spell). The target can use
this additional attack ability a number of times equal to your tier.

### Greater Heroism

**Sources:** PRPG Core Rulebook pg 295

This spell functions like heroism, except the creature gains a +4 morale bonus on attack rolls,
saves, and skill checks, immunity to fear effects, and temporary hit points equal to your caster
level (maximum 20).

### Hollow Heroism

**Sources:** Ultimate Intrigue pg 216

This spell functions as heroism, except that you can reverse the spell by issuing a special command
as a standard action if you are within medium range (100 feet + 10 feet per caster level) of the
target. The target loses the bonuses and instead takes a -2 penalty on attack rolls, saving throws,
and skill checks until the spell's duration ends (no save).

Attempts to identify hollow heroism with a skill check incorrectly identify it as heroism.

### Greater Hollow Heroism

**Sources:** Ultimate Intrigue pg 216

This spell functions as greater heroism, except that you can reverse the spell by issuing a special
command as a standard action if you are within medium range (100 feet + 10 feet per caster level) of
the target. The target loses the bonuses and instead takes a -4 penalty on attack rolls, saving
throws, and skill checks until the spell's duration ends (no save), increasing to a -8 penalty
against fear effects. Additionally, she takes damage equal to your caster level when you reverse the
spell.

Attempts to identify greater hollow heroism with a skill check incorrectly identify it as greater
heroism.
