+++
id = "ref/arc-occultist/haunt-collector"
kind = "archetype"
title = "Haunt Collector"
aon = "ArchetypeDisplay.aspx?FixedName=Occultist%20Haunt%20Collector"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "haunt_collector", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]
[[sources]]
publication = "horror-adventures"
page = "62"

[fields]
kind = "archetype"
features = [
  { anchor = "possessed-possessions", level = 2 },
  { anchor = "hauntist", level = 5 },
  { anchor = "spirit-speaker", level = 8 },
  { anchor = "extricate-haunt" },
]
trades = [
  { replaces = "Aura sight", feature = "aura-sight", by = ["hauntist"] },
  { replaces = "Outside contact", feature = "outside-contact", by = ["spirit-speaker"] },
  { replaces = "Magic circles", feature = "magic-circles", by = ["extricate-haunt"] },
  { replaces = "binding circles", feature = "binding-circles", by = ["extricate-haunt"] },
  { replaces = "fast circles", feature = "fast-circles", by = ["extricate-haunt"] },
  { alters = "Implements", feature = "implements", by = ["possessed-possessions"] },
]
+++

Haunt collectors use items haunted by their former owners to create ghostly presences imbued with
psychic power.

## Possessed Possessions (Su) {#possessed-possessions}

At 2nd level, and every 4 occultist levels thereafter, when the haunt collector chooses an implement
school he doesn't already know, instead of using implements as normal for that school, he can gain
access to a haunted implement—a powerful, spirit-possessed item collected during his travels. When
he selects a haunted implement, he forsakes the resonant power from the item's implement group and
instead selects a spirit from the [medium's](ref/class/medium) list of
[spirits](ref/ability/spirits), gaining that spirit's seance boon in place of the resonant power. He
can also call upon the implement's haunting entity as a swift action to temporarily gain bonuses on
all checks associated with the selected legendary spirit's spirit bonus for 1 round. This spirit
bonus is equal to 1/2 the amount of mental focus invested in the implement, to a maximum bonus of
1 + 1 for every 4 occultist levels the haunt collector has. He can call upon this spirit bonus a
number of times per day equal to the amount of mental focus invested in the implement, though
invoking it doesn't expend any mental focus. Once the spirit type is selected for an implement, it
cannot be changed.

This ability alters implements.

## Hauntist (Su) {#hauntist}

At 5th level, a haunt collector with at least one haunted implement gains the medium's haunt
channeler class feature, with an effective medium level equal to his occultist level - 2.

This ability replaces aura sight.

## Spirit Speaker (Sp) {#spirit-speaker}

At 8th level, a haunt collector with at least one haunted implement can commune with the spirits
once per day. By holding a seance for 10 minutes, he can ask questions of a destroyed undead or a
neutralized or destroyed haunt. To use this ability on a corporeal undead, the haunt collector must
have the creature's head in his possession. For a haunt or incorporeal undead, this seance must be
held in the haunt's location or where the incorporeal undead was destroyed. Treat this ability as
_[speak with haunt](ref/spell/speak-with-haunt)_ or as
_[speak with dead](ref/spell/speak-with-dead)_ (but affecting only destroyed undead rather than only
corpses), using the haunt collector's occultist level as the caster level. He can perform this
seance one additional time per day at 12th level, and again at 16th level and 20th level.

This ability replaces outside contact.

## Extricate Haunt (Su) {#extricate-haunt}

The haunt collector can temporarily exorcise his haunted implements' possessing entities to
spontaneously create phenomena similar to [haunts](ref/rule/haunts) and imbue them with spells the
occultist knows. As a full-round action that provokes attacks of opportunity, the haunt collector
expends 1 point of mental focus to extricate an implement's spirit and infuse an adjacent square
with its ghostly presence while granting it the power to deliver a spell from the implement's
associated school (whose range is touch or greater) on the haunt collector's behalf. This action
consumes the spell just as if it had been cast, but the energy is held in check by the created haunt
until triggered by conditions set forth by the haunt collector. The conditions needed to trigger the
haunt's spell effect must be clear, although they can be general, using the guidelines of the
_[magic mouth](ref/spell/magic-mouth)_ spell. The haunt is stationary, and once the conditions for
the trigger are met, the spell is discharged normally, though it now originates from the haunt's
square.

The haunt itself is an invisible, incorporeal, spectral force, similar to a stationary
_[unseen servant](ref/spell/unseen-servant)_ with an undead aura for the purposes of spells such as
_[detect undead](ref/spell/detect-undead)_. It has a number of hit points equal to the double the
level of the spell used to create it + the occultist's Intelligence modifier. If triggered during
the same combat it is created, the haunt acts at initiative count 10; otherwise, when the trigger
occurs, the haunt initiates combat and acts at initiative count 10 on the surprise round. Other
creatures must succeed at a Perception check (DC = 10 + the haunt collector's occultist level) to
act in the surprise round. The haunt can be damaged by positive energy and anything else that can
harm haunts, and if destroyed before it is triggered, it dissipates harmlessly. If the haunt is
destroyed, it does not reform in its haunted implement until the occultist next invests his
implements with mental focus. If the haunt doesn't trigger before the occultist next invests his
implements with mental focus, the haunt dissolves at that point and reforms in its haunted
implement.

The haunt collector can use this ability a number of times per day equal to 1 + his Intelligence
modifier. While a haunting presence is extricated from its implement, the haunt collector does not
receive the benefit of the implement's seance boon, nor can he call upon the implement's spirit
bonus or use its focus powers, though he can still cast spells associated with the implement without
penalty. If the spell is discharged successfully (rather than the haunt being destroyed), the
spirit's presence returns to the haunt collector's implement the following round, and the seance
boon and spirit bonus abilities are again available to the haunt collector.

At 12th level, the haunt collector can create a free-roaming haunt by expending an additional point
of mental focus, granting it a fly speed of 10 feet with good maneuverability, which allows it to
change locations or seek targets, under the restrictions for trigger conditions as outlined above.
If the haunt wanders beyond [medium range](ref/rule/range) (measured from the haunt collector's
current position), it is instantly destroyed.

At 16th level, the haunt collector can extricate an implement's spirit as a standard action.

This ability replaces magic circles, binding circles, and fast circles.
