+++
id = "ref/arc-vigilante/cabalist"
kind = "archetype"
title = "Cabalist"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Cabalist"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cabalist", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "55"

[fields]
kind = "archetype"
features = [
  { anchor = "spellcasting-vigilantes" },
  { anchor = "skill-ranks-per-level" },
  { anchor = "weapon-and-armor-proficiencies" },
  { anchor = "spellcasting" },
  { anchor = "spellbook" },
  { anchor = "spill-blood", level = 1 },
  { anchor = "cabalist-talents" },
  { anchor = "bond-of-blood" },
  { anchor = "familiar" },
  { anchor = "living-shadow" },
  { anchor = "necromantic-focus" },
  { anchor = "shadow-jump" },
  { anchor = "tattoo-chamber" },
  { anchor = "bloodbound-spell", level = 5 },
  { anchor = "bloody-horror", level = 11 },
  { anchor = "shadowy-appearance", level = 17 },
]
trades = [
  { replaces = "4th-, 8th-, 10th-, 14th-, and 16th-level vigilante talents", feature = "vigilante-talent", levels = [4, 8, 10, 14, 16], by = ["spellcasting"] },
  { replaces = "Vigilante specialization", feature = "vigilante-specialization", by = ["spill-blood"] },
  { replaces = "Startling appearance", feature = "startling-appearance", by = ["bloodbound-spell"] },
  { replaces = "Frightening appearance", feature = "frightening-appearance", by = ["bloody-horror"] },
  { replaces = "Stunning appearance", feature = "stunning-appearance", by = ["shadowy-appearance"] },
  { alters = "Skill ranks per level", by = ["skill-ranks-per-level"] },
  { alters = "Armor and weapon proficiencies", feature = "weapon-and-armor-proficiencies", by = ["weapon-and-armor-proficiencies"] },
  { alters = "Vigilante talents", feature = "vigilante-talent", by = ["cabalist-talents"] },
]
+++

Appearing to be an upstanding member of society, the cabalist clandestinely follows the tenets of a
secret society. Practice with blood sacrifices, necromancy, and shadow magic gives a cabalist a
reputation as a sinister and dangerous vigilante.

## Spellcasting Vigilantes {#spellcasting-vigilantes}

The spellcasting ability granted to some vigilante archetypes refers to the text of another
spellcasting class to determine how that vigilante casts spells. Unless noted otherwise, the
vigilante follows that class's rules on learning, casting, and replacing spells. It also uses the
same ability score to determine bonus spells per day, save DCs, concentration check bonus, and so on
unless noted otherwise. Class Skills: The cabalist adds Knowledge (arcana) and Spellcraft to his
list of class skills, instead of Disable Device, Knowledge (engineering), Perception, and Survival.

This alters the vigilante's class skills.

## Skill Ranks per Level {#skill-ranks-per-level}

The cabalist gains a number of skill ranks equal to 4 + his Intelligence modifier at each level,
instead of 6 + his Intelligence modifier skill ranks.

This alters the vigilante's skill ranks per level.

## Weapon and Armor Proficiencies {#weapon-and-armor-proficiencies}

A cabalist is not proficient with medium armor. Like a [magus](ref/class/magus), he can cast
cabalist spells while wearing light armor without incurring the normal arcane spell failure chance.

This alters the vigilante's armor and weapon proficiencies.

## Spellcasting {#spellcasting}

A cabalist casts arcane spells and cantrips as a magus. He prepares spells using a spellbook,
choosing them from the 6th-level and lower spells from the witch spell list; higher-level witch
spells are not on the cabalist's spell list.

This replaces the 4th-, 8th-, 10th-, 14th-, and 16th-level vigilante talents.

## Spellbook {#spellbook}

A cabalist has a spellbook that functions in the same way as a magus's spellbook but uses the
6th-level and lower spells from the witch spell list.

## Spill Blood (Ex) {#spill-blood}

A cabalist can cause bleeding when he deals piercing or slashing damage with a melee attack (or a
ranged attack within 30 feet) against a living foe who is unaware of his presence, who considers him
an ally, or who is denied its Dexterity bonus to AC. The amount of [bleed](ref/rule/bleed) damage is
equal to the cabalist's level. A cabalist can't deal this bleed damage to a creature with total
[concealment](ref/rule/concealment).

This ability replaces vigilante specialization.

## Cabalist Talents {#cabalist-talents}

A cabalist can select from the following vigilante talents, in addition to general vigilante
talents.

This alters vigilante talents.

## Bond of Blood (Sp, Su) {#bond-of-blood}

The cabalist has a magical bond to life-giving blood. When the cabalist deals bleed damage or 5 or
more points of piercing or slashing damage to an adjacent living creature, he gains 1d6
[temporary hit points](ref/rule/temporary-hit-points). These temporary hit points last for 1 hour,
and the cabalist can't gain temporary hit points again from bond of blood during that hour (even if
he loses all the temporary hit points from bond of blood before that time). The number of temporary
hit points gained increases by 1d6 for every 4 vigilante levels he has. At 4th level, the cabalist
can also activate _[blood armor](ref/spell/blood-armor)_ once per day as a
[spell-like ability](ref/umr/spell-like-abilities) as a swift action.

## Familiar (Ex) {#familiar}

The cabalist gains a [familiar](ref/sidekick/familiar), using his vigilante level as his effective
wizard level. The [familiar](ref/ability/familiars) also has a social identity as a seemingly normal
animal, though cabalists with outlandish familiars might still need to hide them.

## Living Shadow (Sp) {#living-shadow}

Once per day, the cabalist can become a living shadow as though he were using
_[shadow body](ref/spell/shadow-body)_. This effect lasts for 1 round per vigilante level, and the
cabalist can't cast spells while in this form. At 14th level, the cabalist can remain as a living
shadow for 1 minute per vigilante level instead, and can cast spells while he is a living shadow. A
cabalist must be at least 12th level to select this talent.

## Necromantic Focus (Ex) {#necromantic-focus}

The cabalist gains [Spell Focus](ref/feat/spell-focus) (necromancy) as a bonus feat. He also adds
additional spells to his spellbook from the following list, provided he can cast spells of the
appropriate level: 1st—_cause fear_, 2nd—_blindness/deafness_, 3rd—_bestow curse_, 4th—_poison_,
5th—_feast on fear_, 6th—_slay living_.

## Shadow Jump (Su) {#shadow-jump}

The cabalist gains the [shadowdancer's](ref/pclass/shadowdancer) shadow jump ability with an
effective shadowdancer level equal to his vigilante level - 6. If he has levels in shadowdancer,
those levels stack with his vigilante levels to determine the total distance per day he can shadow
jump (to a maximum of 320 feet per day). A cabalist must be at least 10th level to select this
talent.

## Tattoo Chamber (Su) {#tattoo-chamber}

The cabalist can magically absorb items through a tattoo on his hand or wrist and easily retrieve
them or activate their magical abilities without making them manifest. The items seemingly disappear
into the tattoo, but actually enter an extradimensional space that the cabalist can access via the
tattoo. Stowing an item in this way requires a full-round action, and the space can store one item
plus one additional item per 3 vigilante levels he has. These items must be items the cabalist can
hold in one hand. Retrieving a stowed item requires mentally activating the tattoo as a swift
action. The item appears in the cabalist's hand, so worn items must still be donned to gain their
benefits. The cabalist can also activate any [spell-trigger](ref/misc/spell-trigger) abilities of a
stored item as though he were wielding the item, producing the magic effect from his tattoo rather
than from the item. If the cabalist dies while items are within his tattoo chamber, those items fade
into existence within 5 feet of the corpse.

## Bloodbound Spell (Ex) {#bloodbound-spell}

At 5th level, a cabalist gets an advantage when casting spells against bleeding foes. Whenever the
cabalist casts a spell against a foe that is taking bleed damage, the foe takes a -1 penalty on its
saving throw against the spell (or to its AC if the spell requires an attack roll). This penalty
increases to -2 if the spell is from the necromancy school.

This ability replaces startling appearance.

## Bloody Horror (Ex) {#bloody-horror}

At 11th level, when a cabalist casts a spell and one of the targets (or one creature in the area for
an area spell) is taking bleed damage, the cabalist can, as a free action, make an Intimidate check
to demoralize all targets of the spell (or all creatures in the area for an area spell). The
cabalist rolls only one Intimidate check and applies the result to all the targets.

Once a creature has been the target of this ability (regardless of whether or not it was
successful), it is immune to that cabalist's bloody horror for 24 hours. This is a mind-affecting
fear effect.

This ability replaces frightening appearance.

## Shadowy Appearance (Sp) {#shadowy-appearance}

At 17th level, a cabalist becomes cloaked in shadow while in his vigilante identity. He gains a
continuous 20% miss chance (as per _[blur](ref/spell/blur)_). The cabalist can deactivate or
reactivate this effect as a standard action. Once per day, he can spend an immediate action to gain
the benefits of _[greater invisibility](ref/spell/invisibility-greater)_ for 1d6 rounds.

This ability replaces stunning appearance.
