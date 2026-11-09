+++
id = "ref/spell/evaluators-lens"
kind = "spell"
title = "Evaluator's Lens"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "evaluators_lens", path = "json/spells4.json" },
]
[[sources]]
publication = "black-markets"
page = "30"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Inquisitor", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 2 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Effect", value = "see text" },
]
duration = "1 minute/level or until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Inquisitor, Summoner\
3: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level or until discharged
Saving throw: none
Spell resistance: no
Effect: see text
Subschool: Creation
:::

You summon an insubstantial lens of force 4 inches in diameter that hovers in front of your face.
When you attempt a saving throw against a spell with the figment or pattern descriptor, you can roll
twice and take the higher result. You gain a +10 enhancement bonus on Appraise checks to appraise
the worth of an item viewed through the lens, and you never judge an item's value wildly
inaccurately. If you successfully identify that the item has magical properties, you can immediately
attempt a Spellcraft check to determine the item's properties, as if you had cast
[detect magic](ref/spell/detect-magic) on the item and examined it for 3 rounds. This spell cannot
determine the properties of artifacts.

The lens cannot be targeted or harmed by physical attacks, but
[dispel magic](ref/spell/dispel-magic), [disintegrate](ref/spell/disintegrate), or a
[rod of cancellation](ref/magic-rod/rod-of-cancellation) affects it. The lens's AC against touch
attacks is equal to 10 + your Dexterity modifier.
