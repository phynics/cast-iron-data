+++
id = "ref/spell/languid-venom"
kind = "spell"
title = "Languid Venom"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "languid_venom", path = "json/spells6.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "218"

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
