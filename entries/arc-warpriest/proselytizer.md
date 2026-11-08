+++
id = "ref/arc-warpriest/proselytizer"
kind = "archetype"
title = "Proselytizer"
source_ids = ["cohorts-and-companions"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "proselytizer", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]

[fields]
kind = "archetype"
replaces = ["Sacred armor, 3rd-level bonus feat"]
alters = ["Weapon and armor proficiencies", "Sacred weapon", "Blessings", "Blessings (major)"]
+++

**Sources:** Cohorts and Companions pg 24\
The proselytizer is the perfect militant missionary. He seeks to win the hearts and lay claim to the
souls of those he meets, and - failing that - spreads the word of his deity at the edge of the
sword.

**Weapon and Armor Proficiencies**

**Alters:** Weapon and armor proficiencies

**Info:** A proselytizer does not gain proficiency with heavy armor or with all martial weapons,
though he does gain proficiency in his deity's favored weapon. If his deity's favored weapon is
unarmed strike, he gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a bonus
feat.

**Emotional Appeal**

**Flavor:** A proselytizer has great power over the emotions of others, wielding his voice like a
weapon to pierce the heart of listeners and bring them closer to communion with his deity's power.

**Info:** The warpriest adds the following spells to his warpriest spell list at the indicated spell
levels. He casts these as divine warpriest spells.

**Replaces:** Sacred armor, 3rd-level bonus feat

**Spells:** Charm person, rally point, wrath

**Spells:** Castigate, heroism, suggestion

**Spells:** Charm monster, lesser geas

**Spells:** Forced repentance, serenity

**Spells:** Mass castigate, mass suggestion

**Spells:** Antipathy, sympathy

**Sacred Subdual (Su)**

**Ability:** When a proselytizer uses his _sacred weapon_ damage in place of his normal weapon
damage, all damage he deals with that weapon is nonlethal damage.

**Alters:** Sacred weapon

**Blessing of Conversion**

**Alters:** Blessings

**At 3rd Level:** The proselytizer does not gain access to the minor blessings granted by his
_blessing_ class feature until 3rd level.

**Info:** The proselytizer always gains the conversion bonus (see below) upon converting an NPC,
rather than only the first time he does so each level. The bonuses overlap their durations, and do
not stack.

**Voice of the Faithful (Ex)**

**Alters:** Blessings (major)

**At 10th Level:** A proselytizer of can expend a use of his major blessing to be able to speak to
and understand any creature with a language for 1 hour.

### Converting NPCs

Cohorts and their masters often share alignment, but a common religion can be just as important. A
cohort may share a leader's faith when first recruited, or a PC may seek to convert a cohort as
their relationship develops.

While PCs may choose to change alignment, such changes for NPCs may require magical assistance (see
the [atonement](ref/spell/atonement) spell). Alternatively, you can proselytize for your patron
deity, using your powers of persuasion and social influence to indoctrinate an NPC in the dogma of
the faith while inspiring their fealty.

Converting an NPC to your faith is similar to modifying their reaction with Diplomacy. You can only
attempt to convert NPCs who are at least indifferent toward you, though you can take time to make a
hostile or unfriendly NPC indifferent, and then begin the process of conversion. The DC of a
conversion depends on how many conversion steps away from your faith an NPC is, starting at one
conversion step for an NPC with no significant faith who matches your faith's alignment. For each
step the NPC's alignment differs from the alignment of your faith, add one conversion step. If the
NPC already holds a significant religious belief, add an additional conversion step. Note that
servants of other faiths - including divine spellcasters who worship a deity and agents in the
employ of a formal religion - normally can never be converted to a new faith. The GM has final
discretion over whether an NPC will ever convert to your beliefs.

If the GM rules that an NPC can be converted, the DC to convert that NPC is 10 + the NPC's Hit
Dice + the NPC's Wisdom or Charisma modifier (whichever is higher) + 5 per conversion step. For
example, a 5th level warrior with a Wisdom of 12 and no existing significant faith and who is the
same alignment as your deity has a conversion DC of 21. Each conversion attempt requires at least an
hour of proselytizing, and you can attempt no more than one conversion check per week. For your
conversion attempt, roll a Diplomacy check and a Knowledge (religion) check at the DC determined
above. If you succeed at both checks, decrease the number of conversion steps for that NPC by one.
If you fail either check, you reinforce the NPC's existing faith and add one to the number of
conversion steps for that NPC. If you fail three checks over the course of a conversion effort, the
NPC rejects your faith and you cannot attempt another conversion for a year. However, if the number
of conversion steps ever reaches 0, you convince the NPC to adopt your religion. Note that this does
not necessarily change the NPC's alignment, so you could manage to convince a chaotic evil harpy to
worship her own very odd form of Shelyn.

While proselytizing is a reasonable activity for a religious adventurer, it should be handled with
sensitivity, both in character and at the gaming table. Having a PC repeatedly attempt to convert
NPCs who aren't interested is likely to result in worsening their attitude toward the character, and
significant effort may be required to restore those relationships. Some players may be uncomfortable
with too much time being spent on religious talk, in which case a GM is free to simply treat the
conversion as a skill check, without actually roleplaying the talks that allow the conversion check
to take place.

### Successful Conversion

Characters that successfully convert others to their faith can gain divine blessings for adding new
members to their religion. The first time at each character level a PC converts an NPC, they gain a
conversion bonus for a number of days equal to the level of the NPC converted. Typical conversion
bonuses for various faiths, and examples of classes likely to be interested in converting, are
listed on the following page. In the case of Neutral deities, the bonus may be a sacred or profane
bonus as most appropriate for the PC who gains it.

|Deity|Alignment|Classes|Bonus|
| --- | --- | --- | --- |
|[Abadar](ref/faith/abadar)|LN|Alchemist, cleric, investigator|Leader gains +2 sacred/profane bonus on Appraise checks|
|[Asmodeus](ref/faith/asmodeus)|LE|Inquisitor, investigator, slayer|Leader gains +2 profane bonus on Intimidate checks|
|[Calistria](ref/faith/calistria)|CN|Bard, slayer, witch|Leader gains +2 sacred/profane bonus on Bluff checks to feint|
|[Cayden Cailean](ref/faith/cayden-cailean)|CG|Brawler, skald, swashbuckler|Leader gains +2 sacred bonus on saves vs. fear and ingested poison|
|[Desna](ref/faith/desna)|CG|Bard, oracle, witch|Leader gains a +2 sacred bonus on saves vs. curses, divinations, and sleep effects|
|[Erastil](ref/faith/erastil)|LG|Hunter, ranger, shaman|Leader gains a +1 sacred bonus on damage rolls with a longbow|
|[Gorum](ref/faith/gorum)|CN|Bloodrager, fighter, warpriest|Leader gains a +1 sacred bonus on damage rolls with a greatsword|
|[Gozreh](ref/faith/gozreh)|N|Druid, ranger, shaman|Leader gains +2 sacred/profane bonus on Profession and Survival checks|
|[Iomedae](ref/faith/iomedae)|LG|Cavalier, paladin, warpriest|Leader gains +2 sacred bonus on Diplomacy checks|
|[Irori](ref/faith/irori)|LN|Alchemist, brawler, monk|Leader gains a +1 sacred bonus on damage rolls with unarmed strikes|
|[Lamashtu](ref/faith/lamashtu)|CE|Antipaladin, bloodrager, summoner|Leader gains a +1 bonus on damage rolls with natural weapons|
|[Nethys](ref/faith/nethys)|N|Arcanist, sorcerer, wizard|Leader gains a +2 sacred/profane bonus on Spellcraft checks|
|[Norgorber](ref/faith/norgorber)|NE|Alchemist, rogue, slayer|Leader gains a +2 sacred bonus on Stealth checks|
|[Pharasma](ref/faith/pharasma)|N|Arcanist, cleric, oracle|Leader gains a +2 sacred/profane bonus on Knowledge (religion) checks|
|[Rovagug](ref/faith/rovagug)|CE|Barbarian, brawler, fighter|Leader gains a +1 profane bonus on sunder combat maneuvers and attack and damage rolls and Strength checks against objects|
|[Sarenrae](ref/faith/sarenrae)|NG|Bard, cleric, swashbuckler|Leader gains a +1 sacred bonus to caster level for conjuration (healing) spells and spells with the light descriptor|
|[Shelyn](ref/faith/shelyn)|NG|Bard, skald, sorcerer|Leader gains a +1 sacred bonus to caster level for effects with the emotion descriptor (except fear effects)|
|[Torag](ref/faith/torag)|LG|Cavalier, fighter, paladin|Leader gains a +2 sacred bonus on Craft checks dealing with metal and on Profession (soldier) checks|
|[Urgathoa](ref/faith/urgathoa)|NE|Cleric, witch, wizard|Leader gains a +1 profane bonus to caster level for disease and death effects|
|[Zon-Kuthon](ref/faith/zon-kuthon)|LE|Alchemist, inquisitor, magus|Leader gains a +1 profane bonus to caster level for effects with the darkness or pain descriptor|
