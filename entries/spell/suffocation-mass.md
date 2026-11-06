+++
id = "ref/spell/suffocation-mass"
kind = "spell"
title = "Mass Suffocation"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "suffocation_mass", path = "json/spells16.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a vial containing a bit of the caster's breath)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "3 rounds"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Arcanist, Occultist, Psychic, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a vial containing a bit of the caster's breath)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 3 rounds
Saving throw: Fortitude partial
Spell resistance: yes
Target: one living creature
:::

## Suffocation

**Sources:** Advanced Player's Guide pg 248

This spell extracts the air from the target's lungs, causing swift suffocation. The target can
attempt to resist this spell's effects with a Fortitude save - if he succeeds, he is merely
staggered for 1 round as he gasps for breath. If the target fails, he immediately begins to
suffocate. On the target's next turn, he falls unconscious and is reduced to 0 hit points. One round
later, the target drops to -1 hit points and is dying. One round after that, the target dies. Each
round, the target can delay that round's effects from occurring by making a successful Fortitude
save, but the spell effect continues for 3 rounds, and each time a target fails his Fortitude save,
he moves one step further along the track to suffocation. This spell only affects living creatures
that must breathe. It is impossible to defeat the effects of this spell by simply holding one's
breath - if the victim fails the initial saving throw, the air in his lungs is extracted.

### Mass Suffocation

**Sources:** Advanced Player's Guide pg 248

This spell functions as suffocation except as noted above. Note that the duration of this spell is
much longer, forcing those suffering from the effect to make far more Fortitude saves to stave off
eventual suffocation.
