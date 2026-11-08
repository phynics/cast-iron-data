+++
id = "ref/spell/hollow-heroism-greater"
kind = "spell"
title = "Greater Hollow Heroism"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hollow_heroism_greater", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/heroism-greater" },
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

### Greater Hollow Heroism

**Sources:** Ultimate Intrigue pg 216

This spell functions as [greater heroism](ref/spell/heroism-greater), except that you can reverse
the spell by issuing a special command as a standard action if you are within medium range (100
feet + 10 feet per caster level) of the target. The target loses the bonuses and instead takes a -4
penalty on attack rolls, saving throws, and skill checks until the spell's duration ends (no save),
increasing to a -8 penalty against fear effects. Additionally, she takes damage equal to your caster
level when you reverse the spell.

Attempts to identify greater hollow heroism with a skill check incorrectly identify it as greater
heroism.
