+++
id = "ref/arc-bloodrager/id-rager"
kind = "archetype"
title = "Id Rager"
aon = "ArchetypeDisplay.aspx?FixedName=Bloodrager%20Id%20Rager"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "id_rager", path = "json/archetypes_bloodrager.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bloodrager" },
]
[[sources]]
publication = "occult-origins"
page = "23"
[[expanded_in]]
publication = "heroes-from-the-fringe"
page = "19"
via = "ref/emotionalfocus/whimsey"
[[expanded_in]]
publication = "psychic-anthology"
page = "5"
via = "ref/emotionalfocus/kindness"

[fields]
kind = "archetype"
features = [
  { anchor = "atavistic-avatar", level = 1 },
  { anchor = "atavistic-caster", level = 4 },
]
trades = [
  { replaces = "Bloodline", feature = "bloodline", by = ["atavistic-avatar"] },
  { replaces = "all bloodline spells", feature = "bloodline", power = "bloodline spell", by = ["atavistic-avatar"] },
  { replaces = "all bloodline powers", feature = "bloodline", power = "bloodline power", by = ["atavistic-avatar"] },
  { replaces = "Eschew materials", feature = "eschew-materials", by = ["atavistic-caster"] },
  { replaces = "All bloodline feats", feature = "bloodline", power = "bloodline feat" },
  { alters = "Spellcasting", feature = "spells", by = ["atavistic-caster"] },
]
+++

An id rager lacks a supernatural taint to his blood, instead drawing power from pure emotion.

## Atavistic Avatar (Su) {#atavistic-avatar}

An id rager chooses one emotional focus to define his core: anger, dedication, despair, fear,
hatred, jealousy, remorse (see page 19), or zeal. At 1st level, he gains
[Skill Focus](ref/feat/skill-focus) as a bonus feat in one skill associated with his atavistic
focus.

_[Anger](ref/emotionalfocus/anger)_: Intimidate or Survival.

_[Dedication](ref/emotionalfocus/dedication)_: Diplomacy or Sense Motive.

_[Despair](ref/emotionalfocus/despair)_: Intimidate or Stealth.

_[Fear](ref/emotionalfocus/fear)_: Intimidate or Stealth.

_[Hatred](ref/emotionalfocus/hatred)_: Acrobatics or Perception.

_[Jealousy](ref/emotionalfocus/jealousy)_: Appraise or Bluff.

_[Remorse](ref/emotionalfocus/remorse)_: Perception or Sense Motive.

_[Zeal](ref/emotionalfocus/zeal)_: Acrobatics or Survival.

When the id rager enters a bloodrage, he gains additional powers as if he were a
[phantom](ref/sidekick/phantom) with the emotional focus he selected as his atavistic focus. He is
considered to be both a phantom and a [spiritualist](ref/class/spiritualist) for the purposes of
abilities whose effect references both a phantom and a spiritualist, such as a dedication phantom's
dutiful strike, and treats his bloodrager level as both his spiritualist level and his phantom Hit
Dice when determining abilities and save DCs. This ability does not allow the id rager to become
incorporeal.

At 4th level, the id rager gains [Lightning Reflexes](ref/feat/lightning-reflexes),
[Great Fortitude](ref/feat/great-fortitude), or [Iron Will](ref/feat/iron-will) as a bonus feat.

At 8th level, the id rager can meditate for 1 hour to change his atavistic focus for 24 hours or
until he decides to return to his permanent atavistic focus as a free action. When he changes his
focus, he loses access to his Skill Focus feat and the feat he gained at 4th level, and he wields
emotional focus powers as if his spiritualist level and phantom Hit Dice were 3 lower.

At 12th level, the id rager gains Skill Focus in both of the skills associated with his atavistic
focus. If circumstances cause him to lose one Skill Focus feat, he loses both.

This ability replaces bloodline, all bloodline spells, and all bloodline powers.

## Atavistic Caster {#atavistic-caster}

At 4th level, a id rager's bloodrager spells are treated as [psychic magic](ref/rule/psychic-magic).
The bloodrager's bloodrage does not prevent him from casting spells with emotional components, and
he is considered to be a psychic spellcaster for the purposes of prerequisites (such as for the
prerequisites of psychic duels and occult skill unlocks). This ability alters the bloodrager's
spellcasting and replaces eschew materials.

## Bonus Feats {#bonus-feats}

At 6th level and every 3 bloodrager levels thereafter, an id rager can select one of the following
feats as a bonus feat: [Combat Casting](ref/feat/combat-casting), [Empath](ref/feat/empath),
[Extra Rage](ref/feat/extra-rage), [Intuitive Spell](ref/feat/intuitive-spell),
[Logical Spell](ref/feat/logical-spell), [Psychic Combatant](ref/feat/psychic-combatant),
[Psychic Defender](ref/feat/psychic-defender), [Psychic Healing](ref/feat/psychic-healing),
[Psychic Maestro](ref/feat/psychic-maestro), [Psychic Virtuoso](ref/feat/psychic-virtuoso),
[Raging Concentration](ref/feat/raging-concentration), [Spell Focus](ref/feat/spell-focus), or
[Spell Penetration](ref/feat/spell-penetration). This ability replaces all bloodline feats.
