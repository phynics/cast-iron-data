+++
id = "ref/arc-slayer/witch-killer"
kind = "archetype"
title = "Witch Killer"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Witch%20Killer"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "witch_killer", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "horror-adventures"
page = "67"

[fields]
kind = "archetype"
features = [
  { anchor = "studied-witch", level = 1 },
  { anchor = "superstitious" },
  { anchor = "lingering-thrust", level = 4 },
  { anchor = "scent-magic", level = 5 },
  { anchor = "burn-the-witch", level = 10 },
]
trades = [
  { replaces = "Slayer talent gained at 4th level", feature = "slayer-talents", levels = [4], by = ["lingering-thrust"] },
  { replaces = "Slayer talent gained at 10th level", feature = "slayer-talents", levels = [10], by = ["burn-the-witch"] },
  { alters = "Studied target", feature = "studied-target", by = ["studied-witch"] },
  { alters = "Slayer talents", feature = "slayer-talents", by = ["superstitious"] },
  { alters = "Class skills" },
]
+++

Born into cultures where magic users are hated and feared, witch killers devote their lives to purge
the arcane taint from the world.

## Class Skills {#class-skills}

A witch killer adds Knowledge (arcana) and Spellcraft to his list of class skills.

This alters the slayer's class skills.

## Studied Witch (Ex) {#studied-witch}

A witch killer's studied combat bonus applies on Spellcraft checks and saving throws against arcane
spells and [spell-like abilities](ref/umr/spell-like-abilities) and hexes. This bonus is reduced by
1 (minimum 0) if the target is not an arcane spellcaster, or a being called or summoned by arcane
magic. He does not gain the increases to the maximum number of studied targets he can have at a time
normally attained at 5th, 10th, 15th, and 20th levels, but his bonuses still increase at those
levels.

This ability alters studied target.

## Superstitious (Ex) {#superstitious}

Instead of being able to select ranger combat style feats as slayer talents, a witch killer can
select any of the following barbarian rage powers as slayer talents, treating his slayer level as
his barbarian level: [clear mind](ref/ragepower/clear-mind), [disruptive](ref/ragepower/disruptive),
[eater of magic](ref/ragepower/eater-of-magic), [spell sunder](ref/ragepower/spell-sunder),
[spellbreaker](ref/ragepower/spellbreaker), [sunder enchantment](ref/ragepower/sunder-enchantment),
[superstition](ref/ragepower/superstition), or [witch hunter](ref/ragepower/witch-hunter). If the
witch killer selects a rage power that can normally be used only once per rage (eater of magic,
spell sunder, or sunder enchantment), he can use it once per day per 5 slayer levels he possesses,
though no more than once per round in any event. The other rage powers affect the slayer constantly,
though the superstition and witch hunter rage powers apply only against arcane spells and spell-like
abilities and the creatures that use them.

## Lingering Thrust (Ex) {#lingering-thrust}

At 4th level, when a witch killer's attack against an arcane spellcaster in the midst of casting
forces the spellcaster to attempt a [concentration](ref/rule/concentration) check, the witch killer
adds half his slayer level to the check's DC. When he makes a sneak attack against an arcane
spellcaster, up to 1 point of sneak attack damage per slayer level counts as ongoing damage for the
purpose of forcing the spellcaster to attempt concentration checks (the witch killer does not add
half his slayer level to this DC).

This ability replaces the slayer talent gained at 4th level.

## Scent Magic (Su) {#scent-magic}

At 5th level, a witch killer can detect arcane magic by scent. He can use
_[detect magic](ref/spell/detect-magic)_ at will (as per a [paladin's](ref/class/paladin) ability to
[detect evil](ref/spell/detect-evil)), but only against arcane magic, and the ability is scent-based
and thus defeated by effects like _[negate aroma](ref/spell/negate-aroma)_. Even when he isn't
concentrating on using his magic scent, when a creature within scent range casts an arcane spell
(including arcane [spell-like abilities](ref/umr/spell-like-abilities) or magic item effects), the
witch killer automatically pinpoints the caster's location.

## Burn the Witch (Sp) {#burn-the-witch}

At 10th level, once per day when a witch killer observes a creature within 30 feet cast an arcane
spell or use an arcane [spell-like ability](ref/umr/spell-like-abilities), he can use
_[foster hatred](ref/spell/foster-hatred)_ on that character, or target one creature harmed by the
arcane effect with _[vengeful outrage](ref/spell/vengeful-outrage)_, identifying the caster as the
enemy. He can use this ability twice per day at 15th level, and he can use this ability three times
per day at 20th level. The save DC is Charisma-based and uses the witch killer's slayer level as his
caster level.

This ability replaces the slayer talent normally gained at 10th level.
