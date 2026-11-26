+++
id = "ref/arc-investigator/gravedigger"
kind = "archetype"
title = "Gravedigger"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Gravedigger"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gravedigger", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "horror-adventures"
page = "54"

[fields]
kind = "archetype"
features = [
  { anchor = "limited-alchemy" },
  { anchor = "grave-magic" },
  { anchor = "relic-focus", level = 1 },
  { anchor = "deny-death", level = 2 },
  { anchor = "read-the-bones", level = 2 },
  { anchor = "focus-talent" },
  { anchor = "kill-the-dead" },
  { anchor = "grave-lamp", level = 4 },
]
trades = [
  { replaces = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Trapfinding", feature = "trapfinding", by = ["relic-focus"] },
  { replaces = "trap sense", feature = "trap-sense", by = ["relic-focus"] },
  { replaces = "Poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["deny-death"] },
  { replaces = "poison immunity", feature = "poison-resistance", levels = [11], by = ["deny-death"] },
  { replaces = "Poison lore", feature = "poison-lore", by = ["read-the-bones"] },
  { replaces = "Swift alchemy", feature = "swift-alchemy", by = ["grave-lamp"] },
  { alters = "Alchemy", feature = "alchemy", by = ["limited-alchemy"] },
  { alters = "investigator talents", feature = "investigator-talent", by = ["limited-alchemy", "focus-talent"] },
  { alters = "Studied combat", feature = "studied-combat", by = ["kill-the-dead"] },
  { alters = "studied strike", feature = "studied-strike", by = ["kill-the-dead"] },
]
+++

Gravediggers pursue long-buried mysteries, figuratively and literally digging up the truth and
finding answers to secrets only moldering corpses and dry bones can tell.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A gravedigger is proficient with simple weapons and [scythes](ref/eq-weapon/scythe), and can fight
with gravediggers' tools such as a shovel or lantern as if she had the
[Catch Off-Guard](ref/feat/catch-off-guard) feat.

A gravedigger is proficient with light armor, but not with shields.

This replaces the investigator's weapon and armor proficiencies.

## Limited Alchemy {#limited-alchemy}

A gravedigger prepares and uses extracts as an investigator but gains no other benefits of the
alchemy ability. This also means that a gravedigger can't take the
[alchemist discovery](ref/invtalent/alchemist-discovery) investigator talent or any discovery that
affects or involves alchemy.

This alters alchemy and investigator talents.

## Grave Magic (Sp) {#grave-magic}

A gravedigger can sacrifice unused extract slots of the level given below or higher to use the
following spells as [spell-like abilities](ref/umr/spell-like-abilities), using her investigator
level as her caster level and her Intelligence to determine DCs: 1st—_expeditious excavation_;
2nd—_calm spirit_; 3rd—_speak with dead_; 4th—_rest eternal_; 5th—_call spirit_; 6th—_undeath to
death._

## Relic Focus (Su) {#relic-focus}

A gravedigger can form a psychic bond with a skull or bone that she has personally exhumed or
recovered from a burial site, using it as an [occultist](ref/class/occultist)
[necromancy implement](ref/implement/necromancy) and gaining its base focus power. The gravedigger
cannot invest mental focus into the implement and thus doesn't receive any resonant powers. However,
once per day she can expend one use of inspiration to use any focus power she knows that has a cost
of 1 point of mental focus (_Occult Adventures_ 47). She can do this an additional time each day at
3rd level and every 3 investigator levels thereafter. To activate a focus power that costs more than
1 point of mental focus, the gravedigger can expend that number of daily uses of this ability (as
well as uses of inspiration) at the same time. In addition, any number of times per day, she can
expend 1 use of inspiration to use _[grave words](ref/spell/grave-words)_ as
[spell-like ability](ref/umr/spell-like-abilities).

This ability replaces trapfinding and trap sense.

## Deny Death (Ex) {#deny-death}

At 2nd level, a gravedigger gains a +2 bonus on all saving throws against death effects and
[energy drain](ref/rule/energy-drain-and-negative-levels). This increases to +4 at 5th level, to +6
at 8th level, and to +8 at 11th level.

This ability replaces the investigator's poison resistance and poison immunity.

## Read the Bones (Su) {#read-the-bones}

At 2nd level, a gravedigger can perform [object reading](ref/spell/object-reading) as an occultist
(_Occult Adventures_ 48), but only on corpses, bones, and other physical remains.

This ability replaces poison lore.

## Focus Talent (Su) {#focus-talent}

A gravedigger can select a focus power for one of her implements as per an occultist of her
investigator level in place of an investigator talent.

This ability alters investigator talents.

## Kill the Dead (Ex) {#kill-the-dead}

A gravedigger focuses on battling the undead, and her studied combat and studied strike function as
if she were 2 levels lower against creatures other than undead (this means she can't use them at all
against such creatures until 6th level).

This ability alters the investigator's studied combat and studied strike.

## Grave Lamp (Su) {#grave-lamp}

At 4th level, a gravedigger can form a psychic bond with a lantern, using it as a
[conjuration](ref/implement/conjuration) implement in much the same way as she uses her relic focus
as a necromancy implement. She can expend inspiration to fuel her grave lamp's focus powers the same
number of times each day as she can for her relic focus (for example, a 6th-level gravedigger with 6
points of inspiration could expend up to three uses of inspiration as mental focus for her relic
focus and up to three uses of inspiration as mental focus for her grave lamp).

This ability replaces swift alchemy.
