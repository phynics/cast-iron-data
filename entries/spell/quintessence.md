+++
id = "ref/spell/quintessence"
kind = "spell"
title = "Quintessence"
aon = "SpellDisplay.aspx?ItemName=Quintessence"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "quintessence", path = "json/spells8.json" },
]
[[sources]]
publication = "occult-adventures"
page = "184"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature or object touched" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates (harmless) and Will disbelief, see text"
spell_resistance = "see text"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Arcanist, Bard, Medium, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless) and Will disbelief, see text
Spell resistance: see text
Target: creature or object touched
Subschool: Glamer
Descriptors: glamer
:::

You draw forth the idealized image of the target creature or object, masking any flaws or damage. An
injured or ill creature appears healthy, and a damaged object or one with the broken condition
appears intact. However, a corpse masked by quintessence remains obviously dead, and a completely
destroyed object can't be made to seem whole. This illusion has visual and tactile components.
Careful examination of or handling the target grants a saving throw to disbelieve, but casual
observation does not. Using a broken object for its intended purpose automatically reveals the
deception. Appraise checks to assess the value of an object affected by quintessence estimate the
value as an item of its type in perfect condition, unless the appraiser disbelieves the illusion.

Unwilling targets can negate the spell's effect on them with successful Will saves or with
[spell resistance](ref/rule/spell-resistance). Those who interact with the target can attempt Will
saves to see through the glamer, but spell resistance doesn't apply. Quintessence counters and
dispels [decrepit disguise](ref/spell/decrepit-disguise).
