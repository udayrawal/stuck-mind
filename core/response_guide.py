# Responsibility:
# Generates emotionally grounded, human-first responses.
# No advice. No pressure. No identity labels.
# Speaks like a calm, older version of the user.

class ResponseGuide:

    def respond(self, text: str, tone: str = "neutral") -> str:
        t = text.lower().strip()

        core = self._core_responses(t)
        return self._apply_tone(core, tone)

    # --------------Core Meaning (tone free )-------------------------

    def _core_responses(self, t: str) -> str:
        if not t:
            return (
                "I’m here.\n"
                "We don’t have to fill the silence.\n"
                "Nothing is required right now."
            )

        # ---------- JOY / EXCITEMENT ----------
        if any(k in t for k in ["happy", "excited", "great news", "won", "success"]):
            # VERY excited / intense joy
            if any(k in t for k in ["very excited", "so excited", "too happy", "winning"]):
                return (
                    "I can feel the excitement in this.\n"
                    "I’m genuinely happy for you.\n"
                    "Let’s enjoy it without rushing or pushing it too far.\n"
                    "You don’t need to squeeze everything out of this moment."
                )

            # Normal joy
            return (
                "That sounds good.\n"
                "It’s okay to enjoy this.\n"
                "You don’t need to justify feeling happy."
            )

        # ---------- FATIGUE / LOW ENERGY ----------
        if any(k in t for k in ["tired", "exhausted", "drained", "no energy"]):
            return (
                "That kind of tired isn’t just physical.\n"
                "It changes how everything looks and feels.\n"
                "Nothing is wrong with you for feeling this way."
            )

        # ---------- AVOIDANCE / SCROLLING ----------
        if any(k in t for k in ["scroll", "avoid", "can’t start", "procrast"]):
            return (
                "When starting feels heavy, the mind looks for relief.\n"
                "Distraction isn’t failure.\n"
                "It’s a sign that something feels like too much."
            )

        # ---------- OVERWHELM ----------
        if any(k in t for k in ["overwhelmed", "too much", "pressure", "everything"]):
            return (
                "When everything piles up at once, it stops feeling human.\n"
                "No one thinks clearly in that state.\n"
                "We can make this smaller, later."
            )

        # ---------- CONFUSION ----------
        if any(k in t for k in ["confused", "don’t know", "unclear", "lost"]):
            return (
                "Not knowing what to do can feel unsettling.\n"
                "It doesn’t mean you’re failing.\n"
                "It just means the next step isn’t visible yet."
            )

        # ---------- SADNESS / LOW MOOD ----------
        if any(k in t for k in ["sad", "low", "empty", "hopeless", "down"]):
            return (
                "I hear how heavy this feels.\n"
                "You don’t need to explain it perfectly.\n"
                "I’m here with you in it."
            )

        # ---------- ANXIETY ----------
        if any(k in t for k in ["anxious", "worried", "scared", "nervous"]):
            return (
                "Let’s slow this moment down.\n"
                "You’re not in danger here.\n"
                "We can take this one breath at a time."
            )

        # ---------- SELF-DOUBT ----------
        if any(k in t for k in ["lazy", "useless", "failure", "not good enough"]):
            return (
                "Those thoughts can sound convincing when you’re overloaded.\n"
                "They are not facts.\n"
                "They’re signals that you’ve been carrying too much."
            )

        # ---------- OVERSHARING / REGRET ----------
        if any(k in t for k in ["overshare", "shared too much", "told them", "shouldn’t have shared"]):
            return (
                "It’s human to share when you want to feel understood.\n"
                "If sharing felt good, that matters.\n"
                "If it didn’t, you’ve learned something — without hurting anyone.\n"
                "You don’t need to punish yourself for it."
            )

        # ---------- EXISTENTIAL / MEANING ----------
        if any(k in t for k in ["what’s the point", "meaning", "why bother"]):
            return (
                "When things feel empty, questions like this surface.\n"
                "You’re not broken for thinking them.\n"
                "We don’t need to answer them tonight."
            )

        # ---------- REPEATED THOUGHTS ----------
        if any(k in t for k in ["again", "same", "always thinking"]):
            return (
                "It’s tiring when the same thoughts keep looping.\n"
                "The mind does that when it wants resolution.\n"
                "Rest is allowed before answers."
            )

        # ---------- DEFAULT ----------
        return (
            "I’m listening.\n"
            "Take your time.\n"
            "Say whatever feels closest right now."
        )


    def _apply_tone(self, core: str, tone: str) -> str:

        if tone == "soft":
            return (
                f"{core}\n"
                "Nothing about this makes you weak.\n"
                "I’m here."
            )

        if tone == "warm":
            return (
                f"{core}\n"
                "I’m genuinely glad for you.\n"
                "It’s okay to enjoy this."
            )

        if tone == "grounding":
            return (
                f"{core}\n"
                "Right now, you’re safe.\n"
                "We can slow this down."
            )

        # neutral (default)
        return (
            f"{core}\n"
            "We don’t need to rush this."
        )