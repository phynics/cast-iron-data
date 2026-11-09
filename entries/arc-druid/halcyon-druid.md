+++
id = "ref/arc-druid/halcyon-druid"
kind = "archetype"
title = "Halcyon Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Halcyon%20Druid"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "halcyon_druid", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "adventurers-guide"
page = "121"

[fields]
kind = "archetype"
replaces = ["Nature bond", "Nature sense", "Wild empathy", "Spontaneous casting", "Wild shape", "Resist nature's lure", "A thousand faces"]
alters = ["Class skills"]
+++

Druids of the Halcyon Circle embrace [the teachings of Old-Mage Jatembe](ref/rule/aff-i-school),
combining them with traditional druidic practices. Though they revere the natural world, halcyon
druids are less focused on emulating its inhabitants. Instead, like Old-Mage Jatembe, they treat
with beings from the Outer Sphere. As a sign of their allegiance, these druids wear fantastical
masks depicting celestials, fiends, and (most often) the bestial agathions.

Halcyon druids are peacekeepers, mediating between people and nature, people and the spirit world,
and different groups of people. Yet when necessary, they use their magic to fight enemies of peace,
especially demons and demon cultists.

Most halcyon druids serve Nantambu and the surrounding villages - making, memorizing, and
arbitrating the unwritten pacts between them. Some halcyon druids, however, are drawn farther
afield. They may do so to forge new connections between tribes and villages, to spread the message
of peace, or to fight demonic outbreaks.

**Bonded Mask (Su)**

**Ability:** A halcyon druid forms a powerful bond with a mask, which functions identically to a
[wizard's](ref/class/wizard) _bonded object_ except that it can be used to cast druid spells
(including those gained from class abilities) instead of wizard spells. A _bonded mask_ must be worn
to have an effect, and it occupies the [head slot](ref/rule/magic-items-on-the-body). A halcyon
druid can enhance her mask with abilities appropriate for a head slot item, and can designate an
existing head slot item as her _bonded mask_ (but only if it covers her face).

**Replaces:** Nature bond

**Bonded Object**

**Action:** Ability

**Flavor:** Text from the wizard class

If you select a bonded object, you begin play with one at no cost. These objects are always
masterwork quality. If you attempt to cast a spell without your bonded object worn, you must make a
[concentration](ref/rule/concentration) check or lose the spell. The DC for this check is equal to
20 + the spell's level.

A bonded object can be used once per day to cast any one spell that you have in your spellbook and
are capable of casting, even if the spell is not prepared. This spell is treated like any other
spell cast by you, including casting time, duration, and other effects dependent on your level. This
spell cannot be modified by metamagic feats or other abilities. The bonded object cannot be used to
cast spells from your opposition schools.

You can add additional magic abilities to your bonded object as if you have the required item
creation feats and if you meet the level prerequisites of the feat. For example, a wizard with a
bonded dagger must be at least 5th level to add magic abilities to the dagger (see
[Craft Magic Arms and Armor](ref/feat/craft-magic-arms-and-armor)). The magic properties of a bonded
object, including any magic abilities added to the object, only function for the wizard who owns it.
If a bonded object's owner dies, or the item is replaced, the object reverts to being an ordinary
masterwork item of the appropriate type.

If a bonded object is damaged, it is restored to full hit points the next time you prepare your
spells. If the object of an arcane bond is lost or destroyed, it can be replaced after 1 week in a
special ritual that costs 200 gp per wizard level plus the cost of the masterwork item. This ritual
takes 8 hours to complete. Items replaced in this way do not possess any of the additional
enchantments of the previous bonded item. You can designate an existing magic item as your bonded
item. This functions in the same way as replacing a lost or destroyed item except that the new magic
item retains its abilities while gaining the benefits and drawbacks of becoming a bonded item.

**Magaambya-Trained (Ex)**

**Alters:** Class skills

**Passive:** A halcyon druid adds [Diplomacy](ref/skill/diplomacy) (CHA) and all
[Knowledge](ref/skill/knowledge-all) (INT) skills to her list of class skills.

**Replaces:** Nature sense

**Peacekeeper (Ex)**

**Passive:** A halcyon druid adds [half](ref/misc/fractions-and-rounding) her class level (minimum
1) to Diplomacy and Knowledge (local) checks.

**Replaces:** Wild empathy

**Spontaneous Casting**

**Ability:** A halcyon druid adds all spells from the Good cleric domain to her druid spell list,
and she can focus stored spell energy into spells from the Good domain that she hasn't prepared
ahead of time. She can lose a prepared spell to cast any spell of the same level or lower from the
Good domain.

**Replaces:** Spontaneous casting

**Natural Arcana (Su)**

**Choice:** A halcyon druid chooses two spells from the wizard/sorcerer spell list and adds them to
her druid spell list. The chosen spells must be at least 1 level lower than the highest level spell
she can currently cast.

**At 20th Level:** She gains two more bonus spells, but they can be of any level.

**At 6th Level:** She adds two more bonus spells, following the same rules and restrictions above.

**Gained:** At 4th Level

**Repeat:** She gains two more bonus spells., 8, 2, 18

**Replaces:** Wild shape

**Resist Fiendish Influence (Ex)**

**Gained:** At 4th Level

**Passive:** A halcyon druid gains a +4 bonus on saving throws against the spell-like and
supernatural abilities of outsiders with the evil subtype and spells with the evil descriptor.

**Replaces:** Resist nature's lure

**Embody Mask (Sp)**

**Gained:** At 13th Level

**Replaces:** A thousand faces

**Standard:** A halcyon druid wearing her _bonded mask_ can embody the spirit it represents, which
can be any Tiny to Large [agathion](ref/family/agathion), [angel](ref/family/angel),
[archon](ref/family/archon), or [azata](ref/family/azata). This ability functions as per
[beast shape IV](ref/spell/beast-shape-4) (using the adjustments for magical beasts), but adds the
following abilities if the assumed form has them: _aura of menace, protective aura, speak with
animals, telepathy,_ and _truespeech._ If the assumed form has [immunity](ref/umr/immunity) to a
condition, the druid gains a +4 bonus on saving throws against effects that cause that condition.

**Usage:** 1 minute/day per druid level; these minutes need not be consecutive, but must be spent in
1-minute increments
