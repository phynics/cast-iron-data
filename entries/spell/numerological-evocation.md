+++
id = "ref/spell/numerological-evocation"
kind = "spell"
title = "Numerological Evocation"
source_ids = ["occult-mysteries"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "numerological_evocation", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "see text"
effects = [
  { label = "Target", value = "see text" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Magus, Sorcerer, Wizard\
4: Witch
Casting time: 1 standard action
Components: V, S
Range: see text
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Target: see text
:::

**Sources:** Occult Mysteries pg 51

You can use the Path of Numbers to calculate the latent magical energies all around you and fire
customized rays of elemental energy that damage nearby targets. Roll 1d6 per 2 caster levels you
possess. This is your dice pool. You will use each die in the pool exactly once to customize
numerological evocation. Choose a number of dice in the pool, and match their results to the values
in the first column of the [Eight Basic Energies table](ref/rule/mathematical-spellcasting) to
determine the types of energy damage the spell deals. You can allocate any number of dice in this
manner, provided you still have enough dice remaining for the subsequent steps.

Next, allocate one of the dice to represent the total number of target creatures you can affect,
including the initial target. No matter how many creatures you are eligible to affect, no two
affected creatures can be more than 15 feet apart. Next, allocate any number of the dice to
represent the range of numerological resistance. The range of the spell is 10 × the sum of the
allocated dice. Finally, add up the results of the dice remaining in the pool. This is the amount of
damage that numerological evocation deals to the first creature hit. A successful Reflex save halves
this damage. Secondary targets take 50% of the damage dealt to the first creature hit (rounded up),
and successful Reflex saves negate this damage.
