+++
id = "ref/spell/absorb-toxicity"
kind = "spell"
title = "Absorb Toxicity"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "absorb_toxicity", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 5 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Investigator", level = 3 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a thorn from a poisonous plant)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level or until discharged"
saving_throw = "see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Alchemist, Investigator\
4: Druid, Hunter, Witch\
5: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a thorn from a poisonous plant)
Range: personal
Duration: 10 minutes/level or until discharged
Saving throw: see text
Spell resistance: no
Target: you
:::

**Sources:** Ultimate Combat pg 221

You absorb the toxicity of your surroundings, becoming toxic as a result. While under the effect of
this spell, you are immune to diseases and poisons with which you come into contact. When you are
exposed to a disease or poison, you can choose to absorb it. Doing so ends the immunity due to this
spell to any disease and poison other than the one you absorbed. You remain immune to the new
affliction until this spell ends. Casting absorb toxicity on yourself a second time does not allow
you to absorb a second toxin, but instead resets the duration of the effect to its full 10
minutes/level.

While you have a disease or poison absorbed, you can use a melee touch attack to transfer that
affliction to another creature. A missed attack does not discharge the spell, and you can try to
transfer the affliction again in subsequent rounds. If you hit, this spell is discharged, and your
target must make a saving throw against the transferred affliction (DC equal to this spell's save DC
or the affliction's save DC, whichever is higher) or suffer its effect or initial effect
immediately. The target then continues to suffer from the affliction's normal effects.

If the spell's duration expires before you have transferred the affliction, you are exposed to any
absorbed poison or disease as if you had transferred it to yourself, but you gain a +2 bonus on
saves against that particular instance of the poison or disease.
