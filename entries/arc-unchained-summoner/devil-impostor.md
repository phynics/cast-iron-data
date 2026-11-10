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
replaces = ["Bond senses", "Shield ally", "Greater shield ally", "Transposition"]
alters = ["Eidolon", "Summon monster"]
replaces_features = ["bond-senses", "shield-ally", "greater-shield-ally", "transposition"]
alters_features = ["eidolon"]
+++

Some summoners can't abide the cruelty of devils, or simply can't outwit them, but must appear to do
so to get by in Cheliax, the Outer Planes, or similar areas of infernal influence. Rather than risk
binding true devils, they reshape their eidolons into deceptive forms.

**Gained class skills:** bluff, intm

**Bond Alignment (Su)**

**Gained:** At 2nd Level

**Passive:** A devil impostor and her eidolon both radiate alignment auras of lawful evil for the
purpose of divination spells that reveal auras (such as [detect evil](ref/spell/detect-evil)), as
long as they remain within 1,000 feet of one another. This does not affect other abilities that
depend on alignment (such as _smite evil_).

**Replaces:** Bond senses

**Special:** The devil impostor can suppress this effect for 1 minute as a **standard action**.

**Deceptive Eidolon**

**Alters:** Eidolon

**Info:** A devil impostor's eidolon always resembles a specific type of devil of the same size
(caster's choice), and radiates the aura of a lawful evil outsider under magical effects such as
_[detect evil](ref/spell/detect-evil),_ regardless of its actual alignment. The eidolon still uses
its actual alignment when resolving all other alignment-dependent abilities, effects, and spells.
The eidolon can have any subtype, though its appearance always remains that of a devil, and it can
select only evolutions available to its true subtype.

**Fiendish Summons (Sp)**

**Alters:** Summon monster

**Passive:** A devil impostor must apply the [fiendish](ref/template/fiendish) template to any
creatures summoned via her _[summon monster](ref/spell/summon-monster)_
[spell-like ability](ref/umr/spell-like-abilities) regardless of her alignment.

**Devil's Flesh (Ex)**

**Ability:** The devil impostor's eidolon gains the [skilled](ref/unchevolution/skilled) (Bluff) and
[resistance](ref/unchevolution/resistance) (fire) evolutions (or
[immunity](ref/unchevolution/immunity) \[fire\] if it already has resistance to fire). The eidolon
can select additional evolutions available to the devil subtype.

**Flavor:** A devil impostor's eidolon adopts several fiendish traits.

**Gained:** At 4th Level

**Replaces:** Shield ally

**Devil's Tongue (Ex)**

**Gained:** At 12th Level

**Passive:** The devil impostor's eidolon can apply its master's skill ranks and proficiency bonuses
when attempting Bluff, Diplomacy, and Intimidate skill checks.

**Replaces:** Greater shield ally

**Fiendish Appearance (Su)**

**Ability:** A devil impostor can use her _maker's call_ ability to immediately dismiss her eidolon
and take on its appearance. This functions as a modified [alter self](ref/spell/alter-self) spell,
transforming the devil impostor into a replica of her eidolon. She gains a single natural attack
possessed by her eidolon, and if her eidolon is smaller than Small or larger than Medium, she
assumes the form of a Small- or Medium-sized version of her eidolon, respectively. The
transformation lasts for 10 minutes &times& her unchained summoner level or until the eidolon is
resummoned.

**Gained:** At 8th Level

**Replaces:** Transposition
