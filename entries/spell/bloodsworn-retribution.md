+++
id = "ref/spell/bloodsworn-retribution"
kind = "spell"
title = "Bloodsworn Retribution"
source_ids = ["dwarves-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bloodsworn_retribution", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 6 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 6 },
  { class = "Paladin", level = 4 },
  { class = "Ranger", level = 4 },
  { class = "Warpriest", level = 6 },
]
casting_time = "1 round"
components = "V, S, M (your blood)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "special (see text)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Hunter, Paladin, Ranger\
6: Cleric, Oracle, Warpriest
Casting time: 1 round
Components: V, S, M (your blood)
Range: personal
Duration: special (see text)
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Dwarves of Golarion pg 22

> _In order to prepare this spell, the caster must spend an hour performing a ritual in which he
> beseeches [Torag](ref/faith/torag) (or a member of his family) for the aid of
> [Dranngvit](ref/faith/dranngvit). For 24 hours after the ritual, the caster may prepare spells of
> the requested deity. The caster may only attune himself to one additional deity at a time._

When you cast this spell, you cut yourself and swear an oath of retribution on your own blood. You
decide how much damage you want to take from this attack, up to 25 points. This damage cannot be
healed for as long as the spell is in effect. Anytime you perform an attack, save, or check that is
directly related to the oath and brings you closer to the fulfillment of that oath, you gain a
morale bonus to that roll equal to the number of hit points of damage you took from the oath divided
by 5. The GM is the final arbiter over whether or not an action qualifies for this bonus. When you
fulfill the oath (or choose to forsake it), the spell ends, and the lost hit points can be healed as
normal.

For example, a notorious bandit leader killed Stigur's brother, and Stigur wants to avenge his
brother's death. Stigur casts this spell and sacrifices 20 hit points. Thereafter Stigur gains a +4
morale bonus on attack rolls against the bandit leader's minions, saves against spells from said
minions, Intimidate checks to coerce an informant to tell him where the bandit leader is camped, and
so on.
