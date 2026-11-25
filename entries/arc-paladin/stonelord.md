+++
id = "ref/arc-paladin/stonelord"
kind = "archetype"
title = "Stonelord"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Stonelord"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stonelord", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "advanced-race-guide"
page = "16"

[fields]
kind = "archetype"
features = [
  { anchor = "stonestrike", level = 1 },
  { anchor = "heartstone", level = 2 },
  { anchor = "stoneblood", level = 3 },
  { anchor = "defensive-stance", level = 4 },
  { anchor = "earth-channel", level = 4 },
  { anchor = "stone-servant", level = 5 },
  { anchor = "stonebane", level = 11 },
  { anchor = "phase-strike", level = 12 },
  { anchor = "mobile-defense", level = 18 },
  { anchor = "stone-body", level = 20 },
]
trades = [
  { replaces = "Smite evil", feature = "smite-evil", by = ["stonestrike"] },
  { replaces = "Divine grace", feature = "divine-grace", by = ["heartstone"] },
  { replaces = "Divine health", feature = "divine-health", by = ["stoneblood"] },
  { replaces = "Her mercies gained at 3rd, 9th, and 15th level", feature = "mercy", levels = [3, 9, 15], by = ["stoneblood"] },
  { replaces = "Spells", feature = "spells", by = ["defensive-stance"] },
  { replaces = "Channel positive energy", feature = "channel-positive-energy", by = ["earth-channel"] },
  { replaces = "Divine bond", feature = "divine-bond", by = ["stone-servant"] },
  { replaces = "Aura of justice", feature = "aura-of-justice", by = ["stonebane"] },
  { replaces = "12th-level mercy", feature = "mercy", levels = [12], by = ["phase-strike"] },
  { replaces = "18th-level mercy", feature = "mercy", levels = [18], by = ["mobile-defense"] },
  { replaces = "Holy champion", feature = "holy-champion", by = ["stone-body"] },
]
+++

A stonelord is a devoted sentinel of dwarven enclaves, drawing the power of the earth and ancient
stone to protect her people.

## Stonestrike (Su) {#stonestrike}

Once per day per paladin level, a stonelord can draw upon the power of the living rock. As a swift
action, she treats her melee attacks until the beginning of her next turn (whether armed or unarmed)
as magical and [adamantine](ref/eq-material/adamantine), including ignoring
[hardness](ref/umr/hardness) up to twice her paladin level, with a +1 bonus on attack and damage
rolls, as well as on combat maneuver checks. This bonus also applies to her CMD if she or her target
is touching the ground or a stone structure. This bonus increases by +1 at 5th level and every 5
levels thereafter. This ability replaces smite evil.

## Heartstone (Ex) {#heartstone}

At 2nd level, a stonelord's flesh becomes progressively rockier. She gains a +1 natural armor bonus
to AC and DR/adamantine equal to 1/2 her paladin level. The natural armor bonus increases by +1 at
6th level, and every four levels thereafter, to a maximum of +5 at 18th level. These benefits are
halved when not touching the ground or a stone structure. This ability replaces divine grace.

## Stoneblood (Ex) {#stoneblood}

At 3rd level, a stonelord's vitals begin to calcify and her blood transforms into liquid stone. She
adds her paladin level on checks to stabilize at negative hit points and gains a 25% chance to
ignore a critical hit or precision damage. This does not stack with
_[fortification](ref/magic-enh/fortification)_ armor or similar effects. At 9th level, this chance
increases to 50% and she becomes immune to petrification. At 15th level, this chance increases to
75% and she becomes immune to [bleed](ref/rule/bleed) and [blood drain](ref/umr/blood-drain)
effects. This ability replaces divine health and her mercies gained at 3rd, 9th, and 15th level.

## Defensive Stance (Ex) {#defensive-stance}

At 4th level, a stonelord gains the defensive stance ability, as a
[stalwart defender](ref/pclass/stalwart-defender), and may select one defensive power at 8th level
and every four levels thereafter. Levels of stalwart defender stack with her paladin levels when
determining the total number of rounds that she can maintain her defensive stance per day. A
stonelord does not gain any spells or spellcasting abilities, does not have a caster level, and
cannot use spell trigger or spell completion magic items.

## Earth Channel (Su) {#earth-channel}

At 4th level, a stonelord gains [Elemental Channel](ref/feat/elemental-channel) (earth) as a bonus
feat, which she may activate by spending two uses of her lay on hands ability, using her paladin
level as her effective cleric level. This ability replaces channel positive energy.

## Stone Servant (Su) {#stone-servant}

At 5th level, a stonelord may call a [Small earth elemental](ref/monster/earth-elemental) to her
side, as a paladin calls her mount. This earth elemental is Lawful Good in alignment and possesses
the [celestial](ref/template/celestial) template, and it increases in size as the stonelord gains
levels, becoming Medium at 8th level, Large at 11th level, Huge at 14th level, Greater at 17th
level, and Elder at 20th level. This ability replaces divine bond.

## Stonebane (Su) {#stonebane}

At 11th level, when using stonestrike, a stonelord's attack gains the _[bane](ref/magic-enh/bane)_
weapon special ability against creatures with the earth subtype and constructs or objects made of
earth or stone. This ability replaces aura of justice.

## Phase Strike (Su) {#phase-strike}

At 12th level, a stonelord's stonestrike may pass through stone and metal as if they weren't there.
By spending 2 uses of her stonestrike ability, she may ignore any cover less than total cover
provided by stone or metal, and she ignores any AC bonus from stone or metal armor or shields as if
wielding a _[brilliant energy](ref/magic-enh/brilliant-energy)_ weapon. A phase strike cannot damage
constructs, objects, or creatures with the earth subtype, but unlike a _brilliant energy_ weapon, it
can harm undead. This ability replaces her 12th-level mercy.

## Mobile Defense (Ex) {#mobile-defense}

At 18th level, a stonelord can make one 5-foot step per round while maintaining her defensive
stance. This ability replaces her 18th-level mercy.

## Stone Body (Ex) {#stone-body}

At 20th level, a stonelord's body transforms into living stone. She no longer needs to eat, drink,
breathe, or sleep, and she becomes immune to paralysis, poison, and stunning. She is also no longer
subject to critical hits or precision-based damage. This ability replaces holy champion.
