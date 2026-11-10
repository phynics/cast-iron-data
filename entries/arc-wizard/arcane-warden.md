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
replaces = ["Scribe Scroll, 5th-, 10th-, 15th-, and 20th-level bonus feats", "Hand of the apprentice universalist school ability", "Metamagic mastery universalist school ability"]
alters = ["Arcane school"]
replaces_features = ["scribe-scroll"]
alters_features = ["arcane-school"]
+++

In the aftermath of Earthfall, some elven wizards from Mierani chose to remain behind and provide
aid to others. These elves were and still are highly honored by their kin, as they sacrificed the
easy comfort and refuge of Castrovel to brave the wreckage of Earthfall in order to save what
short-lived human lives they could. Although Golarion has long since recovered from Earthfall, the
elven arcane warden traditions remain particularly useful for those who face long-term explorations
of hostile environments - whether on Golarion or the planes beyond. The arcane wardens of today are
wizards who specialize in the discovery or generation of places of safety and refuge.

**Universal Magic**

**Alters:** Arcane school

**Info:** An arcane warden values all schools of magic and recognizes that, faced with an
unpredictable world, versatility is one of the greatest tools for survival. All arcane warden
wizards must be [universalists](ref/arcaneschool/universalist).

**Gained class skills:** climb, heal, sur, swim

**Lost class skills:** app, fly, kno, ling

**Ready for Anything (Ex)**

**Flavor:** Instead of crafting magical items or learning ways to manipulate metamagic, arcane
wardens prefer to spend their time providing safety and refuge for others.

**At 1st Level:** An arcane warden gains a bonus feat associated with aiding allies or providing
shelter. The arcane warden must qualify for any feat he takes, and must choose from the following
list: [Alertness](ref/feat/alertness), [Endurance](ref/feat/endurance),
[Great Fortitude](ref/feat/great-fortitude),
[Improved Great Fortitude](ref/feat/improved-great-fortitude), [Leadership](ref/feat/leadership),
[Self-Sufficient](ref/feat/self-sufficient), [Skill Focus](ref/feat/skill-focus) (Survival),
[Toughness](ref/feat/toughness), or any teamwork feat.

**Repeat:** The arcane warden gains an additional bonus feat., 5, 5

**Replaces:** Scribe Scroll, 5th-, 10th-, 15th-, and 20th-level bonus feats

**Generous Touch (Su)**

**Ability:** When an arcane warden casts a spell with a target of &quot&creature touched&quot& on a
willing target other than himself, he can cause the effects of the spell to last longer than normal.
A spell with a duration of 1 round per level lasts an additional number of rounds equal to the
arcane warden's Intelligence modifier (minimum of 1 additional round). A spell with a duration of 1
minute per level lasts for an additional number of minutes equal to the arcane warden's Intelligence
modifier (minimum of 1 additional minute). Spells with different durations than this are not
enhanced by this ability. Only one spell can be enhanced in this way on any individual creature at a
time.

**Flavor:** Arcane wardens are talented at enhancing the magical effects they create to bolster
allies.

**Replaces:** _Hand of the apprentice_ universalist school ability

**Restorative Shelter (Su)**

**Ability:** An arcane warden learns the following spells:
[mage's magnificent mansion](ref/spell/mages-magnificent-mansion),
[rope trick](ref/spell/rope-trick), [secure shelter](ref/spell/secure-shelter), and
[tiny hut](ref/spell/tiny-hut). These spells do not take up room in the arcane warden's spellbook,
and he does not need his spellbook to prepare these spells. He must still be the appropriate level
to prepare the spell in question.

**Flavor:** While an arcane warden can find refuge in many naturally occurring hideaways, his
preferred places of rest are magically created cottages, homes, and even manors.

**Replaces:** _Metamagic mastery_ universalist school ability

**Special:** The arcane warden's caster level is treated as 2 higher than his actual caster level
for the purposes of determining the duration of these spells and resolving attempts to dispel these
spells. Any creature that spends at least 8 hours relaxing in one of these shelters gains a bonus
equal to the level of the spell that created it on any saving throws against disease or poison
effects made in the next 24 hours.
