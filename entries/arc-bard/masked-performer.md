+++
id = "ref/arc-bard/masked-performer"
kind = "archetype"
title = "Masked Performer"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Masked%20Performer"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "masked_performer", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "dual-identity", level = 1 },
  { anchor = "seamless-guise", level = 1 },
  { anchor = "exaggerated-pose", level = 3 },
  { anchor = "stage-combat", level = 6 },
  { anchor = "multiplicity-of-masks", level = 18 },
  { anchor = "social-grace", level = 2 },
  { anchor = "masked-talents", level = 5 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["dual-identity"] },
  { replaces = "Countersong", feature = "bardic-performance", power = "countersong", by = ["seamless-guise"] },
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["exaggerated-pose"] },
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["stage-combat"] },
  { replaces = "Mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["multiplicity-of-masks"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["social-grace"] },
  { replaces = "Lore master", feature = "lore-master", by = ["masked-talents"] },
]
+++

Not merely an entertainer in a disguise, the masked performer takes on the persona represented by
the likeness she wears. Her alter ego might be a theatrical archetype, a legendary hero, or a
revered spirit. Masked performers are often the stars of religious plays and festivals, and
aficionados easily recognize them and associate them with their most famous role.

## Dual Identity (Ex) {#dual-identity}

This ability acts as the [vigilante](ref/class/vigilante) ability of the same name, except as
follows. The masked performer's identities are referred to as social and masked, rather than social
and vigilante.

Unlike a vigilante, most people who know of the masked performer actually know that the masked
performer's identities are one and the same. Nonetheless, the dual identity ability is valuable to
the masked performer due to offering her two perspectives on any problem and two different
alignments.

This ability replaces bardic knowledge.

## Bardic Performance {#bardic-performance}

A masked performer gains the following types of bardic performance.

## Seamless Guise (Ex) {#seamless-guise}

At 1st level, a masked performer learns to behave in a way that appears perfectly proper and normal
for her current role, on stage or off. She can maintain this performance for 1 hour for every 3
rounds of bardic performance she spends. While this performance is active, she receives a +10 bonus
on Disguise and Perform (act) checks to remain in character after she has already established her
character. For instance, this bonus does not apply against the initial Perception check when meeting
a creature paying attention to her but does apply on the automatic additional Perception check each
hour of interacting.

This ability replaces countersong.

## Exaggerated Pose (Su) {#exaggerated-pose}

At 3rd level, a masked performer can enhance her own physical and social abilities by simply
altering her posture. When she starts this performance, the masked performer chooses a Strength-,
Dexterity-, or Charisma-based skill and gains a +2 competence bonus on checks with that skill as
long as she maintains this performance. This bonus increases by 1 for every 4 bard levels the masked
performer has beyond 3rd (+3 at 7th level, +4 at 11th level, +5 at 15th level, and +6 at 19th
level). The masked performer can change the chosen skill as a swift action. Exaggerated pose is an
emotion effect and relies on visual components.

This ability replaces inspire competence.

## Stage Combat (Su) {#stage-combat}

At 6th level, a masked performer gains the benefit of a combat feat she doesn't have as long as she
maintains this performance. The masked performer chooses the feat when she starts this performance.
The masked performer must meet all the feat's prerequisites. As usual when temporarily gaining a
feat, if the feat she chooses has any limitations on uses, such as
[Stunning Fist's](ref/feat/stunning-fist) daily uses, all uses of that combat feat while maintaining
stage combat count toward that feat's limit. In the case of Stunning Fist, if the masked performer
gained that feat again later the same day, the expended uses would remain expended. Stage combat
relies on visual components.

This ability replaces suggestion.

## Multiplicity of Masks (Su) {#multiplicity-of-masks}

At 18th level, a masked performer can cause any number of her allies to appear as herself or as
another ally within 60 feet. To be affected, an ally must be within 60 feet of the masker performer
and able to see her. As long as the masked performer maintains this performance, enemies perceive
all affected allies as the chosen character. If an affected ally is a different size or creature
type than the chosen character, enemies can attempt a Will save (DC = 10 + 1/2 the masked
performer's bard level + her Charisma modifier) to disbelieve. Otherwise, there is no saving throw,
but a successful attack against a disguised ally automatically reveals the ally's true form. If an
ally moves out of range, that ally reverts to his original form, and the entire effect ends if the
ally providing his appearance to the others moves out of range. Multiplicity of masks is an illusion
(glamer) effect that relies on visual components.

This ability replaces mass suggestion.

## Social Grace (Ex) {#social-grace}

At 2nd level, a masked performer gains the [social grace](ref/soctalent/social-grace) vigilante
social talent. She gains an additional skill with social grace 1 level later than a vigilante (at
6th level, 10th level, and so on).

This ability replaces versatile performance.

## Masked Talents {#masked-talents}

At 5th level, a masked performer gains a rogue talent from the following list:
[expert leaper](ref/talent/expert-leaper), [fast stealth](ref/talent/fast-stealth),
[ledge walker](ref/talent/ledge-walker), [rogue crawl](ref/talent/rogue-crawl),
[rope master](ref/talent/rope-master), [stand up](ref/talent/stand-up), and
[wall scramble](ref/talent/wall-scramble). At 17th level, a masked performer can choose any of the
above talents or an advanced talent from the following list:
[defensive roll](ref/talent/defensive-roll), [fast tumble](ref/talent/fast-tumble),
[hide in plain sight](ref/talent/hide-in-plain-sight), and
[skill mastery](ref/talent/skill-mastery). This ability does not qualify her for the
[Extra Rogue Talent](ref/feat/extra-rogue-talent) feat.

This ability replaces lore master.
