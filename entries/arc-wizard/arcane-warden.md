+++
id = "ref/arc-wizard/arcane-warden"
kind = "archetype"
title = "Arcane Warden"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Arcane%20Warden"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_warden", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "blood-of-the-ancients"
page = "14"

[fields]
kind = "archetype"
features = [
  { anchor = "universal-magic" },
  { anchor = "ready-for-anything", level = 1 },
  { anchor = "generous-touch" },
  { anchor = "restorative-shelter" },
]
trades = [
  { replaces = "Scribe Scroll", feature = "scribe-scroll", by = ["ready-for-anything"] },
  { replaces = "The bonus feats gained at 5th, 10th, 15th, and 20th levels", feature = "bonus-feats", levels = [5, 10, 15, 20], by = ["ready-for-anything"] },
  { replaces = "Hand of the apprentice universalist school ability", feature = "arcane-school", power = "hand of the apprentice", by = ["generous-touch"] },
  { replaces = "Metamagic mastery universalist school ability", feature = "arcane-school", power = "metamagic mastery", by = ["restorative-shelter"] },
  { alters = "Arcane school", feature = "arcane-school", by = ["universal-magic"] },
  { alters = "Class skills" },
]
+++

In the aftermath of Earthfall, some elven wizards from Mierani chose to remain behind and provide
aid to others. These elves were and still are highly honored by their kin, as they sacrificed the
easy comfort and refuge of Castrovel to brave the wreckage of Earthfall in order to save what
short-lived human lives they could. Although Golarion has long since recovered from Earthfall, the
elven arcane warden traditions remain particularly useful for those who face long-term explorations
of hostile environments—whether on Golarion or the planes beyond. The arcane wardens of today are
wizards who specialize in the discovery or generation of places of safety and refuge.

## Universal Magic {#universal-magic}

An arcane warden values all schools of magic and recognizes that, faced with an unpredictable world,
versatility is one of the greatest tools for survival. All arcane warden wizards must be
[universalists](ref/arcaneschool/universalist).

This alters arcane school.

## Class Skills {#class-skills}

An arcane warden focuses his training on survival, be it navigating difficult regions, enduring in
the wilderness, or aiding others in such conditions. He gains Climb, Heal, Survival, and Swim as
class skills. Appraise, Fly, Knowledge (nobility), and Linguistics are not class skills for the
arcane warden.

This alters the wizard's class skills.

## Ready for Anything (Ex) {#ready-for-anything}

Instead of crafting magical items or learning ways to manipulate metamagic, arcane wardens prefer to
spend their time providing safety and refuge for others. At 1st level, an arcane warden gains a
bonus feat associated with aiding allies or providing shelter. At 5th, 10th, 15th, and 20th levels,
the arcane warden gains an additional bonus feat. The arcane warden must qualify for any feat he
takes, and must choose from the following list: [Alertness](ref/feat/alertness),
[Endurance](ref/feat/endurance), [Great Fortitude](ref/feat/great-fortitude),
[Improved Great Fortitude](ref/feat/improved-great-fortitude), [Leadership](ref/feat/leadership),
[Self-Sufficient](ref/feat/self-sufficient), [Skill Focus](ref/feat/skill-focus) (Survival),
[Toughness](ref/feat/toughness), or any teamwork feat.

This replaces Scribe Scroll and the bonus feats gained at 5th, 10th, 15th, and 20th levels.

## Generous Touch (Su) {#generous-touch}

Arcane wardens are talented at enhancing the magical effects they create to bolster allies. When an
arcane warden casts a spell with a target of "creature touched" on a willing target other than
himself, he can cause the effects of the spell to last longer than normal. A spell with a duration
of 1 round per level lasts an additional number of rounds equal to the arcane warden's Intelligence
modifier (minimum of 1 additional round). A spell with a duration of 1 minute per level lasts for an
additional number of minutes equal to the arcane warden's Intelligence modifier (minimum of 1
additional minute). Spells with different durations than this are not enhanced by this ability. Only
one spell can be enhanced in this way on any individual creature at a time.

This replaces the hand of the apprentice universalist school ability.

## Restorative Shelter (Su) {#restorative-shelter}

While an arcane warden can find refuge in many naturally occurring hideaways, his preferred places
of rest are magically created cottages, homes, and even manors. An arcane warden learns the
following spells_: [mage's magnificent mansion](ref/spell/mages-magnificent-mansion)_,
_[rope trick](ref/spell/rope-trick)_, _[secure shelter](ref/spell/secure-shelter)_, and
_[tiny hut](ref/spell/tiny-hut)_. These spells do not take up room in the arcane warden's spellbook,
and he does not need his spellbook to prepare these spells. He must still be the appropriate level
to prepare the spell in question. The arcane warden's caster level is treated as 2 higher than his
actual caster level for the purposes of determining the duration of these spells and resolving
attempts to dispel these spells. Any creature that spends at least 8 hours relaxing in one of these
shelters gains a bonus equal to the level of the spell that created it on any saving throws against
disease or poison effects made in the next 24 hours.

This replaces the metamagic mastery universalist school ability.
