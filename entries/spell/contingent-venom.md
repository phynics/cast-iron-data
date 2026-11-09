+++
id = "ref/spell/contingent-venom"
kind = "spell"
title = "Contingent Venom"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "contingent_venom", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/languid-venom" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "208"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["poison"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (herbs used in antitoxin worth 25 gp)"
range = "touch"
effects = [
  { label = "Target", value = "one dose of poison or one venomous creature" },
]
duration = "permanent until discharged (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Alchemist, Arcanist, Investigator, Shaman, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (herbs used in antitoxin worth 25 gp)
Range: touch
Duration: permanent until discharged (D)
Saving throw: Fortitude negates
Spell resistance: yes
Target: one dose of poison or one venomous creature
Descriptors: poison
:::

### Contingent Venom

This spell functions as [languid venom](ref/spell/languid-venom), but you can stipulate a specific
condition or circumstance that will end the poison's onset time and cause it to take effect. The
conditions for triggering the poison can be as general or as detailed as desired, but the triggers
must be visual or audible (as per magic mouth) or else based on physical contact with or consumption
of a specific object, substance, or creature. This triggering condition can either result in the
immediate onset of the poison, or cause the poison to take effect a number of rounds after being
triggered no greater than 1 round per caster level. You must make all decisions involving triggering
when you cast contingent venom, and you can't change those decisions later.
