+++
id = "ref/arc-bard/sandman"
kind = "archetype"
title = "Sandman"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Sandman"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sandman", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "advanced-players-guide"
page = "82"

[fields]
kind = "archetype"
features = [
  { anchor = "bardic-performance" },
  { anchor = "stealspell" },
  { anchor = "slumber-song", level = 6 },
  { anchor = "dramatic-subtext", level = 9 },
  { anchor = "greater-stealspell" },
  { anchor = "mass-slumber-song", level = 18 },
  { anchor = "spell-catching", level = 20 },
  { anchor = "master-of-deception" },
  { anchor = "sneakspell", level = 2 },
  { anchor = "trap-sense", level = 3 },
  { anchor = "sneak-attack", level = 5 },
]
trades = [
  { replaces = "Inspire courage", feature = "bardic-performance", power = "inspire courage", by = ["stealspell"] },
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["slumber-song"] },
  { replaces = "Inspire greatness", feature = "bardic-performance", power = "inspire greatness", by = ["dramatic-subtext"] },
  { replaces = "Inspire heroics", feature = "bardic-performance", power = "inspire heroics", by = ["greater-stealspell"] },
  { replaces = "Mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["mass-slumber-song"] },
  { replaces = "Deadly performance", feature = "bardic-performance", power = "deadly performance", by = ["spell-catching"] },
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["master-of-deception"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["sneakspell"] },
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["trap-sense"] },
  { replaces = "Lore master", feature = "lore-master", by = ["sneak-attack"] },
]
+++

Combining performance with stealth, trickery, and guile, the sandman uses cleverness to keep others
off-balance.

## Bardic Performance {#bardic-performance}

A sandman gains the following types of bardic performance.

## Stealspell (Su) {#stealspell}

A sandman can use performance to steal spells from his foes and add them to his list of spells
known. Once the performance is started, the bard can steal a prepared spell or a spell known from
another creature with a touch attack as a standard action. The target receives a Will save (DC 10 +
1/2 the bard's level + the bard's Cha bonus) to negate the effect. The sandman may choose a spell to
steal, but if the target does not possess the spell, the bardic performance immediately ends.
Otherwise the spell stolen is random, but it is always of the highest level that the bard can cast,
if possible. The target loses the prepared spell or spell known and the sandman adds it to his list
of spells known for as long as the performance continues, after which it reverts to the original
recipient. While stolen, the bard can cast the spell using his available spell slots. This use does
not consume the stolen spell. If the bard steals another spell while a spell is stolen, the previous
spell immediately reverts to its original owner. This ability requires visual components. This
performance replaces inspire courage.

## Slumber Song (Sp) {#slumber-song}

At 6th level, a sandman can use his performance to cause a creature he has already fascinated to
fall asleep (as _[deep slumber](ref/spell/deep-slumber)_, but with no HD limit). Otherwise, this
ability functions like [suggestion](ref/performance/suggestion). This performance replaces
suggestion.

## Dramatic Subtext (Su) {#dramatic-subtext}

At 9th level, a sandman can use bardic performance to cast spells without obvious visual or audible
components while retaining the spell's normal effects. Observers must succeed at a Perception check
opposed by a sandman's Sleight of Hand check to notice that the sandman is the source of the
spellcasting (though spellcasting still provokes attacks of opportunity). The bard must use this
performance for at least 2 rounds before casting a spell; otherwise he is automatically detected and
the performance ends. This ability replaces inspire greatness.

## Greater Stealspell (Su) {#greater-stealspell}

A sandman's stealspell power improves at 15th level. When a target fails a save against his
stealspell performance, the sandman discovers its [spell resistance](ref/rule/spell-resistance) (if
any) and all spells it has prepared or knows. He can then choose which spell to steal. The sandman
may forgo stealing a spell and instead reduce the target's SR by an amount equal to half his bard
level and gain that amount of [spell resistance](ref/rule/spell-resistance) for as long as he
continues performing. If he steals additional spell resistance, it stacks with previously stolen SR.
If he steals a spell or ceases performing, the spell resistance immediately reverts back to its
owner. This performance replaces inspire heroics.

## Mass Slumber Song (Sp) {#mass-slumber-song}

At 18th level, a sandman can use slumber song to affect any number of fascinated creatures within 30
feet. Otherwise, this ability functions like _[mass suggestion](ref/performance/mass-suggestion)_.
This performance replaces _mass suggestion_.

## Spell Catching (Su) {#spell-catching}

At 20th level, a sandman who saves against a spell or
[spell-like ability](ref/umr/spell-like-abilities) that targets only him (not including area spells)
may use bardic performance as an immediate action. He must attempt a caster level check (DC 10 + the
spell's original caster level). If it succeeds, the sandman can absorb the spell effect without harm
and immediately recast that spell (using the original caster's level and save DC) or any spell he
knows of that level or lower. Using this ability consumes a number of rounds of bardic performance
equal to the spell's level, even if the check fails. This performance replaces deadly performance.

## Master of Deception (Ex) {#master-of-deception}

A sandman gains a bonus equal to half his level on Bluff, Sleight of Hand, and Stealth checks. He
may also disarm magical traps with Disable Device as a rogue's
[trapfinding](ref/ability/trapfinding) ability. This ability replaces bardic knowledge.

## Sneakspell (Ex) {#sneakspell}

At 2nd level, a sandman adds +1 to the save DC of spells and bardic performance against opponents
who are denied their Dex bonus. This increases to +2 at 10th level and +3 at 18th level. In
addition, at 6th level he gains a +2 bonus on caster level checks to overcome
[spell resistance](ref/rule/spell-resistance) against such foes, and this bonus increases to +4 at
14th level. This ability replaces versatile performance.

## Trap Sense (Ex) {#trap-sense}

At 3rd level, a sandman gains a +1 bonus on Reflex saves against traps and a +1 dodge bonus to AC
against traps. These bonuses increase by +1 every three levels after 3rd. This ability replaces
inspire competence.

## Sneak Attack (Ex) {#sneak-attack}

At 5th level, a sandman inflicts +1d6 points of damage against targets within 30 feet that he flanks
or that are denied their Dex bonus to AC against him. This damage increases by +1d6 every five
levels after 5th. This ability replaces lore master.
