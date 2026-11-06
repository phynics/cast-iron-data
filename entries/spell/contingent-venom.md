+++
id = "ref/spell/contingent-venom"
kind = "spell"
title = "Contingent Venom"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "contingent_venom", path = "json/spells6.json" },
]

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

## Languid Venom

**Sources:** Ultimate Intrigue pg 218

You greatly extend the time it takes for the poison you touch to take effect, giving that poison an
onset time up to 1 hour per caster level. (You touch the poison's container, so you don't risk
exposing yourself to a contact poison.) The target doesn't attempt a saving throw when initially
exposed to the languid venom, but instead saves at the end of the poison's onset time. If the poison
is neutralized or otherwise cured prior to the end of its onset time, it is rendered harmless.
Failing saves against multiple doses of languid venom have the normal cumulative effect for poisons.

Languid venom is difficult to detect or identify. Detect poison and similar effects detect languid
venomobscure poison - those effects don't stack. Use only the caster level check with the higher DC
and increase the DC of the check to identify the poison by the higher of the two.

If cast upon a venomous creature, languid venom delays the onset of that creature's poison when the
creature next delivers its natural poison.

### Contingent Venom

**Sources:** Ultimate Intrigue pg 208

This spell functions as languid venom, but you can stipulate a specific condition or circumstance
that will end the poison's onset time and cause it to take effect. The conditions for triggering the
poison can be as general or as detailed as desired, but the triggers must be visual or audible (as
per magic mouth) or else based on physical contact with or consumption of a specific object,
substance, or creature. This triggering condition can either result in the immediate onset of the
poison, or cause the poison to take effect a number of rounds after being triggered no greater than
1 round per caster level. You must make all decisions involving triggering when you cast contingent
venom, and you can't change those decisions later.
