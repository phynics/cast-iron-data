+++
id = "ref/rule/effects-of-sanity-damage"
kind = "rule"
title = "Effects of Sanity Damage"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "effects_of_sanity_damage", path = "json/rules_campaign_types02.json" },
]

[fields]
kind = "none"
+++

**Sources:** Horror Adventures pg 12

When you experience a potential sanity attack, you must typically succeed at a Will saving throw to
shake off or reduce the sanity attack's damage. Whether this saving throw is successful or not, if
the sanity damage from a single sanity attack is equal to or greater than your sanity threshold, you
gain a [madness](ref/rule/madness) with a potency based on the relation between your total sanity
damage accrued and your sanity edge (lesser if the total sanity damage is below your sanity edge,
greater otherwise). In most cases, GMs should choose a madness that reflects the horror faced or
your deep fears and potential mental breaking points rather than rolling on tables. For instance, if
you gain a lesser madness due to an encounter with a [mummy](ref/monster/mummy) or some other undead
that features a fear effect, it might make sense to choose the [phobia](ref/madness/phobia) madness.
If you already suffer from [delirium](ref/madness/delirium) and gain a greater madness, it might
make sense for that madness to be increased to [schizophrenia](ref/madness/schizophrenia). However,
when a random madness is appropriate, the GM can generate one by rolling on Table 5-1 (for a lesser
madness) or Table 5-2 (for a greater madness).

You are afflicted with a madness until that madness is removed. You may not always manifest the
madness, though. If you are afflicted with madness and then are healed of all sanity damage, all of
your madnesses become dormant until you accrue further sanity damage. Typically, a dormant madness
does not affect you at all, but some madnesses feature an effect that occurs only while that madness
is dormant. A lesser madness that becomes dormant does not manifest again until you take sanity
damage equal to or greater than your sanity edge. A greater madness stays dormant only as long as
your total sanity damage remains at 0. Dormant madnesses, no matter the potency, can be removed only
by [miracle](ref/spell/miracle) or [wish](ref/spell/wish).

Lastly, if your total sanity damage equals or exceeds your sanity score, you become insane as per
insanity (no saving throw) until all your sanity damage is healed and all your madnesses are cured.

While _Horror Adventures_ introduces a number of spells, feats, monsters, or other effects that deal
sanity damage, the GM is also encouraged to create her own sanity-damage-dealing effects in her
horror game. The table below gives a number of examples of situations that might cause a character
to take sanity damage.

|Situation|DC|Failure|Success|
| --- | --- | --- | --- |
|The first time a character encounters a dead body|10|1d3 sanity damage|0 sanity damage|
|The first time a character encounters a gruesome scene of death|12|1d6 sanity damge|1 sanity damage|
|The first time a character encounters a horrifying creature\*|10 + CR of the creature|Sanity damage equal to 1/2 the creature's CR|Sanity damage equal to 1/4 the creature's CR|
|Each time a character encounters a [qlippoth](ref/subtype/qlippoth) or other creature with a particularly horrific appearance|10 + CR of the creature|Sanity damage equal to the creature's CR|Sanity damage equal to 1/2 the creature's CR|
|Each time a character encounters a [Great Old One](ref/family/great-old-one)|15 + CR of the creature|Sanity Damage equal to double the creature's CR|Sanity damage qual to the creature's CR|

\* Horrifying creatures are typically aberrations, evil or chaotic outsiders, and undead. "Each
time" could mean the first time for each creature type, or each time a creature encounters a new
kind of specific creature of that type (for example, the first time a creature encounters a skeleton
and then again the first time the character encounters a wraith), at the GM's discretion.

### Expanded Sanity

Effects dealing sanity damage and [madnesses](ref/rule/madness) are mind-affecting effects, and as
such certain creature types are immune to them. In horror games, the GM may want to make an
exception to this, at least in the case of sanity damage and madnesses, allowing undead and even
some kinds of plant and construct creatures to feel the effects of insanity. The GM should be
careful to determine whether the creature's immunity to mind-affecting effects compensates for an
extremely poor Will save and potentially give a bonus on Will saves against sanity damage to such
creatures.
