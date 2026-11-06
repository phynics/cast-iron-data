+++
id = "ref/spell/claim-identity-greater"
kind = "spell"
title = "Greater Claim Identity"
source_ids = ["spymasters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "claim_identity_greater", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a needle and thread)"
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
Level: 3: Alchemist, Antipaladin, Bard, Inquisitor, Investigator, Skald, Witch\
4: Arcanist, Druid, Hunter, Shaman, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a needle and thread)
Range: touch
Duration: 1 hour/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: humanoid creature touched
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

This spell functions as per claim identity, except it transforms its target into a helpless,
inanimate porcelain mask for the spell's duration. The target remains aware of everything it can see
or hear while transformed. The target can't speak or move, but can still take purely mental actions
(such as casting certain spells) or be targeted by spells that affect its mind.

Any creature donning this mask is transformed into a flawless imitation of the spell's target, as if
affected by claim identity, and reverts to its natural form upon removing the mask. Any damage dealt
to the mask immediately ends this spell.
