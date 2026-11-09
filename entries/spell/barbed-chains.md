+++
id = "ref/spell/barbed-chains"
kind = "spell"
title = "Barbed Chains"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "barbed_chains", path = "json/spells12.json" },
]
[[sources]]
publication = "horror-adventures"
page = "109"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
descriptors = ["emotion", "fear", "mind-affecting"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a length of chain doused with fresh blood)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "a chain sharpened at one end" },
]
duration = "instantaneous"
saving_throw = "Will partial (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Antipaladin, Bloodrager, Cleric, Inquisitor, Occultist, Oracle, Shaman, Summoner, Unchained Summoner
Casting time: 1 standard action
Components: V, S, M (a length of chain doused with fresh blood)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will partial (see text)
Spell resistance: no
Effect: a chain sharpened at one end
Subschool: Summoning
Descriptors: emotion, fear, mind-affecting
:::

You summon a chain from another realm, causing it to burst out from the ground and strike a target
within the spell's range. You can have the chain either make a melee attack (dealing 1d6 points of
slashing damage) or attempt a trip combat maneuver against the target. The chain uses your base
attack bonus plus your key spellcasting ability score modifier as its attack bonus and combat
maneuver bonus. On a successful hit or combat maneuver check, the target must attempt a Will save.
If it fails its save, the creature is shaken for 1d4 rounds. You summon one additional chain every 3
levels after 1st, for a total of two chains at 4th level, three at 7th level, and a maximum of four
at 10th level. Multiple chains can attack the same target but the shaken effect doesn't stack.
