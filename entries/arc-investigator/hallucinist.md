+++
id = "ref/arc-investigator/hallucinist"
kind = "archetype"
title = "Hallucinist"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Hallucinist"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hallucinist", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "34"

[fields]
kind = "archetype"
features = [
  { anchor = "psychedelic-perception" },
  { anchor = "drug-lore", level = 2 },
  { anchor = "drug-resistance", level = 2 },
  { anchor = "shared-hallucinations", level = 3 },
  { anchor = "simultaneous-study", level = 6 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["psychedelic-perception"] },
  { replaces = "Trap sense gained at 3rd level", feature = "trap-sense", levels = [3], by = ["psychedelic-perception"] },
  { replaces = "investigator talents gained at 3rd, 7th, 11th, and 15th levels", feature = "investigator-talent", levels = [3, 7, 11, 15], by = ["psychedelic-perception"] },
  { replaces = "Poison lore", feature = "poison-lore", by = ["drug-lore"] },
  { replaces = "All instances of poison resistance", feature = "poison-resistance", by = ["drug-resistance"] },
  { replaces = "poison immunity", by = ["drug-resistance"] },
  { replaces = "Keen recollection", feature = "keen-recollection", by = ["shared-hallucinations"] },
  { replaces = "investigator talents gained at 5th and 9th levels", feature = "investigator-talent", levels = [5, 9], by = ["shared-hallucinations"] },
  { replaces = "All remaining trap sense", feature = "trap-sense", levels = [6, 9, 12, 15, 18], by = ["simultaneous-study"] },
  { alters = "Studied combat", feature = "studied-combat", by = ["simultaneous-study"] },
]
+++

A hallucinist imbibes magical drugs to expand his mind into the psychedelic world, extending his
awareness to things he could not normally perceive. While a hallucinist's body sways oddly under the
effects of his hallucinogen, it grants him strange insights that reveal things to him that others
can't see. Hallucinists know that others can't function with these expanded senses, and they use
that fact to repurpose their hallucinations as distractions or assaults against their enemies.

## Psychedelic Perception (Su) {#psychedelic-perception}

In addition to magical extracts, a hallucinist learns to swiftly mix various psychoactive
substances, using a fraction of his own power to create a magical hallucinogen that he can imbibe to
grant himself powers of psychedelic perception. A hallucinogen follows all the normal rules and
restrictions for an alchemist's mutagen as if they were the same substance, just as a
[cognatogen](ref/discovery/cognatogen) does.

At 1st level, the effects of a hallucinogen last for 1 minute per investigator level, and the
hallucinogen grants [low-light vision](ref/rule/low-light-vision) and a +2 insight bonus on
Perception checks, but imposes a -2 penalty to his Dexterity. At 3rd level, the duration increases
to 10 minutes per the hallucinist's investigator level and the insight bonus on Perception checks
increases to +4. At 7th level, the hallucinogen also grants
_[see invisibility](ref/spell/see-invisibility)_ and [darkvision](ref/rule/darkvision) 60 feet (or
if the hallucinist drinking it already has darkvision, it increases the range of the darkvision by
30 feet) and the Perception bonus increases to +6. At 11th level, the hallucinogen also grants
_[aura sight](ref/spell/aura-sight)_ and the Perception bonus increases to +8. At 15th level, the
hallucinogen also grants [blindsense](ref/umr/blindsense) 60 feet and the Perception bonus increases
to +10.

This ability replaces trapfinding, the trap sense gained at 3rd level, and the investigator talents
gained at 3rd, 7th, 11th, and 15th levels.

## Drug Lore (Ex) {#drug-lore}

At 2nd level, a hallucinist has a deep understanding and appreciation of [drugs](ref/rule/drugs). If
the hallucinist spends 1 minute physically examining a drug, he can attempt a Knowledge (nature)
check to identify any natural drug or a Knowledge (arcana) check to identify any magical drug (DC =
the drug's addiction saving throw DC). Once he identifies a drug, he can spend 1 minute and attempt
a Craft (alchemy) check (DC = the drug's addiction saving throw DC) to neutralize 1 dose of the
drug. Success renders the dose harmless. The hallucinist has no chance of accidentally drugging
herself when examining or attempting to neutralize a drug.

This ability replaces poison lore.

## Drug Resistance (Ex) {#drug-resistance}

At 2nd level, a hallucinist gains a +2 bonus on all saving throws against drug
[addiction](ref/rule/addiction). This bonus increases to +4 at 5th level, and to +6 at 8th level. At
11th level, a hallucinist becomes completely immune to drug addiction, but he can choose to lower
this immunity for any particular drug. If he becomes addicted to a drug, he must fully recover from
the addiction before he can resume his immunity to addiction to that drug.

This ability replaces all instances of poison resistance and poison immunity.

## Shared Hallucinations (Sp) {#shared-hallucinations}

At 3rd level, a hallucinist under the effects of his hallucinogen can share and manipulate his
hallucinatory revelations. By expending 10 minutes of the duration of his hallucinogen or one use of
inspiration, he can create an effect similar to _[minor image](ref/spell/minor-image)_ or
_[oneiric horror](ref/spell/oneiric-horror)_. At 5th level, he can create an effect similar to
_[synesthesia](ref/spell/synesthesia)_.

Any of the effects remain only while the hallucinist concentrates upon it, for up to 1 round per
hallucinist's investigator level, but otherwise function as the spell. The DC of saving throws
against these effects is equal to 10 + 1/2 the hallucinist's investigator level + his modifier.

At 9th level, a hallucinist can expend 10 minutes of the duration of the hallucinogen or one use of
inspiration to use _[aura alteration](ref/spell/aura-alteration)_ on one creature or object (unlike
the other three abilities, this does not require concentration).

This ability replaces keen recollection, and the investigator talents gained at 5th and 9th levels.

## Simultaneous Study (Su) {#simultaneous-study}

At 6th level and every 3 investigator levels thereafter, the expanded mind of a hallucinist is able
to maintain his studied combat bonuses against an additional target at the same time. In order to do
so, the hallucinist must be using his psychedelic perception ability and must expend one use of
inspiration in order to designate each target beyond the first target (this cost stacks with the use
of inspiration required to designate a target more than once per 24 hours). He still needs to take a
move action for each target, designating them one at a time. The hallucinist can discard this
connection to a target of studied combat as a free action, allowing him to study another target in
its place.

This ability alters studied combat and replaces all remaining trap sense.
