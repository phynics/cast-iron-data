+++
id = "ref/arc-paladin/faithful-wanderer"
kind = "archetype"
title = "Faithful Wanderer"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Faithful%20Wanderer"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "faithful_wanderer", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "18"

[fields]
kind = "archetype"
replaces = ["Detect evil", "Aura of good", "aura of justice", "Smite evil", "Holy champion"]
alters = ["Skills per level", "Aura of courage", "aura of resolve", "aura of faith", "aura of righteousness", "Divine bond"]
replaces_features = ["detect-evil", "aura-of-good", "aura-of-justice", "smite-evil", "holy-champion"]
alters_features = ["aura-of-courage", "aura-of-resolve", "aura-of-faith", "aura-of-righteousness", "divine-bond"]
+++

While most paladins stride brazenly forth to battle evil in gleaming armor, faithful wanderers
understand that to accomplish real change in Abyssal environments, a paladin must learn to be
self-sufficient and unobtrusive and that she must pick her battles carefully, lest her mission end
abruptly in a blaze of glory.

**Gained class skills:** kna, kp, per, stl, sur

**Lost class skills:** diplo, ha, kno, ride

**Wanderer's Lore**

**Alters:** Skills per level

**Flavor:** A faithful wanderer quickly learns that everything in the wastes is evil, and she
develops the skills she needs to survive.

**Info:** A faithful wanderer gains a number of skill ranks equal to 4 + her Intelligence modifier
at each level (instead of gaining a number of skill ranks equal to 2 + her Intelligence modifier).

**Replaces:** Detect evil

**Hidden Aura (Su)**

**Alters:** Aura of courage, aura of resolve, aura of faith, aura of righteousness

**At 11th Level:** She takes no penalties even in areas with strongly chaos- and evil-aligned planar
traits.

**At 14th Level:** She leaves no trail in areas with chaos- and evil-aligned planar traits, can't be
tracked in such terrain, and can use Stealth to hide in such terrain, even if the terrain doesn't
grant cover or concealment.

**At 17th Level:** She can use Stealth to hide in areas with these planar traits even while being
observed.

**At 3rd Level:** Her alignment aura emulates the
[alignment planar traits](ref/rule/alignment-traits) of her current location (e.g. chaotic evil in
the Worldwound or the Abyss) for the purposes of alignment-detection effects, though this doesn't
change her actual alignment.

**At 8th Level:** She takes no penalties from the mildly chaos-aligned and mildly evil-aligned
planar traits and treats all opposed strongly aligned planar traits as if they were only mildly
aligned.

**Info:** A faithful wanderer doesn't have an _aura of good_ like other paladins do, as this would
give her presence away to hostile denizens of the Abyssal wastelands. Her other auras likewise don't
reveal her presence. The benefits of her _aura of courage, aura of resolve, aura of faith,_ and
_aura of righteousness_ affect only her.

**Replaces:** Aura of good, aura of justice

**Stalk Evil (Su)**

**Ability:** A faithful wanderer isn't interested in going out in a blaze of glory after exhausting
a limited ability to _smite evil._ Instead, she has developed techniques to evade, stalk, and punish
evil whenever necessary. She gains a +2 bonus on Knowledge, Perception, Sense Motive, Stealth, and
Survival checks against evil outsiders, as well as a +2 bonus on weapon attack and damage rolls
against them. These bonuses don't stack with [favored enemy](ref/ability/favored-enemy) bonuses.

**At 13th Level:** She also gains these bonuses against evil dragons.

**At 7th Level:** The faithful wanderer also gains these bonuses against undead.

**Replaces:** Smite evil

At 5th level: p!These bonuses +4.

At 10th level: p!These bonuses +6.

At 15th level: p!These bonuses +8.

At 20th level: p!These bonuses +10.

**Champion's Bond (Su)**

**Alters:** Divine bond

**At 20th Level:** Whenever her _divine bond_ is active, she gains several additional benefits, as
follows: Her DR improves to 5/-. Additionally, if she rolls a natural 20 on an attack roll against
an evil outsider and confirms the critical hit, the outsider is also subject to
[banishment](ref/spell/banishment), using the faithful wanderer's paladin level as the caster level
(her weapon and holy symbol automatically count as objects that the subject hates). Finally,
whenever she uses _lay on hands_ to heal herself, she heals the maximum possible amount of hit
points.

**At 5th Level:** A faithful wanderer must choose the weapon option of her _divine bond_ class
feature.

**Replaces:** Holy champion
