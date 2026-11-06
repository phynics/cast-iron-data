+++
id = "ref/rule/rule-sanity-and-madness/curing-insanity"
kind = "rule"
title = "Curing Insanity"
source_ids = ["game-mastery-guide", "horror-adventures"]
section = ["Sanity and Madness"]
parent = "ref/rule/sanity-and-madness"
provenance = [
  { dataset = "pathfinder-data-1-e", record = "json/rules_gm07.json#sanity_and_madness|section:curing-insanity", path = "json/rules_gm07.json" },
]

[fields]
kind = "none"
+++

All insanities have a DC that represents the insanity's strength. An insanity's DC indicates the
Will save you need to roll in order to resist contracting the insanity when you are initially
exposed to it, but also the DC you need to make to recover. Recovering from an insanity naturally is
a lengthy process - once per week, you make a Will save against the insanity's current DC. If you
succeed on this save, the insanity's DC is reduced by a number of points equal to your Charisma
bonus (minimum of 1). You continue to suffer the full effects of the insanity until its DC is
reduced to 0, at which point you are cured and the insanity vanishes completely.

[Lesser restoration](ref/spell/restoration-lesser) has no effect on insanity, but
[restoration](ref/spell/restoration) reduces the current DC of one insanity currently affecting a
target by an amount equal to the caster's level.
[Greater restoration](ref/spell/restoration-greater), [heal](ref/spell/heal),
[limited wish](ref/spell/limited-wish), [miracle](ref/spell/miracle), or [wish](ref/spell/wish)
immediately cures a target of all insanity.
