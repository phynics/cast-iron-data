+++
id = "ref/spell/claim-identity-greater"
kind = "spell"
title = "Greater Claim Identity"
source_ids = ["spymasters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "claim_identity_greater", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/claim-identity" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 5 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Inquisitor", level = 5 },
  { class = "Investigator", level = 5 },
  { class = "Shaman", level = 6 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (a silver needle costing 100 gp)"
range = "touch"
effects = [
  { label = "Target", value = "humanoid creature touched" },
]
duration = "1 hour/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Antipaladin\
5: Alchemist, Bard, Inquisitor, Investigator, Skald, Witch\
6: Arcanist, Druid, Hunter, Shaman, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a silver needle costing 100 gp)
Range: touch
Target: humanoid creature touched
Duration: 1 hour/level
Saving throw: Fortitude negates
Spell resistance: yes
Subschool: Polymorph
:::

## Claim Identity

**Sources:** Spymaster's Handbook pg 28

You steal the target's face, transforming yourself into a flawless imitation of it. All of the
target's facial features, vocal cues, and identifying physical traits change, transforming it into
an unremarkable member of its race and gender. You transform into a perfect likeness of the target's
true form, as if affected by alter self, and gain a +10 bonus on Disguise checks to impersonate the
original subject of this spell; you take no penalties on this check if the original target is of a
different race, age, size, or gender.

Claim identity prevents any other polymorph effects from restoring the target's true face for the
spell's duration, though the target can still assume other forms or faces via magic or any natural
shapechanging ability.

### Greater Claim Identity

**Sources:** Spymaster's Handbook pg 28

This spell functions as per [claim identity](ref/spell/claim-identity), except it transforms its
target into a helpless, inanimate porcelain mask for the spell's duration. The target remains aware
of everything it can see or hear while transformed. The target can't speak or move, but can still
take purely mental actions (such as casting certain spells) or be targeted by spells that affect its
mind.

Any creature donning this mask is transformed into a flawless imitation of the spell's target, as if
affected by claim identity, and reverts to its natural form upon removing the mask. Any damage dealt
to the mask immediately ends this spell.
