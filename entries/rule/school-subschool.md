+++
id = "ref/rule/school-subschool"
kind = "rule"
title = "Name, School, Subschool, Descriptor"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "school_subschool", path = "json/rules_basics04.json" },
]
[[sources]]
publication = "core-rulebook"
page = "209"

[fields]
kind = "none"
+++

The first line of every spell description gives the name by which the spell is generally known.

Beneath the spell name is a line giving the school of magic (and the subschool, if any) to which the
spell belongs.

Almost every spell belongs to one of eight schools of magic. A school of magic is a group of related
spells that work in similar ways.

- [Abjuration](ref/spelldef/abjuration)
- [Divination](ref/spelldef/divination)
- [Conjuration](ref/spelldef/conjuration)
- [Enchantment](ref/spelldef/enchantment)
- [Evocation](ref/spelldef/evocation)
- [Illusion](ref/spelldef/illusion)
- [Necromancy](ref/spelldef/necromancy)
- [Transmutation](ref/spelldef/transmutation)

Some of the schools have _subschools_ which further delineate their effects. And a small number of
spells ([arcane mark](ref/spell/arcane-mark), [limited wish](ref/spell/limited-wish),
[permanency](ref/spell/permanency), [prestidigitation](ref/spell/prestidigitation), and
[wish](ref/spell/wish)) are [universal](ref/spelldef/universal), belonging to no school.

Appearing on the same line as the school and subschool, when applicable, is a descriptor that
further categorizes the spell in some way. Some spells have more than one descriptor.

The descriptors are [acid](ref/spelldef/acid), [air](ref/spelldef/air),
[chaotic](ref/spelldef/chaotic), [cold](ref/spelldef/cold), [curse](ref/spelldef/curse),
[darkness](ref/spelldef/darkness), [death](ref/spelldef/death), [disease](ref/spelldef/disease),
[draconic](ref/spelldef/draconic), [earth](ref/spelldef/earth),
[electricity](ref/spelldef/electricity), [emotion](ref/spelldef/emotion), [evil](ref/spelldef/evil),
[fear](ref/spelldef/fear), [fire](ref/spelldef/fire), [force](ref/spelldef/force),
[good](ref/spelldef/good), [language-dependent](ref/spelldef/language-dependent),
[lawful](ref/spelldef/lawful), [light](ref/spelldef/light), [meditative](ref/spelldef/meditative),
[mind-affecting](ref/spelldef/mind-affecting), [pain](ref/spelldef/pain),
[poison](ref/spelldef/poison), [ruse](ref/spelldef/ruse), [shadow](ref/spelldef/shadow-descriptor),
[sonic](ref/spelldef/sonic), and [water](ref/spelldef/water).

Most of these descriptors have no game effect by themselves, but they govern how the spell interacts
with other spells, with special abilities, with unusual creatures, with alignment, and so on.

A _language-dependent_ spell uses intelligible language as a medium for communication. If the target
cannot understand or cannot hear what the caster of a _language-dependant_ spell says, the spell
fails.

A _mind-affecting_ spell works only against creatures with an Intelligence score of 1 or higher.
