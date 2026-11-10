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
replaces = ["Inspire courage", "Suggestion", "Inspire greatness", "Inspire heroics", "Mass suggestion", "Deadly performance", "Bardic knowledge", "Versatile performance", "Inspire competence", "Lore master"]
replaces_features = ["bardic-knowledge", "versatile-performance", "lore-master"]
+++

Combining performance with stealth, trickery, and guile, the sandman uses cleverness to keep others
off-balance.

**Bardic Performance**

**Info:** A sandman gains the following types of bardic performance.

**Stealspell (Su)**

**Ability:** A sandman can use performance to steal spells from his foes and add them to his list of
spells known. Once the performance is started, the bard can steal a prepared spell or a spell known
from another creature with a touch attack as a standard action. The target receives a Will save (DC
10 + [half](ref/misc/fractions-and-rounding) the bard's level + the bard's Cha bonus) to negate the
effect. The sandman may choose a spell to steal, but if the target does not possess the spell, the
bardic performance immediately ends. Otherwise the spell stolen is random, but it is always of the
highest level that the bard can cast, if possible. The target loses the prepared spell or spell
known and the sandman adds it to his list of spells known for as long as the performance continues,
after which it reverts to the original recipient.

**Info:** While stolen, the bard can cast the spell using his available spell slots. This use does
not consume the stolen spell. If the bard steals another spell while a spell is stolen, the previous
spell immediately reverts to its original owner.

**Replaces:** Inspire courage

**Special:** This ability requires visual components.

**Slumber Song (Sp)**

**At 6th Level:** A sandman can use his performance to cause a creature he has already _fascinated_
to fall asleep (as [deep slumber](ref/spell/deep-slumber), but with no HD limit). Otherwise, this
ability functions like [suggestion](ref/performance/suggestion).

**Replaces:** Suggestion

**Dramatic Subtext (Su)**

**At 9th Level:** A sandman can use bardic performance to cast spells without obvious visual or
audible components while retaining the spell's normal effects. Observers must succeed at a
Perception check opposed by a sandman's Sleight of Hand check to notice that the sandman is the
source of the spellcasting (though spellcasting still provokes attacks of opportunity).

**Replaces:** Inspire greatness

**Special:** The bard must use this performance for at least 2 rounds before casting a spell;
otherwise he is automatically detected and the performance ends.

**Greater Stealspell (Su)**

**At 15th Level:** A sandman's _stealspell_ power improves. When a target fails a save against his
_stealspell_ performance, the sandman discovers its [spell resistance](ref/rule/spell-resistance)
(if any) and all spells it has prepared or knows. He can then choose which spell to steal. The
sandman may forgo stealing a spell and instead reduce the target's SR by an amount equal to half his
bard level and gain that amount of spell resistance for as long as he continues performing.

**Replaces:** Inspire heroics

**Special:** If he steals additional [spell resistance](ref/rule/spell-resistance), it stacks with
previously stolen SR. If he steals a spell or ceases performing, the spell resistance immediately
reverts back to its owner.

**Mass Slumber Song (Sp)**

**At 18th Level:** A sandman can use _slumber song_ to affect any number of _fascinated_ creatures
within 30 feet. Otherwise, this ability functions like
[mass suggestion](ref/performance/mass-suggestion).

**Replaces:** Mass suggestion

**Spell Catching (Su)**

**Immediate:** A sandman who saves against a spell or
[spell-like ability](ref/umr/spell-like-abilities) that targets only him (not including area spells)
may respond with his bardic performance. He must attempt a caster level check (DC 10 + the spell's
original caster level). If it succeeds, the sandman can absorb the spell effect without harm and
immediately recast that spell (using the original caster's level and save DC) or any spell he knows
of that level or lower.

**Gained:** At 20th Level

**Replaces:** Deadly performance

**Special:** Using this ability consumes a number of rounds of bardic performance equal to the
spell's level, even if the check fails.

**Master of Deception (Ex)**

**Ability:** He may also disarm magical traps with Disable Device as a rogue's
[trapfinding](ref/ability/trapfinding) ability.

**Passive:** A sandman gains a bonus equal to half his level on Bluff, Sleight of Hand, and Stealth
checks.

**Replaces:** Bardic knowledge

**Sneakspell (Ex)**

**At 10th Level:** The save DC now increases by +2.

**At 14th Level:** The bonus on caster level checks becomes +4.

**At 18th Level:** The save DC now increases by +3.

**At 2nd Level:** A sandman adds +1 to the save DC of spells and bardic performance against
opponents who are denied their Dex bonus.

**At 6th Level:** He gains a +2 bonus on caster level checks to overcome
[spell resistance](ref/rule/spell-resistance) against such foes.

**Replaces:** Versatile performance

**Trap Sense (Ex)**

**Gained:** At 3rd Level

**Passive:** A sandman gains a bonus on Reflex saves against traps and a dodge bonus to AC against
traps. These bonuses are equal to one-third of his bard level.

**Replaces:** Inspire competence

**Sneak Attack (Ex)**

**Ability:** A sandman inflicts extra damage against targets within 30 feet that he flanks or that
are denied their Dex bonus to AC against him. This damage is equal to +1d6 points for every five
bard levels he has (e.g, a 15th-level sandman would deal +3d6 extra damage).

**Replaces:** Lore master
