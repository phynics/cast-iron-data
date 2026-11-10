+++
id = "ref/arc-paladin/forgefathers-seeker"
kind = "archetype"
title = "Forgefather's Seeker"
source_ids = ["construct-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forgefathers_seeker", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "construct-handbook"
page = "13"

[fields]
kind = "archetype"
replaces = ["Detect evil", "Aura of faith", "Holy champion"]
alters = ["Smite evil", "Aura of justice"]
replaces_features = ["detect-evil", "aura-of-faith", "holy-champion"]
alters_features = ["smite-evil", "aura-of-justice"]
+++

Torag constantly seeks those who would use the power of creation to threaten or harm others. To this
end, he sends his seekers to locate constructs that are used for evil or that become uncontrollable.
These paladins are adept at battling constructed foes and guarding those threatened by such
creations.

**Prerequisites:** Must select [Torag](ref/faith/torag) as her patron deity.

**Detect Construct (Sp)**

**Ability:** A Forgefather's seeker can detect the presence of constructs at will. This functions as
the spell [aura sight](ref/spell/aura-sight), except the duration is 1 round and a Forgefather's
seeker learns the locations and power of all auras of all constructs, similar to
[detect undead](ref/spell/detect-undead).

**Replaces:** Detect evil

**Smite Construct (Su)**

**Ability:** This ability functions as the paladin's _smite evil_ ability, but it functions only
against constructs. Smiting a construct automatically bypasses any DR or
[hardness](ref/umr/hardness) a construct might have.

**Ability2:** A Forgefather's seeker can still _smite evil,_ but she adds only half her Charisma
bonus on attack rolls, adds only half of her level on damage rolls, and doesn't increase her bonus
damage against outsiders with the evil subtype, evil-aligned dragons, or undead.

**Alters:** Smite evil

**Special:** This otherwise functions as _smite evil_ for the purposes of feats, prerequisites, and
other effects.

**Aura of Destruction (Su)**

**Ability:** A Forgefather seeker grants her allies _smite construct_ with her _aura of justice_
ability instead of _smite evil._

**Alters:** Aura of justice

**Gained:** At 11th Level

**Aura of Unmaking (Su)**

**Gained:** At 14th Level

**Passive:** A Forgefather's seeker's weapons are treated as
[adamantine](ref/eq-material/adamantine) for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction). Any attack made against an enemy within 10 feet of
her is treated as adamantine for the purpose of overcoming damage reduction. This ability functions
only while a Forgefather's seeker is conscious, not if she is unconscious or dead.

**Replaces:** Aura of faith

**Forgefather's Champion (Su)**

**Ability:** Whenever she uses _smite construct_ and hits a construct, she can immediately attempt
to destroy the construct. The construct is reduced to 0 hit points and destroyed unless it succeeds
at a Will save (DC = 10 + half the Forgefather's seeker's level + the Forgefather's seeker's
Charisma modifier). After this destruction effect and the damage from the attack is resolved, the
_smite_ immediately ends.

**Flavor:** A Forgefather's seeker becomes capable of completely dismantling constructs.

**Gained:** At 20th Level

**Passive:** Her DR increases to 10/evil. In addition, whenever a Forgefather's seeker channels
positive energy or uses _lay on hands_ to heal a creature, she heals the maximum possible amount.

**Replaces:** Holy champion
