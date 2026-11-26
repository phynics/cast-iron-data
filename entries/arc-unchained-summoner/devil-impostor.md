+++
id = "ref/arc-unchained-summoner/devil-impostor"
kind = "archetype"
title = "Devil Impostor"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20%28Unchained%29%20Devil%20Impostor"
source_ids = ["agents-of-evil"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "devil_impostor", path = "json/archetypes_summoner_UC.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/unchained-summoner" },
]
[[sources]]
publication = "agents-of-evil"
page = "17"

[fields]
kind = "archetype"
features = [
  { anchor = "bond-alignment", level = 2 },
  { anchor = "deceptive-eidolon", level = 1 },
  { anchor = "fiendish-summons", level = 1 },
  { anchor = "devil-s-flesh", level = 4 },
  { anchor = "devil-s-tongue", level = 12 },
  { anchor = "fiendish-appearance", level = 8 },
]
trades = [
  { replaces = "Bond senses", feature = "bond-senses", by = ["bond-alignment"] },
  { replaces = "Shield ally", feature = "shield-ally", by = ["devil-s-flesh"] },
  { replaces = "Greater shield ally", feature = "greater-shield-ally", by = ["devil-s-tongue"] },
  { replaces = "Transposition", feature = "transposition", by = ["fiendish-appearance"] },
  { alters = "Eidolon", feature = "eidolon", by = ["deceptive-eidolon"] },
  { alters = "Summon monster", feature = "summon-monster-i", by = ["fiendish-summons"] },
  { alters = "Class skills" },
]
+++

Some summoners can't abide the cruelty of devils, or simply can't outwit them, but must appear to do
so to get by in Cheliax, the Outer Planes, or similar areas of infernal influence. Rather than risk
binding true devils, they reshape their eidolons into deceptive forms.

## Skills {#skills}

A devil impostor adds Bluff and Intimidate to her list of class skills. This alters the unchained
summoner's class skills.

## Bond Alignment (Su) {#bond-alignment}

At 2nd level, a devil impostor and her eidolon both radiate alignment auras of lawful evil for the
purpose of divination spells that reveal auras (such as _[detect evil](ref/spell/detect-evil)_), as
long as they remain within 1,000 feet of one another. This does not affect other abilities that
depend on alignment (such as smite evil). The devil impostor can suppress this effect for 1 minute
as a standard action. This ability replaces bond senses.

## Deceptive Eidolon {#deceptive-eidolon}

A devil impostor's eidolon always resembles a specific type of devil of the same size (caster's
choice), and radiates the aura of a lawful evil outsider under magical effects such as
_[detect evil](ref/spell/detect-evil)_, regardless of its actual alignment. The eidolon still uses
its actual alignment when resolving all other alignment-dependent abilities, effects, and spells.
The eidolon can have any subtype, though its appearance always remains that of a devil, and it can
select only evolutions available to its true subtype. This modifies the normal eidolon rules.

## Fiendish Summons (Sp) {#fiendish-summons}

A devil impostor must apply the [fiendish](ref/template/fiendish) template to any creatures summoned
via her _[summon monster](ref/spell/summon-monster)_
[spell-like ability](ref/umr/spell-like-abilities) regardless of her alignment. This alters the
unchained summoner's _summon monster_ ability.

## Devil's Flesh (Ex) {#devil-s-flesh}

At 4th level, a devil impostor's eidolon adopts several fiendish traits. The devil impostor's
eidolon gains the [skilled](ref/unchevolution/skilled) (Bluff) and
[resistance](ref/unchevolution/resistance) (fire) evolutions (or
[immunity](ref/unchevolution/immunity) \[fire\] if it already has resistance to fire). The eidolon
can select additional evolutions available to the devil subtype. This ability replaces shield ally.

## Devil's Tongue (Ex) {#devil-s-tongue}

At 12th level, the devil impostor's eidolon can apply its master's skill ranks and proficiency
bonuses when attempting Bluff, Diplomacy, and Intimidate skill checks. This ability replaces greater
shield ally.

## Fiendish Appearance (Su) {#fiendish-appearance}

At 8th level, a devil impostor can use her maker's call ability to immediately dismiss her eidolon
and take on its appearance. This functions as a modified _[alter self](ref/spell/alter-self)_ spell,
transforming the devil impostor into a replica of her eidolon. She gains a single natural attack
possessed by her eidolon, and if her eidolon is smaller than Small or larger than Medium, she
assumes the form of a Small- or Medium-sized version of her eidolon, respectively. The
transformation lasts for 10 minutes × her unchained summoner level or until the eidolon is
resummoned. This ability replaces transposition.
