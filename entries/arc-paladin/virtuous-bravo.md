+++
id = "ref/arc-paladin/virtuous-bravo"
kind = "archetype"
title = "Virtuous Bravo"
source_ids = ["heroes-of-the-high-court"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "virtuous_bravo", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "heroes-of-the-high-court"
page = "12"

[fields]
kind = "archetype"
replaces = ["Mercy", "Spellcasting", "Aura of justice", "Holy champion"]
alters = ["Armor proficiency", "Smite evil"]
+++

Although no less a beacon of hope and justice than other paladins, virtuous bravos rely on their wit
and grace rather than might and strong armor.

**Weapon and Armor Proficiency**

**Alters:** Armor proficiency

**Info:** Virtuous bravos aren't proficient with heavy armor or shields (except for
[bucklers](ref/eq-armor/buckler)).

**Bravo's Finesse (Ex)**

**Ability:** A virtuous bravo can use her Dexterity modifier instead of her Strength modifier on
attack rolls with light or one-handed piercing melee weapons (though if she carries a shield, she
applies its armor check penalty to such attack rolls), and she can use her Charisma score in place
of her Intelligence score to meet prerequisites of combat feats.

**Special:** This ability counts as having the [Weapon Finesse](ref/feat/weapon-finesse) feat for
the purpose of meeting feat prerequisites.

**Bravo's Smite (Su)**

**Alters:** Smite evil

**Info:** When using _smite evil,_ a virtuous bravo doesn't gain a deflection bonus to AC.

**Nimble (Ex)**

**Gained:** At 3rd Level

**Passive:** A virtuous bravo gains a +1 dodge bonus to AC while wearing light armor or no armor.

**Replaces:** Mercy

**Special:** Anything that causes the virtuous bravo to lose her Dexterity bonus to AC also causes
her to lose this dodge bonus.

At 7th level: This bonus +2.

At 11th level: This bonus +3.

At 15th level: This bonus +4.

At 19th level: This bonus +5.

**Panache and Deeds (Ex)**

**Ability:** A virtuous bravo gains the [swashbuckler's](ref/class/swashbuckler) _panache_ class
feature along with the following swashbuckler deeds:
[dodging panache](ref/swashdeed/dodging-panache),
[menacing swordplay](ref/swashdeed/menacing-swordplay),
[opportune parry and riposte](ref/swashdeed/opportune-parry-and-riposte),
[precise strike](ref/swashdeed/precise-strike), and
[swashbuckler initiative](ref/swashdeed/swashbuckler-initiative).

**Gained:** At 4th Level

**Replaces:** Spellcasting

**Special:** The virtuous bravo's paladin levels stack with any swashbuckler levels when using these
deeds.

**Panache (Ex)**

**Action:** Ability

**Flavor:** Text from the swashbuckler ability

At the start of each day, you gain a number of panache points equal to your Charisma modifier
(minimum 1). Your panache goes up or down throughout the day, but usually cannot go higher than your
Charisma modifier (minimum 1), though feats and magic items can affect this maximum. You spend
panache to accomplish deeds, and regain panache in the following ways.

Each time you confirm a critical hit with a light or one-handed piercing melee weapon, you regain 1
panache point. Confirming a critical hit on a [helpless](ref/misc/helpless) or unaware creature or a
creature that has fewer Hit Dice than [half](ref/misc/fractions-and-rounding) your character level
doesn't restore panache.

When you reduce a creature to 0 or fewer hit points with a light or one-handed piercing melee weapon
attack while in combat, you regain 1 panache point. Destroying an unattended object, reducing a
helpless or unaware creature to 0 or fewer hit points, or reducing a creature that has fewer Hit
Dice than half your character level to 0 or fewer hit points doesn't restore any panache.

**Advanced Deeds (Ex)**

**Ability:** A virtuous bravo gains the following swashbuckler deeds:
[bleeding wound](ref/swashdeed/bleeding-wound), [evasive](ref/swashdeed/evasive),
[subtle blade](ref/swashdeed/subtle-blade), [superior feint](ref/swashdeed/superior-feint),
[swashbuckler's grace](ref/swashdeed/swashbucklers-grace), and targeted strike.

**Gained:** At 11th Level

**Replaces:** Aura of justice

**Bravo's Holy Strike (Su)**

**Ability:** When the virtuous bravo confirms a critical hit with a light or one-handed piercing
melee weapon, she can choose one of the following three effects in addition to dealing damage: the
target is rendered [unconscious](ref/misc/unconscious) for 1d4 hours, the target is
[paralyzed](ref/rule/paralyzed) for 2d6 rounds, or the target is slain. Regardless of the effect
chosen, the target can attempt a Fortitude save. On a success, the target is instead
[stunned](ref/misc/stunned) for 1 round (it still takes damage). The DC of this save is equal to
10 + 1/2 the virtuous bravo's paladin level + her Charisma modifier.

**Flavor:** A virtuous bravo becomes a master at dispensing holy justice with her blade.

**Gained:** At 20th Level

**Replaces:** Holy champion

**Special:** Once a creature has been the target of a bravo's holy strike, regardless of whether or
not it succeeds at the save, that creature is immune to that bravo's holy strike for 24 hours.
Creatures that are immune to critical hits are also immune to this ability.
