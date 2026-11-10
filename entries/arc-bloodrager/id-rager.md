+++
id = "ref/arc-bloodrager/id-rager"
kind = "archetype"
title = "Id Rager"
aon = "ArchetypeDisplay.aspx?FixedName=Bloodrager%20Id%20Rager"
source_ids = ["occult-origins", "psychic-anthology", "heroes-from-the-fringe"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "id_rager", path = "json/archetypes_bloodrager.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bloodrager" },
]
[[sources]]
publication = "occult-origins"
page = "23"

[fields]
kind = "archetype"
replaces = ["Bloodline", "all bloodline spells", "all bloodline powers", "Eschew materials", "All bloodline feats"]
alters = ["Spellcasting"]
replaces_features = ["bloodline", "eschew-materials"]
+++

An id rager lacks a supernatural taint to his blood, instead drawing power from pure emotion.

**Atavistic Avatar (Su)**

**Action:** Choice

**At 1st Level:** When the id rager enters a _bloodrage,_ he gains additional powers as if he were a
[phantom](ref/sidekick/phantom) with the emotional focus he selected as his atavistic focus. He is
considered to be both a phantom and a [spiritualist](ref/class/spiritualist) for the purposes of
abilities whose effect references both a phantom and a spiritualist, such as a dedication phantom's
_dutiful strike,_ and treats his bloodrager level as both his spiritualist level and his phantom Hit
Dice when determining abilities and save DCs. This ability does not allow the id rager to become
incorporeal.

**At 12th Level:** The id rager gains Skill Focus in both of the skills associated with his
atavistic focus. If circumstances cause him to lose one Skill Focus feat, he loses both.

**At 4th Level:** The id rager gains [Lightning Reflexes](ref/feat/lightning-reflexes),
[Great Fortitude](ref/feat/great-fortitude), or [Iron Will](ref/feat/iron-will) as a bonus feat.

**At 8th Level:** The id rager can meditate for 1 hour to change his atavistic focus for 24 hours or
until he decides to return to his permanent atavistic focus as a **free action**. When he changes
his focus, he loses access to his Skill Focus feat and the feat he gained at 4th level, and he
wields emotional focus powers as if his spiritualist level and phantom Hit Dice were 3 lower.

**Replaces:** Bloodline, all bloodline spells, all bloodline powers

An id rager chooses one emotional focus to define his core: anger, dedication, despair, fear,
hatred, jealousy, kindness, remorse, whimsey, or zeal. He gains [Skill Focus](ref/feat/skill-focus)
as a bonus feat in one skill associated with his atavistic focus.

- **[Anger](ref/emotionalfocus/anger):** Intimidate or Survival
- **[Dedication](ref/emotionalfocus/dedication):** Diplomacy or Sense Motive
- **[Despair](ref/emotionalfocus/despair):** Intimidate or Stealth
- **[Fear](ref/emotionalfocus/fear):** Intimidate or Stealth
- **[Hatred](ref/emotionalfocus/hatred):** Acrobatics or Perception
- **[Jealousy](ref/emotionalfocus/jealousy):** Appraise or Bluff
- **[Kindness](ref/emotionalfocus/kindness):** Diplomacy or Heal.^1^
- **[Remorse](ref/emotionalfocus/remorse):** Perception or Sense Motive
- **[Whimsey](ref/emotionalfocus/whimsey):** Acrobatics or Perception.^2^
- **[Zeal](ref/emotionalfocus/zeal):** Acrobatics or Survival

**Atavistic Caster**

**Alters:** Spellcasting

**At 4th Level:** An id rager's bloodrager spells are treated as
[psychic magic](ref/rule/psychic-magic). The bloodrager's _bloodrage_ does not prevent him from
casting spells with emotional components, and he is considered to be a psychic spellcaster for the
purposes of prerequisites (such as for the prerequisites of psychic duels and occult skill unlocks).

**Replaces:** Eschew materials

**Bonus Feats**

**At 12th Level:** He can select a third bonus feat from the list.

**At 15th Level:** He can select a fourth bonus feat from the list.

**At 18th Level:** He can select a fifth and final bonus feat from the list.

**At 6th Level:** An id rager can select one of the following feats as a bonus feat:
[Combat Casting](ref/feat/combat-casting), [Empath](ref/feat/empath),
[Extra Rage](ref/feat/extra-rage), [Intuitive Spell](ref/feat/intuitive-spell),
[Logical Spell](ref/feat/logical-spell), [Psychic Combatant](ref/feat/psychic-combatant),
[Psychic Defender](ref/feat/psychic-defender), [Psychic Healing](ref/feat/psychic-healing),
[Psychic Maestro](ref/feat/psychic-maestro), [Psychic Virtuoso](ref/feat/psychic-virtuoso),
[Raging Concentration](ref/feat/raging-concentration), [Spell Focus](ref/feat/spell-focus), or
[Spell Penetration](ref/feat/spell-penetration).

**At 9th Level:** He can select a second bonus feat from the list.

**Replaces:** All bloodline feats

^\[Psychic Anthology^(source/psychic\_anthology) pg. 4\]\{from=1\} ^\[Heroes from the
Fringe^(source/heroes\_from\_the\_fringe) pg. 17\]\{from=2\}
